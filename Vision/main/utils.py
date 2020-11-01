#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 31 23:56:57 2020

@author: nikhilchaudhary
"""
import cv2
import numpy as np
import pytesseract
import string
import matplotlib.pyplot as plt

# For Windows Local Machine - Begins
EXE_PATH = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
pytesseract.pytesseract.tesseract_cmd = EXE_PATH
# Ends

path = r"C:\Users\hp\Desktop\Nikhil Project\nikhil.png"

def get_text_from_image(image_path, remove=False):
    image = cv2.imread(image_path)
    gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    blur=cv2.bilateralFilter(gray,11,90,90)
    edges=cv2.Canny(blur,30,200)
    cnts, new=cv2.findContours(edges.copy(),cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
    image_copy=image.copy()
    _=cv2.drawContours(image_copy,cnts,-1,(255,0,255),2)
    cnts=sorted(cnts,key=cv2.contourArea,reverse=True)[:30]
    image_reduced_cnts=image.copy()
    _=cv2.drawContours(image_reduced_cnts,cnts,-1,(255,0,255),2)
    plate=None
    for c in cnts:
        perimeter=cv2.arcLength(c,True)
        edges_count=cv2.approxPolyDP(c,0.02*perimeter,True)
        if len(edges_count)==4:
            x,y,w,h=cv2.boundingRect(c)
            plate=image[y:y+h,x:x+w]
            break
    text=pytesseract.image_to_string(plate,lang="eng")
    if remove:
        alpha_numerics = string.ascii_lowercase + string.ascii_uppercase + string.digits + " " + "\n"
        return "".join([k for k in text if k in alpha_numerics])
    else:
        return text





