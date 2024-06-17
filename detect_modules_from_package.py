import ast
import os

def extract_functions_and_classes_from_file(file_path):
    functions_and_classes = {'functions': set(), 'classes': set()}

    with open(file_path, 'r', encoding='utf-8') as file:
        try:
            tree = ast.parse(file.read(), filename=file_path)
        except SyntaxError as e:
            print(f"Error parsing {file_path}: {e}")
            return functions_and_classes

        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                functions_and_classes['functions'].add(node.name)
            elif isinstance(node, ast.ClassDef):
                functions_and_classes['classes'].add(node.name)

    return functions_and_classes

def extract_functions_and_classes_from_package(package_path):
    functions_and_classes = {'functions': set(), 'classes': set()}

    for root, _, files in os.walk(package_path):
        for file in files:
            if file.endswith('.py'):
                file_path = os.path.join(root, file)
                extracted_data = extract_functions_and_classes_from_file(file_path)

                functions_and_classes['functions'].update(extracted_data['functions'])
                functions_and_classes['classes'].update(extracted_data['classes'])

    return functions_and_classes

if __name__ == "__main__":
    package_path = "C:\\DepedencyResolver\\TempPackages\\seaborn"

    if not os.path.exists(package_path):
        print(f"The specified package path '{package_path}' does not exist.")
    else:
        extracted_data = extract_functions_and_classes_from_package(package_path)

        print("\nFunctions in the Package:")
        for function in sorted(extracted_data['functions']):
            print(f"  - {function}")
        print("\nClasses in the Package:")
        for class_name in sorted(extracted_data['classes']):
            print(f"  - {class_name}")
