import os
from shutil import copyfile
from tqdm import tqdm

emotions = {
    'Happy': [12, 25],
    'Sad': [4, 15],
    'Fearful': [1, 4, 20, 25],
    'Angry': [4, 7, 24],
    'Surprised': [1, 2, 25, 26],
    'Disgusted': [9, 10, 17],
    'Happily sad': [4, 6, 12, 25],
    'Happily surprised': [1, 2, 12, 25],
    'Happily disgusted': [10, 12, 25],
    'Sadly fearful': [1, 4, 15, 25],
    'Sadly angry': [4, 7, 15],
    'Sadly surprised': [1, 4, 25, 26],
    'Sadly disgusted': [4, 10],
    'Fearfully angry': [4, 20, 25],
    'Fearfully surprised': [1, 2, 5, 20, 25],
    'Fearfully disgusted': [1, 4, 10, 20, 25],
    'Angrily surprised': [4, 25, 26],
    'Disgusted surprise': [1, 2, 5, 10],
    'Happily fearful': [1, 2, 12, 25, 26],
    'Angrily disgusted': [4, 10, 17],
    'Awed': [1, 2, 5, 25],
    'Appalled': [4, 9, 10],
    'Hatred': [4, 7, 10]
}

dst_dir = 'raw'

count = 0
total_images = 1068550  # Total number of images

# Get the names of images from the txt files
text_files = "emotioNet_challenge_files"

discovered_emotions = []

for filename in os.listdir(text_files):
    if filename.endswith('.txt'):
        file_path = os.path.join(text_files, filename)
        with open(file_path, 'r') as file:
            lines = file.readlines()
            progress_bar = tqdm(lines, desc="Copying images", unit="image")
            for line in progress_bar:
                data = line.strip().split('	')
                data.pop(1)
                image_url = data[0]
                au_values = data[1:]
                
                image_name = os.path.basename(image_url)
                
                emotion = None
                for emotion, au_list in emotions.items():
                    match = True
                    for au in au_list:
                        if au > len(au_values) or au_values[au - 1] != '1':
                            match = False
                            break
                    if match:
                        break
                corresponding_emotion = emotion
                if emotion not in discovered_emotions:
                    discovered_emotions.append(emotion)

                path_to_save = image_url.replace("https://s3.us-east-2.amazonaws.com/emotionet/Images/", "")
                directory = path_to_save.split("/")[0]
                
                if not os.path.exists(dst_dir + "/" + directory + "/" + corresponding_emotion):
                    os.makedirs(dst_dir + "/" + directory + "/" + corresponding_emotion)
                
                try:
                    copyfile(f"whole/{path_to_save}", dst_dir + "/" + directory + "/" + corresponding_emotion + "/" + path_to_save.replace(directory + "/", ""))
                except FileNotFoundError:
                    count += 1
                progress = count / total_images * 100
                progress_bar.set_postfix({"Progress": "{:.2f}%".format(progress)})

print(discovered_emotions)
print(f"Total number of discovered emotions: {len(discovered_emotions)}")

"""

# print the list of images 
import os
from shutil import copyfile
emotions = {
    'Happy': [12, 25],
    'Sad': [4, 15],
    'Fearful': [1, 4, 20, 25],
    'Angry': [4, 7, 24],
    'Surprised': [1, 2, 25, 26],
    'Disgusted': [9, 10, 17],
    'Happily sad': [4, 6, 12, 25],
    'Happily surprised': [1, 2, 12, 25],
    'Happily disgusted': [10, 12, 25],
    'Sadly fearful': [1, 4, 15, 25],
    'Sadly angry': [4, 7, 15],
    'Sadly surprised': [1, 4, 25, 26],
    'Sadly disgusted': [4, 10],
    'Fearfully angry': [4, 20, 25],
    'Fearfully surprised': [1, 2, 5, 20, 25],
    'Fearfully disgusted': [1, 4, 10, 20, 25],
    'Angrily surprised': [4, 25, 26],
    'Disgusted surprise': [1, 2, 5, 10],
    'Happily fearful': [1, 2, 12, 25, 26],
    'Angrily disgusted': [4, 10, 17],
    'Awed': [1, 2, 5, 25],
    'Appalled': [4, 9, 10],
    'Hatred': [4, 7, 10]
}

dst_dir = 'raw'

count = 0
#get the names of images from the txt files
text_files = "emotioNet_challenge_files"
for filename in os.listdir(text_files):
    if filename.endswith('.txt'):
        file_path = os.path.join(text_files, filename)
        with open(file_path, 'r') as file:
            for line in file:
                data = line.strip().split('	')
                data.pop(1)
                image_url = data[0]
                au_values = data[1:]
                #print(au_values)
                image_name = os.path.basename(image_url)
                #print(image_url)
                #print(image_name)
                #give the corresponding emotion to each image from AU
                corresponding_emotion = ""
                emotion_list = []
                index = 0
                for i in au_values:
                    index += 1
                    if i == "1":
                        emotion_list.append(index)
                #print(emotion_list)
                #exit()
                #check the emotion list with the emotions dictionary
                if len(emotion_list) == 0:
                    continue
                for emotion in emotions:
                    if emotion_list == emotions[emotion]:
                        corresponding_emotion = emotion
                        break
                #add this to the corresponding folder
                path_to_save = image_url.replace("https://s3.us-east-2.amazonaws.com/emotionet/Images/", "")
                #print(path_to_save)
                #save the image to the correct folder
                directory = path_to_save.split("/")[0]
                #print(directory)
                if corresponding_emotion == "":
                    continue
                #print(image_url, corresponding_emotion)
                if not os.path.exists(dst_dir + "/" + directory + "/" + corresponding_emotion):
                    os.makedirs(dst_dir + "/" + directory + "/" + corresponding_emotion)
                copyfile(f"whole/{path_to_save}", dst_dir + "/" + directory + "/" +corresponding_emotion + "/" + path_to_save.replace(directory + "/", ""))
                count += 1
                print("Copied: {count}/1068550 images".format(count=count))
"""
