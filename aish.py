import RPi.GPIO as GPIO
import time
import pygame
import cv2
import sys
import os

pygame.mixer.init()

GPIO.setmode(GPIO.BCM)

TRIG = 23
ECHO = 24
while 1:

    GPIO.setmode(GPIO.BCM)
    print "Distance Measurement In Progress"
    GPIO.setup(TRIG,GPIO.OUT)
    GPIO.setup(ECHO,GPIO.IN)

    GPIO.output(TRIG, False)
    print "Waiting For Sensor To Settle"
    time.sleep(2)

    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)

    while GPIO.input(ECHO)==0:
        pulse_start = time.time()

    while GPIO.input(ECHO)==1:
        pulse_end = time.time()
    pulse_duration = pulse_end - pulse_start

    distance = pulse_duration * 17150

    distance = round(distance, 2)

    print "Distance:",distance,"cm"
    if distance <= 30:
        
        count = 5
        print("Initializing Alert sound")
        while count>0:
            pygame.mixer.music.load("alert001.mp3")
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy() == True:
                continue
            count-=1
        os.system('python image_capture.py')
        time.sleep(2)
    GPIO.cleanup()
