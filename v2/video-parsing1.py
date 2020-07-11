#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 13:38:59 2020
@author: joelbinu
"""
import cv2

def main(h, w, r, o, address):

    p = 0; q = 0

    dh = 0; dw = 0

    tot = h * w

    if o == "h":

        disize = (1024, 600)

        dh = h * 600

        dw = w * 1024

    if o == "v":

        disize = (600, 1024)

        dh = h * 1024

        dw = w * 600

    final = int(str(h+1) + str(w+1))

    outcrop = []

    outcrop = ["" for x in range(0, final)] # creating an array the size of the number of display connected for the output purposes


    cap = cv2.VideoCapture(address) # for testing on your local machine, change this path to the source of the original video



    fourcc = cv2.VideoWriter_fourcc(*'avc1') # for mac



    #for counter in range(1,tot+1):

    #    outcrop[counter] = cv2.VideoWriter('/Users/joelbinu/Desktop/ModDisplay/Image repo/Video_handling_comb/' + 'cropped_video' + str(counter) + '.mp4', fourcc, 30, disize) # destination of each of the cropped videos


    if (r == "2"):
        for i in range(0, w):
            for j in range(0, h):
                outcrop[int(str(p) + str(q))] = cv2.VideoWriter('export/display' + 'cropped_video' + str(p) + str(q) + '.mp4', fourcc, 30, disize)
                q = q + 1
            p = p + 1
            q = 0

    elif (r == "1"):
        for i in range(w, 0, -1):
            for j in range(h, 0, -1):
                outcrop[int(str(p) + str(q))] = cv2.VideoWriter('export/display' + 'cropped_video' + str(p) + str(q) + '.mp4', fourcc, 30, disize)
                q = q + 1
            p = p + 1
            q = 0

    elif (r == "3"):
        for i in range(0, w):
            for j in range(h, 0, -1):
                outcrop[int(str(j) + str(i))] = cv2.VideoWriter('export/display' + 'cropped_video' + str(p) + str(q) + '.mp4', fourcc, 30, disize)
                q = q + 1
            p = p + 1
            q = 0

    elif (r == "4"):
        for i in range(w, 0, -1):
            for j in range(0, h):
                outcrop[int(str(j) + str(i))] = cv2.VideoWriter('export/display' + 'cropped_video' + str(p) + str(q) + '.mp4', fourcc, 30, disize)
                q = q + 1
            p = p + 1
            q = 0



    while True:

        p = 0
        q = 0

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


        if (r == "2"):

            for i in range(0, w):

                for j in range(0, h):

                    img = image[int(height/h) * j : int(height/h) * (j + 1), int(width/w) * i : int(width/w) * (i + 1)]

                    counter = counter + 1

                    outcrop[int(str(j) + str(i))].write(img)

                    q = q + 1

                p = p + 1

                q = 0

        elif (r == "1"):

            for i in range(w, 0, -1):

                for j in range(h, 0, -1):

                    img = image[int(height/h) * (j - 1) : int(height/h) * j, int(width/w) * (i - 1) : int(width/w) * i]

                    counter = counter + 1

                    outcrop[int(str(p) + str(q))].write(img)

                    q = q + 1

                p = p + 1

                q = 0

        elif (r == "3"):

            for i in range(0, w):

                for j in range(h, 0, -1):

                    img = image[int(height/h) * (j - 1) : int(height/h) * j, int(width/w) * i : int(width/w) * (i + 1)]

                    counter = counter + 1

                    outcrop[int(str(j) + str(i))].write(img)

                    q = q + 1

                p = p + 1

                q = 0

        elif (r == "4"):

            for i in range(w, 0, -1):

                for j in range(0, h):

                    img = image[int(height/h) * j : int(height/h) * (j + 1), int(width/w) * (i - 1) : int(width/w) * i]

                    counter = counter + 1

                    outcrop[int(str(j) + str(i))].write(img)

                    q = q + 1

                p = p + 1

                q = 0




    cv2.destroyAllWindows()
