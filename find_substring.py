import os


def find_substring_in_file(file_path, substring):
    """
    Checks if the given substring is present in the specified file.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            if substring in content:
                print(f'Substring found in file: {file_path}')
    except Exception as e:
        print(f'Error reading {file_path}: {e}')


def search_directory_for_substring(directory_path, substring):
    """
    Recursively searches through the directory for files containing the substring.
    """
    for dirpath, _, filenames in os.walk(directory_path):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            find_substring_in_file(file_path, substring)


if __name__ == '__main__':
    directory_to_search = 'path/to/search'  # Change this path to the directory you want to search
    substring_to_find = 'מכרוזת'  # Substring to find
    search_directory_for_substring(directory_to_search, substring_to_find)