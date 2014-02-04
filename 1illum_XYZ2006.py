'''
Created on 28 janv. 2014

@author: gary
'''
import pandas as pd
import glob

ofile = file('primary_colorlist.xyz', 'w')

for filename in glob.glob("C:\Users\gary\Documents\eclipse\Light Transformer Setup\RefSpec/*.s"):
    with open(filename) as f:
        #for filename in glob.glob("C:\Users\gary\Documents\eclipse\Light Transformer Setup\Illuminants/*.illum"):
            #with open(filename) as f:

        cmf = pd.read_csv('C:\Users\gary\Documents\eclipse\Light Transformer Setup\data csv\CMF_MA68II.csv', names=['wavelength', 'x', 'y', 'z'])
        
        #here it should be made such as the illuminant depends on x,y position
        ill = pd.read_csv('C:\Users\gary\Documents\eclipse\Light Transformer Setup\data csv\D65_MA68II_10nm.csv', names=['wavelength', 'a', 'b'])

        #here we should get one by one the files *.refspec
        data = pd.read_csv(f, names=['wavelength', 'measurement'])

        lookup = pd.merge(cmf, ill, on='wavelength')
        merged = pd.merge(data, lookup, on='wavelength')

        totals = ((lookup[['x', 'y', 'z']].T*lookup['a']).T).sum()
        wps  = 100 * totals/totals['y']

        #print totals['y']
        #print "D65_CMF_2006_10_deg white point = "
        #print wps

        x = 100 * ((merged.x * merged.a * merged.measurement).sum() / (merged.y * merged.a * 100).sum())    
        y = 100 * ((merged.y * merged.a * merged.measurement).sum() / (merged.y * merged.a * 100).sum())    
        z = 100 * ((merged.z * merged.a * merged.measurement).sum() / (merged.y * merged.a * 100).sum())         
        
        print filename,x, y, z
    
        ofile.write(str(filename) + "," + str(x) + "," + str(y) + "," + str(z) + '\n')
        



    
    
    
    
    