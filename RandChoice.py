'''
Created on 30 janv. 2014

@author: gary
'''
import random

a = .1
b = .3
c = .1
d = 1-a-b-c


R = random.uniform(0, 1)

print R

if R <= a:
    print "a"

elif R <= a+b:
    print "b"
    
elif R <= a+b+c:
    print "c"
    
else:
    print "d"