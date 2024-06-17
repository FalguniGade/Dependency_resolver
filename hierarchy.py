import ast
import os
from collections import defaultdict

def extract_functions_and_classes_from_file(file_path):
    functions_and_classes = {'functions': set(), 'classes': defaultdict(set)}

    with open(file_path, 'r', encoding='utf-8') as file:
        try:
            tree = ast.parse(file.read(), filename=file_path)
        except SyntaxError as e:
            print(f"Error parsing {file_path}: {e}")
            return functions_and_classes

        class_stack = []

        def visit_function(node):
            functions_and_classes['functions'].add(node.name)
            for inner_node in ast.walk(node):
                if isinstance(inner_node, ast.FunctionDef) and inner_node != node:
                    visit_function(inner_node)

        for node in ast.walk(tree):
            if isinstance(node, ast.ClassDef):
                class_stack.append(node.name)
            elif isinstance(node, ast.FunctionDef):
                if class_stack:
                    class_name = '.'.join(class_stack)
                    functions_and_classes['classes'][class_name].add(node.name)
                    visit_function(node)
                else:
                    functions_and_classes['functions'].add(node.name)

    return functions_and_classes

def extract_functions_and_classes_from_package(package_path):
    functions_and_classes = {'functions': set(), 'classes': defaultdict(set)}

    for root, _, files in os.walk(package_path):
        for file in files:
            if file.endswith('.py'):
                file_path = os.path.join(root, file)
                extracted_data = extract_functions_and_classes_from_file(file_path)

                functions_and_classes['functions'].update(extracted_data['functions'])
                functions_and_classes['classes'].update(extracted_data['classes'])

    return functions_and_classes

def print_hierarchy(data):
    for class_name, class_functions in data['classes'].items():
        print(f"\nClass: {class_name}")
        print(f"  Functions: {', '.join(sorted(class_functions))}")

    print("\nFunctions:")
    for function_name in sorted(data['functions']):
        print(f"  - {function_name}")

if __name__ == "__main__":
    package_path = "C:\\DepedencyResolver\\TempPackages\\seaborn"

    if not os.path.exists(package_path):
        print(f"The specified package path '{package_path}' does not exist.")
    else:
        extracted_data = extract_functions_and_classes_from_package(package_path)

        print("\nHierarchy of Functions and Classes in the Package:")
        print_hierarchy(extracted_data)
