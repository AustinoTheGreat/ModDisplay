#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 18:10:43 2020

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

cap = cv2.VideoCapture('/Users/joelbinu/Desktop/ModDisplay /Image repo/cropped_video2.mp4')

fourcc = cv2.VideoWriter_fourcc(*'mp4v')

outcrop2 = cv2.VideoWriter('/Users/joelbinu/Desktop/ModDisplay /Image repo/cropped_video3.mp4', fourcc, 60, (1024, 600))


#for i in range(0, w):

#    for j in range(0, h):

while True:

    ret, frame = cap.read()

    if not ret:

        break

    width, height = int (cap.get(3)), int (cap.get(4))

    img = frame[int(height/h) * 1 : int(height/h) * (1 + 1), int(width/w) * 0 : int(width/w) * (0 + 1)]

    cv2.imshow("video", img)

    outcrop2.write(img)


#while True:

    #ret, frame = cap.read()


    #if not ret:
    #    break

    #cv2.imshow("video", frame)

    #outcrop2.write(frame)
