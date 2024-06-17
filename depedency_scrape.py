# https://pypi.org/pypi/<package>/<version>/json
import requests

def get_dep(package,version):
    package_name = package
    version = version
    base_url = f"https://pypi.org/pypi/{package_name}/{version}/json"
    package = requests.get(base_url,verify=False).json()
    return package['info']['requires_dist']

def get_package_name(s):
    s = s.split(" ")[0]
    s2 = ""
    for i in s:
        if i.isalpha() or (i == "-" or i == "_"):
            s2 += i
    return s2

def get_package_versions(s):
    versions_list = s.split(";")[0].split(",")
    v = []
    temp = ""
    for versions in versions_list:
        for i in versions:
            if not i.isalpha() and (i != "-" and i != "_"):
                temp += i
        v.append(temp.strip())
        temp = ""
    return v

for j in get_dep(package="seaborn",version="0.13.0"):
    print(get_package_name(j),get_package_versions(j))
    # print(get_package_name(j.split(" ")[0]))

# import ast # <2
#
# ast.walk()
#
# import ast # >= 2
# ast.AST.walk() 