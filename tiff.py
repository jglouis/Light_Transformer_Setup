'''
Created on 29 janv. 2014

@author: gary
'''
import cv2

def imageprops(path):
    #name = raw_input("Image name[.tiff or .tif]: ")
    img = cv2.imread(path, -1) # load as-is: this allows for 16-bit images to import correctly
    #dir(img)

    height, width = img.shape

    imgMax = img.max()
    imgMin = img.min()

    return {"LumMax": imgMax, "LumMin": imgMin, "Width": width, "Height": height}

def Luminance(path, x, y):
    
    img = cv2.imread(path, -1) # load as-is: this allows for 16-bit images to import correctly
    return {"Luminance": img[x,y]}

if __name__ == '__main__':
    props = imageprops("MAP.tif")
    print props
    print "width is", props["Width"]
    print "keys are", props.keys()