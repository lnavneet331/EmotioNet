import cv2

image = cv2.imread("dataset/Angrily Surprised/N_0000000202_00058.jpg")
height, width, channels = image.shape
print("Image dimensions: {} x {} pixels, {} channels".format(width, height, channels))