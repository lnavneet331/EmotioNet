import cv2
import numpy as np

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
    image_path = 'input_image.jpg'
    cropped_image = crop_face(image_path)
    cv2.imshow('Cropped Image', cropped_image)
    cv2.waitKey(0)
