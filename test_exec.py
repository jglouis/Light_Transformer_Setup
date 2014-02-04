'''
Created on 30 janv. 2014

@author: gary
'''
print "a file named MAP.tif should be in the folder"

import objects

x=0
y=0
img=raw_input('MAP.tif')

lumi_map = objects.Lumi()

for x in range(x, x+1):
    for y in range(y, y+1):
        
        lumi_map.Lumi(img, x, y)

"""je ne comprends pas pourquoi cela ne fonctionne pas"""