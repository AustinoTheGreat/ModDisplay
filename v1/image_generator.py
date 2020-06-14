#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 14 17:01:45 2020

@author: joelbinu
"""
from PIL import Image


im = Image.open("/Users/joelbinu/Desktop/ModDisplay /Image repo/download2.jpg")
image2 = im.resize((2048,600))
image2.save('/Users/joelbinu/Desktop/ModDisplay /Image repo/image_produce1.jpg', quality=95)
