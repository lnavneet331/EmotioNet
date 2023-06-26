import os

counter = []
def count_files_in_subfolders(folder_path):
    for root, dirs, files in os.walk(folder_path):
        if files:
            print(f"Sub-folder: {root} -   Number of files: {len(files)}")
            counter.append(len(files))

# Provide the path to your folder
folder_path = 'dataset'

count_files_in_subfolders(folder_path)
print(f"Average number of files per sub-folder: {sum(counter)/len(counter)}")
