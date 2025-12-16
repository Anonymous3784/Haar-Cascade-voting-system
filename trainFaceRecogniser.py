import cv2
import os
import numpy as np
from IPython import display
from skimage import io
from skimage import color
import matplotlib.pyplot as plt


def get_detected_faces(cascade, test_image, scaleFactor, minNeighbours):
    # create a copy of the image to prevent any changes to the original one.
    image_copy = test_image.copy()

    #convert the test image to gray scale as opencv face detector expects gray images
    gray_image = cv2.cvtColor(image_copy, cv2.COLOR_BGR2GRAY)

    # Applying the haar classifier to detect faces
    faces_rect = cascade.detectMultiScale(gray_image, scaleFactor=scaleFactor, minNeighbors= minNeighbours)
    print("No. of faces found : " , len(faces_rect))
    faces = []
    for (x, y, w, h) in faces_rect:
        cv2.rectangle(image_copy, (x, y), (x+w, y+h), (0, 255, 0), 15)
        face = gray_image[y:y+h, x:x+w]
        faces.append(face)

    return image_copy, faces

haar_cascade_face = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')


def prepare_training_data_from_dataset():
    print("Preparing train data from dataset")
    faces = []
    labels = []
    count = 0

    
    for i in os.listdir('dataset'): #i is Giridhar folder
        count = count +1
        print("label "+ str(count) + " for " + i)
        names_text_file = open("names.txt","a")
        names_text_file.write(i+'\n')
        for j in os.listdir('dataset\\'+i): #j is image in Giridhar folder
            temp_face = cv2.imread('dataset/'+i+'/'+j, cv2.IMREAD_GRAYSCALE)
            label = count
            # full, face = get_detected_faces(haar_cascade_face, temp_face, 1.2, 5)
            # if(len(face)):
                # faces.append(face[0])
                # labels.append(label)
            faces.append(temp_face)
            labels.append(label)
        names_text_file.close()
    return [faces, labels]

# os.remove("names.txt")
open('names.txt', 'w').close()
[faces, labels] = prepare_training_data_from_dataset()
print( "Faces :" +  str(len(faces)) + "   Labels :" + str(len(labels)))

print("Dataset prepared")
# #TRAINING
face_recognizer = cv2.face.LBPHFaceRecognizer_create()
print("Training dataset")
face_recognizer.train(faces, np.array(labels))

print("Training complete")
face_recognizer.write('model.yml') 
