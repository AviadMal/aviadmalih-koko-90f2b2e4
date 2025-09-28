import os

# Function to recursively search for a substring in files

def find_substring_in_file(file_path, substring):
    """
    Check if the substring exists in the given file.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            if substring in content:
                print(f'Substring found in: {file_path}')
    except (UnicodeDecodeError, FileNotFoundError):
        print(f'Cannot read file: {file_path}')


def search_directory_for_substring(directory, substring):
    """
    Recursively search through all files in a directory for a substring.
    """
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            find_substring_in_file(file_path, substring)


if __name__ == '__main__':
    directory_to_search = 'path_to_directory'  # Set this to your target directory
    substring_to_find = 'מכרוזת'  # Set this to the substring you want to find
    search_directory_for_substring(directory_to_search, substring_to_find)