#!/usr/bin/env python3
# Lab 06 Loopy Lab
# Conner Walkenhorst
# 11/13/2017

"""Lab 06 programs"""

#Do 9 times starting at 1 (row)
for row in range(1,10):
    
    #Loop to print spaces
    for space in range(9 - row):
        print(' ', end=' ')
        
    #Loop to print digits
    for digit in range(1, row + 1):
        print(digit,end=' ')
        
    #Loop to print digits2
    for digit2 in range(row - 1,0,-1):
        print(digit2, end=' ')
        
    #print a new line
    print()