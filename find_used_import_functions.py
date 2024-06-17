import re
import ast


def findre(s):
    pattern = r"Name\(id='([^']+)',\s*ctx=Load\(\)\)|attr='([^']+)'"
    matches = re.findall(pattern, s)
    matches = [value for match in matches for value in match if value]
    return matches


def extract_called_functions(file_path):
    called_functions = set()

    with open(file_path, 'r', encoding='utf-8') as file:
        try:
            tree = ast.parse(file.read(), filename=file_path)
        except SyntaxError as e:
            print(f"Error parsing {file_path}: {e}")
            return called_functions

        for node in ast.walk(tree):
            if isinstance(node,ast.Attribute):
                att_value = ast.dump(node.value)
                attr_values = findre(att_value)
                # get full scrapy.crawler....
                val = ".".join(attr_values)
                # only get last value
                called_functions.add(node.attr)


            if isinstance(node, ast.Call):
                if isinstance(node.func, ast.Name):
                    function_name = node.func.id
                    called_functions.add(function_name)

    return called_functions

if __name__ == "__main__":
    script_path = "C:\\Library-Management-System-main\\LMS\\library\\views.py"

    try:
        called_functions = extract_called_functions(script_path)

        if called_functions:
            print("\nCalled Functions:")
            for function_name in sorted(called_functions):
                print(f"  - {function_name}")
        else:
            print("\nNo called functions found.")
    except Exception as e:
        print(f"\nError: {e}")
