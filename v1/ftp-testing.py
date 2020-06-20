#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 16:52:29 2020

@author: joelbinu
"""
import ftplib

filename = 'border_adj.py'

ftp = ftplib.FTP('192.168.0.157')

ftp.login("pi", "infinityone")

ftp.cwd('files')

myfile = open('/Users/joelbinu/Desktop/ModDisplay /Code/Cropping /border_adj.py', 'rb')

ftp.storbinary('STOR ' + filename, myfile)


