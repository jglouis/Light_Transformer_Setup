'''
Created on 28 janv. 2014

@author: gary
'''

import serial  # requires pyserial library

print "please make sure a previous version of this software isn't still opened to avoid error"
print "if an [ERROR 5] appears under windows, Kill Python.exe and try again"

ser  = serial.Serial(0)

number = 1

while True:

    name  = number
    
    ofile = file(str(name) + '.s', 'w')
    print "measure now..." + "num: " + str(name)
    
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
    number = number + 1
    
    print "PRESS ENTER TO CONTINUE. Q + ENTER TO QUIT" + "\n"
    wait = raw_input()
    if wait == "Q":
        ofile.close()
        print "bye bye!"
        break
    
    