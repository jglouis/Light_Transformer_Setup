'''
Created on 30 janv. 2014

@author: gary
'''

import cv2
#load all .xyz files struct: x, y, colors(X,Y,Z)
# for each color needed

img = cv2.imread("MAP.tif", -1) # load as-is: this allows for 16-bit images to import correctly
height, width = img.shape





XYZ=(y*width-x*y)*D+x*y*C+(x*height-x*y)*B+(A*width-x*A)*height-y*A*width+x*y*A

print XYZ