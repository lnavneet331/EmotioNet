import os
import random
import shutil

def select_random_files(folder_path, num_files):
    # Get a list of all files in the folder
    all_files = os.listdir(folder_path)

    # Select a random subset of files
    random_files = random.sample(all_files, num_files)

    # Create a new folder to store the selected files
    selected_folder = os.path.join(f"short{folder_path}", 'selected_files')
    os.makedirs(selected_folder, exist_ok=True)
    print(f"Created a new folder at: {selected_folder}")

    # Copy the selected files to the new folder
    for file_name in random_files:
        file_path = os.path.join(folder_path, file_name)
        shutil.copy2(file_path, selected_folder)
        print(f"Copied file: {file_name}")

    print(f"Randomly selected {num_files} files and saved them in '{selected_folder}'.")

# Provide the path to your folder and the number of files to select
folder_path = 'dataset/Hatred'
num_files = 10000

select_random_files(folder_path, num_files)

folder_path = 'dataset/Happy'
num_files = 10000

select_random_files(folder_path, num_files)


folder_path = 'dataset/Neutral'
num_files = 10000

select_random_files(folder_path, num_files)


folder_path = 'dataset/Sad'
num_files = 10000

select_random_files(folder_path, num_files)