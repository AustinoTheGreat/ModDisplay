#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 18:10:43 2020

@author: joelbinu
"""
import cv2

r = "h"
h = 2
w = 3
dh = 0
dw = 0
tot = h * w

if r == "h":

    dh = h * 600
    dw = w * 1024

elif r == "v":

    dh = h* 1024
    dw = w * 600

outcrop = []

outcrop = ["" for x in range(0, tot+1)] # creating an array the size of the number of display connected for the output purposes

print (outcrop)

cap = cv2.VideoCapture('/Users/joelbinu/Desktop/ModDisplay /Image repo/Video_handling/cropped_video.mp4') # for testing on your local machine,change this link to the location of the cropped video that is produced by video_capability.py

fourcc = cv2.VideoWriter_fourcc(*'H264') # setting the codec for the video output. (can be mp4, avi, mov, ...) (codes can be found on openCV documentation)

#outcrop2 = cv2.VideoWriter('/Users/joelbinu/Desktop/ModDisplay /Image repo/cropped_video3.mp4', fourcc, 60, (1024, 600))

for counter in range(1,tot+1):

    outcrop[counter] = cv2.VideoWriter('/Users/joelbinu/Desktop/ModDisplay /Image repo/Video_handling/' + 'cropped_video' + str(counter) + '.mp4', fourcc, 60, (1024, 600)) # destination of each of the cropped videos



while True:

        ret, frame = cap.read()

        if not ret:

            break

        width, height = int (cap.get(3)), int (cap.get(4))

        counter = 0

        for i in range(0, h):

            for j in range(0, w):

                img = frame[int(height/h) * i : int(height/h) * (i + 1), int(width/w) * j : int(width/w) * (j + 1)]

                cv2.imshow("video", img)

                counter = counter + 1

                outcrop[counter].write(img)
