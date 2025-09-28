import os


def find_substring_in_file(file_path, substring):
    """
    Searches for a given substring in a specified file.
    :param file_path: Path to the file where the search will take place.
    :param substring: The substring to search for.
    :return: True if substring is found, otherwise False.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            return substring in content
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return False


def search_directory_for_substring(directory, substring):
    """
    Recursively searches through all files in a directory for a specific substring.
    :param directory: The root directory to start the search.
    :param substring: The substring to search for.
    :return: A list of file paths where the substring is found.
    """
    found_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            if find_substring_in_file(file_path, substring):
                found_files.append(file_path)
    return found_files


if __name__ == '__main__':
    # Example usage
    search_path = '.'  # Change this to the directory you want to search
    substring_to_find = 'your_substring_here'  # Change this to your target substring
    found_files = search_directory_for_substring(search_path, substring_to_find)
    print('Files containing the substring:', found_files)