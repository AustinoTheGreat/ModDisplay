#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 13:38:59 2020

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

    o = (1024, 600)

    dh = h * 600

    dw = w * 1024

if r == "w":

    o = (600, 1024)

    dh = h * 1024

    dw = w * 600

outcrop = []

outcrop = ["" for x in range(0, tot+1)] # creating an array the size of the number of display connected for the output purposes


cap = cv2.VideoCapture('/Users/joelbinu/Desktop/ModDisplay/Image repo/Video_handling_comb/Original.mov') # for testing on your local machine, change this path to the source of the original video



fourcc = cv2.VideoWriter_fourcc(*'mp4v') # for mac


for counter in range(1,tot+1):

    outcrop[counter] = cv2.VideoWriter('/Users/joelbinu/Desktop/ModDisplay/Image repo/Video_handling_comb/' + 'cropped_video' + str(counter) + '.mp4', fourcc, 30, (1024,600)) # destination of each of the cropped videos

#the extension for the file will need to change depending on the OS


while True:



    ret, frame = cap.read()

    #print(ret)

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

    counter = 0

    width, height = dw, dh

    for i in range(0, h):

        for j in range(0, w):

            img = image[int(height/h) * i : int(height/h) * (i + 1), int(width/w) * j : int(width/w) * (j + 1)]

            counter = counter + 1

            cv2.imshow("image", img)

            outcrop[counter].write(img)

    key = cv2.waitKey(1)

    if key == 32:
        timestamp = [cap.get(cv2.CAP_PROP_POS_MSEC)]
        continue


print(timestamp)
cv2.destroyAllWindows()
