# -*- coding: utf-8 -*-
"""
Jose Fernández Ortiz
"""


import numpy as np
import cv2
import os

path ='c:\\improc'
os.chdir(path)

im = cv2.imread('lena.jpg')
trans_rows = 180
trans_cols = 60

translation_matrix = np.array([[1,0, trans_cols], [0,1, trans_rows]], 'float32')

rows, cols = im.shape[:2]
rotation_degree = 30
rotation_centre = (cols/2, rows/2)

rotation_matrix = cv2.getRotationMatrix2D(rotation_centre, rotation_degree, 1)
im1 = cv2.warpAffine(im, translation_matrix, (cols+200, rows+200))
im2 = cv2.warpAffine(im1, rotation_matrix, (cols+300, rows+250))
cv2.imshow('lena',im2)
cv2.waitKey()
cv2.destroyAllWindows()