import os


def find_pattern_in_file(file_path, pattern):
    """Search for a given pattern in a file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                if pattern in line:
                    print(f'Pattern found in {file_path}: {line.strip()}')
    except Exception as e:
        print(f'Error reading {file_path}: {e}')


def search_directory(directory, pattern):
    """Recursively search for a pattern in all files within a directory."""
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            find_pattern_in_file(file_path, pattern)


def main():
    # Define the directory to search and the pattern to find
    directory_to_search = './'  # Change this to your target directory
    pattern_to_find = 'מכרוזת'  # The pattern you want to find

    # Start the search
    search_directory(directory_to_search, pattern_to_find)


if __name__ == '__main__':
    main()