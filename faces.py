import cv2
import numpy as np
from tqdm import tqdm

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

    if len(faces) == 0:
        print('No faces found in the image.')
        return None

    face = faces[0]
    (x, y, w, h) = face
    cropped_image = image[y:y + h, x:x + w]

    return cropped_image


if __name__ == '__main__':
    folder_path = "shortdataset/Surprised/selected_files"
    files = os.listdir(folder_path)

    for file_name in tqdm(files, desc="Processing images"):
        image_path = os.path.join(folder_path, file_name)
        cropped_image = crop_face(image_path)
        # Save the cropped image
        cv2.imwrite(image_path, cropped_image)