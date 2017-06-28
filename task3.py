# -*- coding: utf-8 -*-
"""
Jose Fernández Ortiz
"""


import numpy as np

import cv2
import os


def myrotate(im, rotation_degree, rotation_centre):
    rows, cols = im.shape[:2]
    rotation_matrix = cv2.getRotationMatrix2D(rotation_centre, rotation_degree, 1)
    p = np.array([[0, cols-1, cols-1, 0],[0, 0, rows-1, rows-1],[1,1,1,1,]])
    #Calculate where the corner points are after the translation
    p2 = np.dot(rotation_matrix, p).astype(int)
    minx = np.min(p2[0,:])
    maxx = np.max(p2[0,:])
    miny = np.min(p2[1,:])
    maxy = np.max(p2[1,:])
    #tranaslate the original image before rotation
    translation_matrix = np.array([[1,0,-minx],[0,1,-miny]], 'float32')
    im2 = cv2.warpAffine(im, translation_matrix, (-minx+cols, -miny+rows))
    #calculate the centre of roaton in the new translated image
    rotation_centre2 = np.array([rotation_centre[0], rotation_centre[1], 1])
    rotation_centre2 = np.dot(translation_matrix, rotation_centre2).astype(int)
    #calculate the rotation matrix in new translated image
    rotation_matrix2 = cv2.getRotationMatrix2D(tuple(rotation_centre2), rotation_degree, 1)
    im3 = cv2.warpAffine(im2, rotation_matrix2, (maxx-minx, maxy-miny))
    return im3
path ='c:\\improc'
os.chdir(path)

im = cv2.imread('edin_castle.png')

rotation_degree = 60
rotation_centre = (50, 70)
im2 = myrotate (im, rotation_degree, rotation_centre)

#cv2.imshow('image original',im)

cv2.imshow('image translated',im2)

cv2.waitKey()
cv2.destroyAllWindows()