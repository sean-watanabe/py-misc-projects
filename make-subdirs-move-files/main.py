import os
import sys
import shutil
import math

def create_folder(destination_path, number_to_create):
    '''
    "destination_path" parameter (:str) is a folder path in which new folders are created, whereas
    "number_to_create" parameter (:int) specifies how many folders to create
    '''
    try:
        # Validates the arguments
        if not isinstance(destination_path, str):
            raise TypeError('The destination_path must be a string.')
        if not isinstance(number_to_create, int):
            raise TypeError('The number of sub-files to create must be a integer.')
        if number_to_create < 0:
            raise ValueError('The number of sub-files to create must be a positive integer.')

        # .DS_Store will be handled as a directory, causing an error. 
        # This removes .DS_Store if it exists in the destination directory.
        ds_store_path = os.path.join(destination_path, ".DS_Store")
        if os.path.exists(ds_store_path):
            os.remove(ds_store_path)
            # print(".DS_Store file has been removed from the destination directory.")

        for i in range(1, number_to_create + 1):
            if i < 10:
                folder_name = f'0{i}'
            else:
                folder_name = f'{i}'
            
            new_folder_path = os.path.join(destination_path, folder_name)
            os.makedirs(new_folder_path, exist_ok=True)
        
        print("\nNew folders successfully created!")

    except TypeError as te:
        print(f"Oops! An error occurred while creating sub folders \nError: {te}")
        sys.exit(1)
    except ValueError as ve:
        print(f"Oops! An error occurred while creating sub folders \nError: {ve}")
        sys.exit(1)
    except Exception as e:
        print(f"OOPS! An unexpected error occurred while creating sub folders \nError: {e}")
        sys.exit(1)

def move_files(source_folder_path, destination_folder_path):
    '''
    "source_folder_path" parameter (:str) is a folder path where the original files exist, whereas
    "destination_folder_path" parameter (:str) accepts the path to the destination folder
    '''
    try:
        # Validates the arguments
        if not isinstance(source_folder_path, str):
            raise TypeError('The source folder path must be a string.')
        if not isinstance(destination_folder_path, str):
            raise TypeError('The number of sub-files to create must be a integer.')
        if (len(source_folder_path) < 5) or (len(destination_folder_path) < 5):
            raise ValueError('The entered path seems not right. Check it and try again.')

        for directory in sorted(os.listdir(destination_folder_path)):

            target_directory = os.path.join(destination_folder_path, directory)
            
            remaining_files = sorted(os.listdir(source_folder_path))

            if len(remaining_files) >= number_of_files_per_folder:
                slice_index = slice(number_of_files_per_folder)
            else:
                slice_index = slice(len(remaining_files))

            for file in remaining_files[slice_index]:
                source_file = os.path.join(source_folder_path, file)
                moved_file = os.path.join(target_directory, file)

                shutil.move(source_file, moved_file)
        
        print("\nFiles successfully moved to the destination folder!")

    except TypeError as te:
        print(f"Oops! An error occurred while moving files. \nError: {te}")
        sys.exit(1)
    except ValueError as ve:
        print(f"Oops! An error occurred while moving files. \nError: {ve}")
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


# Defines paths to the source and destination directories
source_directory = str(input("Enter the source folder path.\nSource path: "))

# Creates a list of the files in the source folder, which is used to calculate "files per folder"
source_files = os.listdir(source_directory)

# Remove .DS_Store in the source folder, as the .DS_Store file is counted and 
# treated as a file to be moved.
ds_store_path = os.path.join(source_directory, ".DS_Store")
if os.path.exists(ds_store_path):
    os.remove(ds_store_path)
    # print(".DS_Store file has been removed from the source directory.")

if len(source_files) == 0:
    print("\nThere are no files in the source folder.")
    sys.exit(1)


destination_directory = str(input("\nEnter the destination folder path. \nDestination path: "))

# Defines the number of files to be stored in each destination folder
number_of_files_per_folder = int(input("\nHow many files should each subfolder store?\nFiles per sub folders: "))

number_of_folders_needed = math.ceil(len(source_files) / number_of_files_per_folder)

create_folder(destination_directory, number_of_folders_needed)
move_files(source_directory, destination_directory)
