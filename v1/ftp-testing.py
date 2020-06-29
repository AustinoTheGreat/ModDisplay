#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 16:52:29 2020

@author: joelbinu
"""
import ftplib

filename = 'single-display-image.jpg'

ftp = ftplib.FTP('192.168.0.157')

ftp.login("pi", "password")

ftp.cwd('files')

myfile = open('/Users/joelbinu/Desktop/ModDisplay /Image repo/Produced_images/single-display-image.jpg', 'rb')

ftp.storbinary('STOR ' + filename, myfile)



