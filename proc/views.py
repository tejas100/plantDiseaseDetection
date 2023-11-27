from django.shortcuts import render
from django.http import HttpResponse, request
from django.core.files.storage import FileSystemStorage
import string, random
import numpy as np
import os, io
import re
import matplotlib.pyplot as plt
from django.test import TestCase
import cv2


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MEDIA_ROOT = os.path.join(BASE_DIR)

def index(request):
     if request.method == 'POST':
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        print(name)
        f = fs.url(name)   #Context
        print(f)

        # Start OF Main

        # ----------------- Directories ------------------- 
        letters = string.ascii_lowercase
        str1 = ( ''.join(random.choice(letters) for i in range(5)) )    
        graydir = '/grey'+str1+'.png'                   #Context --Geayscale
        contdir = '/cont'+str1+'.png'                 #Context --Noise
        morphdir = '/morph'+str1+'.png'             #Context --Morph
        mcontdir = '/mcont'+str1+'.png'             #Context --Morph Contrast 
        flatdir = '/flat'+str1+'.png'             #Context --Flat Contrast    
        
    
        # ------------------- Gray scale -----------------------
        originalImage = cv2.imread('/Users/tejasbk/Documents/code/plantDiseaseDetection/plantDiseaseDetection'+f)  #Context
        grayImage = cv2.cvtColor(originalImage, cv2.COLOR_BGR2GRAY)
        # maskout
        (thresh, blackAndWhiteImage) = cv2.threshold(grayImage, 127, 255, cv2.THRESH_BINARY)
        cv2.imwrite('/Users/tejasbk/Documents/code/plantDiseaseDetection/plantDiseaseDetection/media/grey'+graydir,grayImage)


        # -------------------- Contrast Histogram ---------------------
        img = cv2.imread('/Users/tejasbk/Documents/code/plantDiseaseDetection/plantDiseaseDetection/media/grey'+graydir,0)
        # create a CLAHE object (Arguments are optional).
        clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
        cl1 = clahe.apply(img)
        cv2.imwrite('/Users/tejasbk/Documents/code/plantDiseaseDetection/plantDiseaseDetection/media/cont'+contdir,cl1)

        # ------------ Morphological transformation in feature extraction -----------
        img = cv2.imread('/Users/tejasbk/Documents/code/plantDiseaseDetection/plantDiseaseDetection/media/cont'+contdir)

        rect_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (512, 512))
        black_hat_image = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, rect_kernel)
        cv2.imwrite('/Users/tejasbk/Documents/code/plantDiseaseDetection/plantDiseaseDetection/media/morph'+morphdir,black_hat_image)

        # -------------------- Morph Contrast Histogram ---------------------
        img = cv2.imread('/Users/tejasbk/Documents/code/plantDiseaseDetection/plantDiseaseDetection/media/morph'+morphdir,0)
        # create a CLAHE object (Arguments are optional).
        clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
        cl1 = clahe.apply(img)
        cv2.imwrite('/Users/tejasbk/Documents/code/plantDiseaseDetection/plantDiseaseDetection/media/mcont'+mcontdir,cl1)

     return render(request, "index.html")

