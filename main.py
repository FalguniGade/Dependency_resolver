import argparse
import sys
import download_extract_whl

def main():
    parser = argparse.ArgumentParser(description="Accept Path")

    # Add command-line arguments
    parser.add_argument('--path', help='User name', required=True)

    # Parse the command-line arguments
    args = parser.parse_args()

    # Access the values of the arguments
    path = args.path

    # Print the user information
    print(f"name: {path}")

    download_extract_whl.install_and_execute_pipreqs(path)

if __name__ == "__main__":
    # If path is not provided, print a default suggestion
    if len(sys.argv) < 2:
        print("Usage: python main.py --path <path_to_directory>")
        sys.exit(1)

    main()