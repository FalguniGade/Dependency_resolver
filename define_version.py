from find_used_import_functions import extract_called_functions
from used_imports import detect_imports_in_dir,extract_imports_from_file
from detect_modules_from_package import extract_functions_and_classes_from_package

script_path = "C:\\Library-Management-System-main\\LMS\\library\\views.py"
package_path = "C:\\DepedencyResolver\\TempPackages\\seaborn"

function_used = set(extract_called_functions(script_path))
package_fun = set(extract_functions_and_classes_from_package(package_path)['functions'])
imports = extract_imports_from_file(script_path)


print(function_used.intersection(package_fun))
print(package_fun)
print(function_used)



