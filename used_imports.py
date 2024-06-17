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
                # for alias in node.names:
                #     imports.add(alias.name)
                imports.add(node.module.split(".")[0])
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