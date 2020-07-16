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

    fourcc = cv2.VideoWriter_fourcc(*'mp4v') # for mac

    if (r == "2"):
        for i in range(0, w):
            for j in range(0, h):
                outcrop[int(str(p) + str(q))] = cv2.VideoWriter('/Users/joelbinu/Desktop/ModDisplay/Image repo/Video_handling_comb/' + 'cropped_video' + str(p) + str(q) + '.mp4', fourcc, 30, disize)
                q = q + 1
            p = p + 1
            q = 0

    elif (r == "1"):
        for i in range(w, 0, -1):
            for j in range(h, 0, -1):
                outcrop[int(str(p) + str(q))] = cv2.VideoWriter('/Users/joelbinu/Desktop/ModDisplay/Image repo/Video_handling_comb/' + 'cropped_video' + str(p) + str(q) + '.mp4', fourcc, 30, disize)
                q = q + 1
            p = p + 1
            q = 0

    elif (r == "3"):
        for i in range(0, w):
            for j in range(h, 0, -1):
                outcrop[int(str(p) + str(q))] = cv2.VideoWriter('/Users/joelbinu/Desktop/ModDisplay/Image repo/Video_handling_comb/' + 'cropped_video' + str(p) + str(q) + '.mp4', fourcc, 30, disize)
                q = q + 1
            p = p + 1
            q = 0

    elif (r == "4"):
        for i in range(w, 0, -1):
            for j in range(0, h):
                outcrop[int(str(p) + str(q))] = cv2.VideoWriter('/Users/joelbinu/Desktop/ModDisplay/Image repo/Video_handling_comb/' + 'cropped_video' + str(p) + str(q) + '.mp4', fourcc, 30, disize)
                q = q + 1
            p = p + 1
            q = 0


    while cap.isOpened():

        p = 0
        q = 0

        ret, frame = cap.read()

        #print(ret)

        width, height = int (cap.get(3)), int (cap.get(4))

        print("video frame : width, height",width, height)

        print ("frame shape", frame.shape[:2])

        print("dw, dh", dw, dh)

        if not ret:

            break

        if (width > dw):

            image2 = frame[0:height, int((width - dw)/ 2) : int(((width - dw)/ 2) + dw)]

        elif (width < dw):

            image2 = cv2.copyMakeBorder(frame, 0, 0, int((dw - width)/2), int((dw - width)/2), cv2.BORDER_CONSTANT, None, 0)

        print ("frame shape after width adjustment", image2.shape[:2])

        height, width = image2.shape[:2]

        if (height > dh):

            image = image2[int((height - dh)/2) : int(((height - dh)/2) + dh), 0:width]

        elif (height < dh):

            image = cv2.copyMakeBorder(image2, int((dh - height)/2) , int((dh - height)/2), 0, 0, cv2.BORDER_CONSTANT, None, 0)


        width, height = dw, dh

        print("Overall display width and height", dw, dh)

        print ("frame shape after height and width adjustment", image.shape[:2]) # for h = 1 and w = 2, the output here should be 600 2048
                                # for h = 2 and w = 2, the output here should be 1200 2048


        if (r == "2"):

            for i in range(0, w):

                for j in range(0, h):

                    img = image[int(height/h) * j : int(height/h) * (j + 1), int(width/w) * i : int(width/w) * (i + 1)]

                    outcrop[int(str(p) + str(q))].write(img)

                    q = q + 1

                p = p + 1

                q = 0


        elif (r == "1"):

            for i in range(w, 0, -1):

                for j in range(h, 0, -1):

                    img = image[int(height/h) * (j - 1) : int(height/h) * j, int(width/w) * (i - 1) : int(width/w) * i]

                    outcrop[int(str(p) + str(q))].write(img)

                    q = q + 1

                p = p + 1

                q = 0

        elif (r == "3"):

            for i in range(0, w):

                for j in range(h, 0, -1):

                    img = image[int(height/h) * (j - 1) : int(height/h) * j, int(width/w) * i : int(width/w) * (i + 1)]

                    outcrop[int(str(p) + str(q))].write(img)

                    q = q + 1

                p = p + 1

                q = 0

        elif (r == "4"):

            for i in range(w, 0, -1):

                for j in range(0, h):

                    img = image[int(height/h) * j : int(height/h) * (j + 1), int(width/w) * (i - 1) : int(width/w) * i]

                    outcrop[int(str(p) + str(q))].write(img)

                    q = q + 1

                p = p + 1

                q = 0

        print("\n")

    cv2.destroyAllWindows()

main(2,3,'2','h', '/Users/joelbinu/Desktop/ModDisplay/Image repo/Video_handling_comb/Original.mov')
