import os
import ast

def extract_imports_from_file(file_path):
    with open(file_path,'r',encoding='utf-8') as file:
        try:
            tree = ast.parse(file.read(),filename=file_path)
        except SyntaxError as e:
            print(f"Error parsing {file_path}: {e}")
            return []

        imports = set()
        for node in ast.walk(tree):
            if isinstance(node,ast.Import):
                for alias in node.names:
                    imports.add(alias.name)
            elif isinstance(node, ast.ImportFrom):
                for alias in node.names:
                    imports.add(alias.name)
    return imports


dr = "C:\\Library-Management-System-main"
def detect_imports_in_dir(directory):
    all_imports = set()
    for root,_,files in os.walk(directory):
        for file in files:
            if file.endswith(".py"):
                file_path = os.path.join(root,file)
                file_imports = extract_imports_from_file(file_path)
                all_imports.update(file_imports)
    return all_imports

file_path = "C:\\Library-Management-System-main\\LMS\\library\\views.py"
print(extract_imports_from_file(file_path))
print(detect_imports_in_dir(dr))


def extract_functions_from_file(file_path):
    # List of all the functions used from external packages
    with open(file_path, 'r', encoding='utf-8') as file:
        try:
            tree = ast.parse(file.read(), filename=file_path)
        except SyntaxError as e:
            print(f"Error parsing {file_path}: {e}")
            return []

        functions = set()
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                functions.add(node.name)
    return functions

def extract_imported_functions_from_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        try:
            tree = ast.parse(file.read(), filename=file_path)
        except SyntaxError as e:
            print(f"Error parsing {file_path}: {e}")
            return []

        imported_functions = set()
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                for alias in node.names:
                    module_name = alias.name
                    imported_functions.update(get_functions_from_module(module_name))
            elif isinstance(node, ast.ImportFrom):
                module_name = node.module
                imported_functions.update(get_functions_from_module(module_name))
    return imported_functions

def get_functions_from_module(module_name):
    # Gets all the functions in a module
    try:
        module = __import__(module_name, fromlist=[''])
        return set(filter(callable, map(getattr, [module] * len(dir(module)), dir(module))))
    except (ImportError, AttributeError) as e:
        print(f"Error importing module '{module_name}': {e}")
        return set()


print(extract_imported_functions_from_file(file_path))