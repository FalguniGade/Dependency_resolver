import os
import subprocess
import zipfile
from tempfile import TemporaryDirectory

# Replace 'path/to/pipreqs.whl' with the actual path to the pipreqs .whl file
whl_file_path = 'C:\\DepedencyResolver\\TempPackages\\pipreqs-0.4.13.dist-infol'
temp = 'C:\\DepedencyResolver\\TempPackages\\'

def install_and_execute_pipreqs(whl_path):
    # Create a temporary directory to extract the contents of the .whl file
    #
    #     with zipfile.ZipFile(whl_path, 'r') as zip_ref:
    #         zip_ref.extractall(temp)
    #
    #     # Navigate to the extracted directory
    #     extracted_dir = os.path.join(temp, os.listdir(temp)[0])
    #     os.chdir(extracted_dir)

        # Install the pipreqs module
        subprocess.run(['pip', 'install', 'pipreqs'],stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

        # Execute 'pipreqs .' command in the terminal
        subprocess.run(['pipreqs', '--force',whl_path])

if __name__ == "__main__":
    if not os.path.exists(whl_file_path):
        print(f"Error: The specified .whl file '{whl_file_path}' does not exist.")
    else:
        install_and_execute_pipreqs(whl_file_path)
