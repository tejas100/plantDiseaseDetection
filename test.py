import numpy as np
import os, io
import re
import matplotlib.pyplot as plt
from django.test import TestCase
import cv2



directory = 'AH'
i = 0
# iterate over files in
# that directory
for filename in os.listdir(directory):
    f = os.path.join(directory, filename)

    # cv2.imwrite('/Users/tejasbk/Documents/code/plantDiseaseDetection/plantDiseaseDetection/EAH/i.jpg',f)
    # checking if it is a file
    # if os.path.isfile(f):
    print(f)
    name = filename
    img = cv2.imread(f,0)
    clahe = cv2.createCLAHE(clipLimit=3.0, tileGridSize=(8,8))
    cl1 = clahe.apply(img)
    print(cl1)
    
    # cv2.imshow()
    cv2.imwrite('/Users/tejasbk/Documents/code/plantDiseaseDetection/plantDiseaseDetection/EAH/'+filename,cl1)
    i = i+1
    if(i == 1):
        break



  # -------------------- Contrast Histogram ---------------------


# img = cv2.imread('/Users/tejasbk/Documents/code/plantDiseaseDetection/plantDiseaseDetection/media/grey'+graydir,0)
# # create a CLAHE object (Arguments are optional).
# clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
# cl1 = clahe.apply(img)
# cv2.imwrite('/Users/tejasbk/Documents/code/plantDiseaseDetection/plantDiseaseDetection/media/cont'+contdir,cl1)
# # ------------ Morphological transformation in feature extraction -----------
# img = cv2.imread('/Users/tejasbk/Documents/code/plantDiseaseDetection/plantDiseaseDetection/media/cont'+contdir)
# rect_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (512, 512))
# black_hat_image = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, rect_kernel)
# cv2.imwrite('/Users/tejasbk/Documents/code/plantDiseaseDetection/plantDiseaseDetection/media/morph'+morphdir,black_hat_image)
# # -------------------- Morph Contrast Histogram ---------------------
# img = cv2.imread('/Users/tejasbk/Documents/code/plantDiseaseDetection/plantDiseaseDetection/media/morph'+morphdir,0)
# # create a CLAHE object (Arguments are optional).
# clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
# cl1 = clahe.apply(img)
# cv2.imwrite('/Users/tejasbk/Documents/code/plantDiseaseDetection/plantDiseaseDetection/media/mcont'+mcontdir,cl1)