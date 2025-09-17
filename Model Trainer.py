import cv2
import numpy as np
from PIL import Image
import os

path = 'samples'

# Ensure that the 'cv2.face' module is available
if not hasattr(cv2.face, 'LBPHFaceRecognizer_create'):
    raise ImportError("The cv2.face module is not available. Make sure you have opencv-contrib-python installed.")

recognizer = cv2.face.LBPHFaceRecognizer_create()
detector = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

def Images_And_Labels(path):
    imagePaths = [os.path.join(path, f) for f in os.listdir(path)]
    faceSamples = []
    ids = []

    for imagePath in imagePaths:
        gray_image = Image.open(imagePath).convert('L')
        img_arr = np.array(gray_image, 'uint8')
        
        id = int(os.path.split(imagePath)[-1].split(".")[1])
        faces = detector.detectMultiScale(img_arr)
        
        for (x, y, w, h) in faces:
            faceSamples.append(img_arr[y:y+h, x:x+w])
            ids.append(id)

    return faceSamples, ids

print("Training faces. It will take a few seconds. Wait...")

faces, ids = Images_And_Labels(path)

# Debug prints to check if faces and ids are loaded correctly
print(f"Number of faces detected: {len(faces)}")
print(f"IDs detected: {ids}")

if len(faces) == 0 or len(ids) == 0:
    print("No faces or IDs found. Please check your dataset and path.")
else:
    recognizer.train(faces, np.array(ids))
    recognizer.write('trainer/trainer.yml')
    print("Model trained, now we can recognize your face.")