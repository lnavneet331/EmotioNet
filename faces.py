import cv2
import numpy as np
from tqdm import tqdm
import os

def crop_face(image_path):
    """Crops everything except the face in an image.

    Args:
        image_path (str): The path to the image file.

    Returns:
        numpy.ndarray: The cropped image.
    """

    image = cv2.imread(image_path)
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    faces = face_cascade.detectMultiScale(
        image,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
    )
    #print(image_path)
    height, width, channels = image.shape
    #print("Image dimensions: {} x {} pixels, {} channels".format(width, height, channels))
    if height == 48 and width == 48:
        print('Image already 48x48 pixels')
        return image
    if len(faces) == 0:
        print('No faces found in the image.')   
        cropped_image = cv2.resize(image, (48, 48))
        print('Cropped image dimensions: {} x {} pixels'.format(cropped_image.shape[1], cropped_image.shape[0]))
        return cropped_image
        
    face = faces[0]
    (x, y, w, h) = face
    cropped_image = image[y:y + h, x:x + w]
    #resize the image to 48x48 pixels
    cropped_image = cv2.resize(cropped_image, (48, 48))
    print('Cropped image dimensions: {} x {} pixels'.format(cropped_image.shape[1], cropped_image.shape[0]))
    return cropped_image


if __name__ == '__main__':
    count = 0
    folder_path = "shortdataset/Surprised/selected_files"
    for file_name in os.listdir(folder_path):
        image_path = os.path.join(folder_path, file_name)
        cropped_image = crop_face(image_path)
        # Save the cropped image
        cv2.imwrite(image_path, cropped_image)
        count += 1
        print(count)