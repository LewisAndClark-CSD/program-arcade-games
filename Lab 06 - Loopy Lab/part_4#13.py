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
    
#Do 8 times starting at 8 down to 1
for row2 in range(8,0,-1):

    #Loop to print spaces
    for space in range(9 - row2):
        print(' ',end=' ')
        
    #Loop to print digits3
    for digit3 in range(1,row2 + 1):
        print(digit3,end=' ')
        
    #Loop to print digits3
    for digit4 in range(row2 - 1, 0, -1):
        print(digit4,end=' ')
    
    #print new line
    print()