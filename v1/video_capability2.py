#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 11:07:47 2020

@author: joelbinu
"""

import cv2


r = "h"
h = 2
w = 3
dh = 0
dw = 0


if r == "h":

    dh = h * 600
    dw = w * 1024

elif r == "v":

    dh = h* 1024
    dw = w * 600




cap = cv2.VideoCapture('/Users/joelbinu/Desktop/ModDisplay /Image repo/Video_handling/Original.mov') # for teesting on your local machine, change this path to the source of the original video

fourcc = cv2.VideoWriter_fourcc(*'mp4v')

outcrop = cv2.VideoWriter('/Users/joelbinu/Desktop/ModDisplay /Image repo/Video_handling/cropped_video.mp4', fourcc, 60, (dw, dh)) # destination of the cropped video for the entire display orientation


while True:

    ret, frame = cap.read()

    width, height = int (cap.get(3)), int (cap.get(4))

    if not ret:

        break

    if (width > dw):
        image = frame[0:height, int((width - dw)/ 2) : int(((width - dw)/ 2) + dw)]
    else:
        image = cv2.copyMakeBorder(frame, 0, 0, int((dw - width)/2), int((dw - width)/2), cv2.BORDER_CONSTANT, None, 0)

    if (height > dh):
        image = image[int((height - dh)/2) : int(((height - dh)/2) + dh), 0:width]
    else:
        image = cv2.copyMakeBorder(image, int((dh - height)/2) , int((dh - height)/2), 0, 0, cv2.BORDER_CONSTANT, None, 0)

    cv2.imshow('Video', image)

    outcrop.write(image)

cap.release()
outcrop.release()
cv2.destroyAllWindows()

