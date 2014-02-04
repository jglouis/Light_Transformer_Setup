'''
Created on 28 janv. 2014

@author: gary
'''
import pandas as pd

ofile = file('primary_colorlist.xyz', 'w')



#def MakeXYZ(self):


with open('measurementsMA68II.csv') as f:
    
    data = pd.read_csv(f, names=['name', 'wavelength', 'measurement'])
    
    print data
    
#     # for filename in glob.glob("C:\Users\gary\Documents\eclipse\Light Transformer Setup\Illuminants/*.illum"):
#         # with open(filename) as f:
#     
#     cmf = pd.read_csv('C:\Users\gary\Documents\eclipse\Light Transformer Setup\data csv\CMF_MA68II.csv', names=['wavelength', 'x', 'y', 'z'])
#     
#     # loads illuminant file
#     ill = pd.read_csv('C:\Users\gary\Documents\eclipse\Light Transformer Setup\data csv\D65_MA68II_10nm.csv', names=['wavelength', 'a', 'b'])
#     
#     # here we should get one by one the files *.refspec
#     data = pd.read_csv(f, names=['name', 'wavelength', 'measurement'])
#     
#     lookup = pd.merge(cmf, ill, on='wavelength')
#     merged = pd.merge(data, lookup, on='wavelength')
#     
#     totals = ((lookup[['x', 'y', 'z']].T * lookup['a']).T).sum()
#     #wps = 100 * totals / totals['y']
#     
#     # print totals['y']
#     # print "D65_CMF_2006_10_deg white point = "
#     # print wps
    
#     x = 100 * ((merged.x * merged.a * merged.measurement).sum() / (merged.y * merged.a * 100).sum())    
#     y = 100 * ((merged.y * merged.a * merged.measurement).sum() / (merged.y * merged.a * 100).sum())    
#     z = 100 * ((merged.z * merged.a * merged.measurement).sum() / (merged.y * merged.a * 100).sum())         
#     
#     print f, x, y, z
#     
#     ofile.write(str(f) + "," + str(x) + "," + str(y) + "," + str(z) + '\n')
#     








