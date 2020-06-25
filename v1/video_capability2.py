#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 11:07:47 2020

@author: joelbinu
"""

import cv2

r = "h"
h = 2
w = 1
dh = 0
dw = 0

if r == "h":

    dh = h * 600
    dw = w * 1024

elif r == "v":

    dh = h* 1024
    dw = w * 600

cap = cv2.VideoCapture('/Users/joelbinu/Desktop/ModDisplay /Image repo/Microscope_5__Scientist__Videvo.mov')

while True:

    ret, frame = cap.read()

    width, height = int (cap.get(3)), int (cap.get(4))

    print (width, height)

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

    cv2.imwrite("/Users/joelbinu/Desktop/ModDisplay /Image repo/Produced_images/export-display" + ".jpg", image)

    #sky = frame[0:100, 0:200]

    for i in range(0, w):
        for j in range(0, h):
            (height, width) = image.shape[:2]
            img = image[int(height/h) * j : int(height/h) * (j + 1), int(width/w) * i : int(width/w) * (i + 1)]
            cv2.imshow("video", img)
            # cv2.waitKey(0)
            # cv2.destroyAllWindows()
            # cv2.imwrite("/Users/joelbinu/Desktop/ModDisplay /Image repo/Produced_images/export-display" + str(j) + str(i) + ".jpg", img)

    # cv2.imshow('Video', image)

    if cv2.waitKey(1) == 27:

        exit(0)

cv2.destroyAllWindows()
