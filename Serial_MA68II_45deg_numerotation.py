'''
Created on 28 janv. 2014

@author: gary
'''

import serial  # requires pyserial library
import os.path
#import pandas as pd

#save_path = 'RefSpecs'

#rgb_names = pd.read_csv('colornames.txt', names=['number', 'R', 'G', 'B'])


# find a way to command measurements by their names



print "please make sure a previous version of this software isn't still opened to avoid error"
print "if an [ERROR 5] appears under windows, Kill Python.exe and try again"

ser  = serial.Serial(0)

while True:
    name  = raw_input("Pigment name [Q to finish]: ")
    if name == "Q":
        print "bye bye!"
        break
    else:
        ofile = file(str(name) + '.s', 'w')
    
    first = True

    while True:
        line = ser.readline()
        if first:
            print "  Data incoming..."
            first = False
        split = line.split()
        if 10 <= len(split):
            try:
                wavelength = int(split[0])
                ofile.write(str(wavelength) + "," + split[6] + '\n')
                """"http://stackoverflow.com/questions/21419574/python-export-to-file-via-ofile-without-bracket-characters#21419589"""
                
            except ValueError:
                pass    # handles the table heading
        if line[:3] == "110":
            break

    print "  Data gathered."