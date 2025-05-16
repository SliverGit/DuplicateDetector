import os

def find_duplicates(directory):
    """
    Finds all duplicate files in the given directory and its subdirectories.

    Args:
        directory (str): The path to the root directory to search for duplicates.

    Returns:
        dict: A dictionary where each key is a tuple containing the size, name and type of a file,
              and the corresponding value is a list of paths to files with that size and name.
    """
    # Initialize an empty dictionary to store the sizes and their corresponding files
    size_name_type_dict = {}

    # Walk through the directory and its subdirectories
    for root, dirs, files in os.walk(directory):
        for file in files:
            # Get the full path of the current file
            file_path = os.path.join(root, file)

            # Calculate the size of the current file
            file_size = os.path.getsize(file_path)

            # Get the name and type of the current file
            file_name, file_extension = os.path.splitext(file)
            file_type = 'file' if file_extension else 'directory'

            # If the size is already in the dictionary, add the file to its list
            key = (file_size, file_name, file_type)
            if key in size_name_type_dict:
                size_name_type_dict[key].append(file_path)
            else:
                # Otherwise, add the size and the file to the dictionary
                size_name_type_dict[key] = [file_path]

    # Filter out files that appear only once (i.e., they are not duplicates)
    duplicate_files = {key: paths for key, paths in size_name_type_dict.items() if len(paths) > 1}

    return duplicate_files


def output_duplicates(duplicate_files):
    """
    Outputs the list of duplicate files to a text file.

    Args:
        duplicate_files (dict): A dictionary where each key is a tuple containing
                                the size, name and type of a file,
                                and the corresponding value is a list of paths
                                to files with that size and name.
    """
    # Open a new file in write mode
    with open('duplicates.txt', 'w') as f:
        for key, paths in duplicate_files.items():
            # Write the size, name and type of its corresponding files to the file
            size, name, _ = key
            f.write(f"Size: {size} bytes\nName: {name}\nType: Directory/File\n")
            for path in paths:
                f.write(f"- {path}\n")


def calculate_storage_saved(duplicate_files):
    """
    Calculates the total storage space saved if all duplicates were to be removed.

    Args:
        duplicate_files (dict): A dictionary where each key is a tuple containing
                                the size, name and type of a file,
                                and the corresponding value is a list of paths
                                to files with that size and name.

    Returns:
        int: The total storage space saved in bytes.
    """
    # Initialize a variable to store the total storage space saved
    total_storage_saved = 0

    # Walk through the dictionary of duplicate files
    for key, paths in duplicate_files.items():
        # Calculate the size of each file
        _, _, _ = key
        size = os.path.getsize(paths[0])

        # Add the size to the total storage space saved, only deleting all but one of each duplicate
        total_storage_saved += (len(paths) - 1) * size

    return total_storage_saved


if __name__ == "__main__":
    directory = input("Enter the directory path: ")

    # Find all duplicate files in the given directory and its subdirectories
    duplicate_files = find_duplicates(directory)

    # Output the list of duplicate files to a text file
    output_duplicates(duplicate_files)

    # Calculate the total storage space saved if all duplicates were to be removed
    storage_saved = calculate_storage_saved(duplicate_files)

    # Print a message when complete with the total of duplicate files found and storage space saved
    print(f"Total duplicate files found: {sum(len(paths) for paths in duplicate_files.values())}")
    print(f"Total storage space saved if all duplicates were to be removed: {storage_saved} bytes")
