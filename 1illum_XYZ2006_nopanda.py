'''
Created on 28 janv. 2014

@author: gary
'''
import csv


f = open('measurementsMA68II.csv')
reader = csv.reader(f, delimiter = ',')
spect_data = dict()

for row in reader:
    if not row[0] in spect_data:
        spect_data[row[0]] = dict()
    spect_data[row[0]][row[1]] = row[2]
        

#print spect_data['1']['400']

f = open('CMF_MA68II.csv')
reader = csv.reader(f, delimiter = ',')
cmf = dict()
    
for row in reader:
    cmf[row[0]] = {'x_bar':row[1], 'y_bar':row[2], 'z_bar':row[3]}
    """ voir s'il y a moyen d'importer des floats avec le module csv"""



f = open('D65.csv')
reader = csv.reader(f, delimiter = ',')
illuminant = dict()
    
for row in reader:
    illuminant[row[0]] = row[1]

norm_Y = 0


for wavelength in illuminant.keys():
    norm_Y = norm_Y + float(cmf[wavelength]['y_bar']) * float(illuminant[wavelength])
    
print "norm_Y = " + str(norm_Y)

XYZ = dict()

for spectrum in spect_data.keys():
    X = 0
    Y = 0
    Z = 0
    
    for wavelength in spect_data[spectrum].keys():
        
        X += float(cmf[wavelength]['x_bar']) * float(illuminant[wavelength]) * float(spect_data[spectrum][wavelength])
        Y += float(cmf[wavelength]['y_bar']) * float(illuminant[wavelength]) * float(spect_data[spectrum][wavelength])
        Z += float(cmf[wavelength]['z_bar']) * float(illuminant[wavelength]) * float(spect_data[spectrum][wavelength])
        
    XYZ[spectrum] = {'X': X/norm_Y, 'Y': Y/norm_Y, 'Z': Z/norm_Y}

ofile = file('XYZcolorlist.csv', 'w')

for spectrum in XYZ.keys():
    ofile.write(str(spectrum) + ',' + str(XYZ[spectrum]['X']) + ',' + str(XYZ[spectrum]['Y']) + ',' + str(XYZ[spectrum]['Z']) + '\n')
