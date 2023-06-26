import os
from shutil import copyfile
from tqdm import tqdm

raw = "raw"
dst = "dataset"
count = 0

def create_folder_if_not_exists(folder_path):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        print(f"Created folder: {folder_path}")

for folder in os.listdir(raw):    #get the folder names
    for sub_folder in os.listdir(f"raw/{folder}"):     #get emotion folders
        for image in os.listdir(f"raw/{folder}/{sub_folder}"):  #get images
            if image.endswith('.jpg'):
                image_path = os.path.join(sub_folder, image)
                dst_path = os.path.join(f"{dst}/{sub_folder}", image)
                try:
                    copyfile(f"raw/{folder}/{sub_folder}/{image}", dst_path)
                except FileNotFoundError:
                    create_folder_if_not_exists(f"{dst}/{sub_folder}")
                count += 1
                print(count)
        