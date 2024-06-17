import requests

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

def print_version_history(version_history):
    if version_history is not None:
        print(f"Version History for {package_name}:\n")
        for version, release_info in version_history.items():
            print(f"Version: {version}")
            print("Release Date:", release_info[0]['upload_time'])
            print("URL",release_info[0]["url"])
            print("\n")

if __name__ == "__main__":
    package_name = input("Enter the package name: ")

    version_history = get_version_history(package_name)

    if version_history:
        print_version_history(version_history)
