#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# maybe this link will help
"""
Created on Mon Jun 22 13:26:26 2020
@author: joelbinu
"""
from cv2 import cv2

global height
global width

image = cv2.imread('pic/old_campus.jpg')

def crop(im, n_width, n_height, width, height):

    image2 = im[int ((height - n_height)/2) : int (((height - n_height)/2) + n_height),  int ((width - n_width)/ 2) : int (((width - n_width)/ 2) + n_width), ]
    return image2

def border_man(im, width, height, w_width, w_height):
     im = cv2.copyMakeBorder(im, int ((w_height - height)/2) , int ((w_height - height)/2) , int ((w_width - width)/2), int ((w_width - width)/2), cv2.BORDER_CONSTANT, None, 0)
     return im

m1 = 1
m2 = 1

im = image

(height, width) = image.shape[:2]
print(str(height) + " " + str(width))

if (m1 == 0) and (m2 == 0):
    if (width > 1024) or (height > 600):
        im = crop(image, 1024, 600, width, height)
elif (m1 == 1) and (m2 == 0):
    if (width > 2048) or (height > 600):
        im = crop(image, 2048, 600, width, height)
elif (m1 == 0) and (m2 == 1):
    if (width > 1024) or (height > 1200):
        im = crop(image, 1024, 1200, width, height)
elif (m1 == 1) and (m2 == 1):
    if (width > 2048) or (height > 1200):
        im = crop(image, 2048, 1200, width, height)



if (m1 == 0) and (m2 == 0):
    im2_new = border_man(im, width, height, 1024, 600)
elif (m1 == 1) and (m2 == 0):
    im2_new = border_man(im, width, height, 2048, 600)
elif (m1 == 0) and (m2 == 1):
    im2_new = border_man(im, width, height, 1024, 1200)
elif (m1 == 1) and (m2 == 1):
    im2_new = border_man(im, width, height, 2048, 1200)


cv2.imshow("overall_image_displayed", im2_new)

cv2.waitKey(0)

print (im2_new.shape[:2])

if (m1 == 0) and (m2 == 0):
    (height, width) = im2_new.shape[:2]
    img2 = im2_new
elif (m1 == 1) and (m2 == 0):
    (height, width) = im2_new.shape[:2]
    img2 = im2_new[int (width/2) : width, 0 : height]
elif (m1 == 0) and (m2 == 1):
    (height, width) = im2_new.shape[:2]
    img2 = im2_new[int (height/2) : height, 0 : width]
elif (m1 == 1) and (m2 == 1):
    (height, width) = im2_new.shape[:2]
    print(str(height) + " " + str(width))
    img2 = im2_new[int(height/2) : int(height), int(width/2) : int(width)]
    # img2 = im2_new[int (width/2): int(width), int(height/2) : int(height)]



cv2.imshow("single_display_image_produced", img2)

cv2.waitKey(0)
print (img2.shape[:2])
cv2.destroyAllWindows()
