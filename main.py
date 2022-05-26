import cv2
import numpy as np
import face_recognition
import os
from datetime import datetime

path = 'image'
images = []
personNames = []
myList = os.listdir(path)
print(myList)
for cu_img in myList:
    current_Img = cv2.imread(f'{path}/{cu_img}')
    images.append(current_Img)
    personNames.append(os.path.splitext(cu_img)[0])
print(personNames)

def faceEncodings(images):
    encodeList = []
