#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 14 16:22:00 2020

@author: joelbinu
"""
from PIL import Image

global height
global width

def add_margin(pil_img, top, right, bottom, left, color):
    width, height = pil_img.size
    new_width = width + right + left
    new_height = height + top + bottom
    result = Image.new(pil_img.mode, (new_width, new_height), color)
    result.paste(pil_img, (left, top))
    return result



def border_man(im, width, height, w_width, w_height):
    
    im2_new = add_margin(im, int((w_height - height)/2), int((w_width - width)/2),  int((w_height - height)/2), int((w_width - width)/2), (0, 0, 0))
    
    im2_new.save('/Users/joelbinu/Desktop/ModDisplay /Image repo/overall_image_produced.jpg', quality=95)
    
    print (im2_new.size)
    
    return im2_new

def crop(im, n_width, n_height, width, height):
    im2 = im.crop(((width - n_width)/2, (height - n_height)/2, (n_width + (width - n_width)/2), (n_height + (height - n_height)/2)))
    return im2

im = Image.open("/Users/joelbinu/Desktop/ModDisplay /Image repo/original-image.jpg")

print (im.size)

width, height = im.size


m1 = 1
m2 = 0

if (m1 == 0) and (m2 == 0):
    if (width > 1024) or (height > 600):
        im = crop(im, 1024, 600, width, height)
elif (m1 == 1) and (m2 == 0):
    if (width > 2048) or (height > 600):
        im = crop(im, 2048, 600, width, height)
elif (m1 == 0) and (m2 == 1):
    if (width > 1024) or (height > 1200):
        im = crop(im, 1024, 1200, width, height)
elif (m1 == 1) and (m2 == 1):
    if (width > 2048) or (height > 1200):
        im = crop(im, 2048, 1200, width, height)

width, height = im.size        


if (m1 == 0) and (m2 == 0):
    im2_new = border_man(im, width, height, 1024, 600)
elif (m1 == 1) and (m2 == 0):
    im2_new = border_man(im, width, height, 2048, 600)
elif (m1 == 0) and (m2 == 1):
    im2_new = border_man(im, width, height, 1024, 1200)
elif (m1 == 1) and (m2 == 1):
    im2_new = border_man(im, width, height, 2048, 1200)

if (m1 == 0) and (m2 == 0):
    width, height = img1.size
    img2 = im2_new
elif (m1 == 1) and (m2 == 0):
    width, height = im2_new.size
    img2 = im2_new.crop((width/2, 0, width, height))
elif (m1 == 0) and (m2 == 1):
    width, height = im2_new.size
    img2 = im2_new.crop((0, height/2, width, height))
elif (m1 == 1) and (m2 == 1):
    width, height = im2_new.size
    img2 = im2_new.crop((width/2, height/2, width, height))

img2.save('/Users/joelbinu/Desktop/ModDisplay /Image repo/single-display-image.jpg', quality=95)


