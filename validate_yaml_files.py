import os
import yaml
import sys

def get_yaml_files_in_directory(directory):
    yaml_files = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.yaml') or file.endswith('.yml'):
                yaml_files.append(os.path.join(root, file))
    return yaml_files

def validate_yaml_file(file_path):
    try:
        with open(file_path, 'r') as file:
            yaml.safe_load(file)
        return None
    except yaml.YAMLError as error:
        return f"Error in {file_path}: {error}"

def validate_all_yaml_files(files):
    invalid_files = []
    for file in files:
        error_message = validate_yaml_file(file)
        if error_message:
            invalid_files.append((file, error_message))
    return invalid_files

def main():
    if len(sys.argv) < 2:
        print("Usage: python validate_yaml.py <directory>")
        sys.exit(1)

    directory = sys.argv[1]
    yaml_files = get_yaml_files_in_directory(directory)
    invalid_files = validate_all_yaml_files(yaml_files)

    if invalid_files:
        print("\nThe following YAML files are invalid:")
        for file, error_message in invalid_files:
            print(f"- {file}: {error_message}")
        sys.exit(2)
    else:
        print("All YAML files are valid.")

if __name__ == "__main__":
    main()
