import os
import requests
import tempfile
import zipfile
from wheel import wheelfile
from pipreqs_method import install_and_execute_pipreqs

def get_version_history(package_name):
    url = f"https://pypi.org/pypi/{package_name}/json"

    try:
        response = requests.get(url)
        response.raise_for_status()
        package_data = response.json()
        releases = package_data.get('releases', {})
        return releases
    except requests.exceptions.RequestException as e:
        print(f"Error fetching version history for {package_name}: {e}")
        return None

def rename_file(old_name, new_name):
    try:
        os.rename(old_name, new_name)
        print(f"File '{old_name}' has been renamed to '{new_name}'.")
    except FileNotFoundError:
        print(f"Error: File '{old_name}' not found.")
    except FileExistsError:
        print(f"Error: A file with the name '{new_name}' already exists.")

def delete_file(file_path):
    try:
        os.remove(file_path)
        print(f"File '{file_path}' has been deleted.")
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except PermissionError:
        print(f"Error: Permission denied. Unable to delete '{file_path}'.")


def download_and_extract_wheel(package_name,version,release_info,download_dir):
    try:
        response = requests.get(release_info[0]['url'])
        response.raise_for_status()

        with tempfile.NamedTemporaryFile(delete=False,suffix='.whl') as temp_file:
            temp_file.write(response.content)

        fname = release_info[0]['filename']
        wheel_path = temp_file.name
        curr_dir = wheel_path.split("\\")
        curr_dir.pop()
        new_path = ""
        for i in curr_dir:
            new_path += i + "\\"
        new_path += fname
        rename_file(wheel_path,new_path)

        with wheelfile.WheelFile(new_path) as wheel:
            wheel.extractall(download_dir)

        install_and_execute_pipreqs("")
        delete_file(new_path)

        print(f"Downloaded and extracted {package_name}-{version} to {download_dir}")
    except requests.exceptions.RequestException as e:
        print(f"Error downloading and extracting {package_name}-{version}: {e}")

if __name__ == "__main__":
    package_name = "seaborn"
    download_dir = "C:\\DepedencyResolver\\TempPackages"

    # Ensure the download directory exists
    os.makedirs(download_dir, exist_ok=True)

    # Get version history
    version_history = get_version_history(package_name)

    if version_history:
        for version,release_info in version_history.items():
            if release_info[0]['filename'].endswith(".whl"):
                download_and_extract_wheel(package_name, version, release_info, download_dir)
                break
