import cv2
import sys
import os
import pygame
pygame.mixer.init()

faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')  #machine learning model for recognizing faces

image = cv2.imread('image.jpg')                          #read the image
image = cv2.resize(image, (0,0), fx=0.5, fy=0.5)        #resize the image to half of its current size
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)          #convert the image to grayscale to ease up the process

#detect faces in the image
faces = faceCascade.detectMultiScale(gray, 1.1, 8)     #(grayscale image, scale factor, minimum number of neighbours) last 1 helps in decreasing errors in face detection

print("Found {0} Human(s)!".format(len(faces)))
if len(faces) >= 1: #if number of faces detected is more than or equals one, play mp3 file
       pygame.mixer.music.load("sound.mp3")
       pygame.mixer.music.play()
       while pygame.mixer.music.get_busy() == True:
            continue
     

#Draw a rectangle around the faces
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)    # draw a rectangle around the face detected(colored image, top-left corner, bottom right corner, green color, threshold value)
    
cv2.imshow("Faces found", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
