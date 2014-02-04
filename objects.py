'''
Created on 29 janv. 2014

@author: gary

'''
#libraries




## OPTIONAL
class RGBcolor(object):
    def __init__(self, name, R, G, B):
        """defines the name and color of a pixel to be printed"""
## OPTIONAL >> can be a list in a .csv file


class Reflectance(object):
    def __init__(self, name, spec_A, spec_B, spec_C, spec_D, spec_E):
        """reflectance specter of a printed RGB_color, spec_C for 45/0 geometry
        Using a spectrophotometer X-Rite MA-68 II"""
# CAN BE SIMPLIFIED >> using only spec_C
        
        
class Illuminant(object):
    def __init__(self, name, x, y, spec):
        """emission specter of an Illuminant"""


class Lumi(object):
    
    def __init__(self, img, x, y):
        import cv2
        self.img = cv2.imread(img, -1) # load as-is: this allows for 16-bit images to import correctly
        self.x = x
        self.y = y
        print cv2[x,y]   


class BilinearInterpolation(object):
    def __init__(self, Illuminant):
        """computes a normalized bilinear interpolation of illuminant values with position x, y"""
    
      
class ColorList(object):
    def __init__(self, *args, **kwargs):
        """computes a list of XYZ values using RGB names, Reflectance, Luminance L and the interpolated illuminant
        for each object Illuminant"""


## OPTIONAL
class DelaunayCleaner(object):
    def __init__(self, color_list):
        """removes unnecessary ("non-primary") colors from colorlists"""  
    #return ColorList
## OPTIONAL


class RandColors(object):
    def __init__(self, ColorList):
        """randomly chooses 4 colors in ColorList"""
    #return RGBname_1, RGBname_2, RGBname_3, RGBname_4


class SolverXYZ(object):
    def __init__(self):
        """determines the characteristics of the color layer to be printed at one x, y position"""
 
        
class LocalSolution(object):
    def __init__(self, RandColors):
        """tries to match the needed colorimetric result using RandColors"""
    #if true:
        #return D_1, D_2, D_3, D_4
    #else:
        #iterate RandColors
 
        
class RandChoice(object):
    def __init__(self, LocalSolution):
        """generates a uniform random floating number and associates it with one LocalSolution"""
        
        
class PBMgen(object):
    def __init__(self, LocalSolution):
        """generates a bitmap with RandChoice"""
    