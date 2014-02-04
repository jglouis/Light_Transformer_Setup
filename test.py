import cv2



S = cv2.imread("MAP.tif", -1)

height, width = S.shape
min_luminance = S.min()

print "min luminance is: " + str(min_luminance)

for x in range(width):
    for y in range(height):
        luminance = S[x,y]
        
        
        

        
        #toDoX = (imgMin*Ref_X)/Luminance
        #toDoY = (imgMin*Ref_Y)/Luminance
        #toDoZ = (imgMin*Ref_Z)/Luminance
        
        
     

        
        
        
        
        
        
        
        

