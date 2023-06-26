import os
import csv
import requests

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


output_dir = 'dataset'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

for emotion in emotions.keys():
    emotion_dir = os.path.join(output_dir, emotion)
    if not os.path.exists(emotion_dir):
        os.makedirs(emotion_dir)

dataset_folder = 'emotioNet_challenge_files'
discovered_emotions = []
for filename in os.listdir(dataset_folder):
    if filename.endswith('.txt'):
        file_path = os.path.join(dataset_folder, filename)
        
        with open(file_path, 'r') as file:
            for line in file:
                data = line.strip().split('	')
                data.pop(1)
                image_url = data[0]
                au_values = data[1:]
                
                emotion = None
                for emotion, au_list in emotions.items():
                    match = True
                    for au in au_list:
                        if au > len(au_values) or au_values[au - 1] != '1':
                            match = False
                            break
                    if match:
                        break
                
                if emotion not in discovered_emotions:
                    discovered_emotions.append(emotion)


            """
                if emotion:
                    emotion_dir = os.path.join(output_dir, emotion)
                    image_name = os.path.basename(image_url)
                    image_path = os.path.join(emotion_dir, image_name)
                    response = requests.get(image_url, stream=True)
                    print(image_url)
                    if response.status_code == 200:
                        with open(image_path, 'wb') as image_file:
                            for chunk in response.iter_content(1024):
                                image_file.write(chunk)
                        print(f"Downloaded image: {image_name} for emotion: {emotion}")
                    else:
                        print(f"Failed to download image: {image_name} for emotion: {emotion}")
                else:
                    print(f"No matching emotion found for image URL: {image_url}")
            """
print(discovered_emotions)
print(len(discovered_emotions))