"""
Jose Fernández Ortiz
"""
import numpy as np
import cv2
import os

path ='c:\\improc'
os.chdir(path)

im = cv2.imread('lena.jpg')

rows, cols = im.shape[:2]
trans_rows = 50
trans_cols = 50

new_rows = rows + trans_rows +50
new_cols = cols + trans_cols +50
sfx = 2.0 #Scaling factor for width
sfy = 2.0 # scalin factor for height
im_nearest = cv2.resize (im, None, fx = sfx, fy= sfy, interpolation = cv2.INTER_CUBIC)

translation_matrix = np.array([[1,0, trans_cols], [0,1, trans_rows]], 'float32')

im2 = cv2.warpAffine(im, translation_matrix, (new_cols, new_rows))
#cv2.imshow('Nearest',im_nearest)

cv2.imshow('lena', im2)




cv2.waitKey()
cv2.destroyAllWindows()