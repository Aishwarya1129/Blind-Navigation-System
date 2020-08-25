import cv2
import sys
import os

ramp_frames = 30    #Number of frames to throw away while the camera adjusts to the light levels

camera = cv2.VideoCapture(0)

def get_image():
    retval, im = camera.read()
    return im
    
#Ramp the camera - these frames will be discarded and are only used to adjust light levels if necessary
for i in xrange(ramp_frames):
    temp = get_image()

print("Taking Image...")
camera_capture = get_image()
file = "image.jpg"
cv2.imwrite(file, camera_capture)
del(camera)
os.system('python face_detect.py')
