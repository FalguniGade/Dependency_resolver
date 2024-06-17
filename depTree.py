import subprocess
import sys

def get_dep(package):
    try:
        # result = subprocess.run(
        #     ['pipdeptree',"-p",package],
        #     capture_output=True,
        #     text=True,
        #     check=True
        # )
        result = subprocess.run(
            ['pipdeptree'],
            capture_output=True,
            text=True,
            check=True
        )
        return result.stdout
    except Exception as e:
        print(f"Error retrieving depedencies for {package}")
        print(e)
        sys.exit(1)

if __name__ == "__main__":
    package_name = "requests"
    dep = get_dep(package_name)
    print("Rum")
    print(dep)

