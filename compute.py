'''
Created on 30 janv. 2014

@author: gary
'''

imgMax = 57059
imgMin = 7114
Luminance = 18604

#reference XYZ from wallpaper's white (lowest luminance)
Ref_X = 90.1
Ref_Y = 95.1
Ref_Z = 100.1

toDoX = (imgMin*Ref_X)/Luminance
toDoY = (imgMin*Ref_Y)/Luminance
toDoZ = (imgMin*Ref_Z)/Luminance

print toDoX, toDoY, toDoZ