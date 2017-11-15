#!/usr/bin/env python3
# Lab 06 Loopy Lab
# Conner Walkenhorst
# 11/13/2017

"""Lab 06 programs"""

#Do 9 times starting at 1 (row)
for row in range(1,10):
    
    #Loop to print multiples
    for i in range(1,10):
        print(repr(row*i).rjust(2),end=' ')
    #print a new line
    print()