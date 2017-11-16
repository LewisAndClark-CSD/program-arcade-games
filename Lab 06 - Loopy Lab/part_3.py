#!/usr/bin/env python3
#Lab #6
#Christian Groves
#11-15-17
size = int(input('Size: '))


for row in range(1,10):
    for digit1 in range(9 - row):
        print(digit1, end=' ')
    for spaces in range(1,row +1):
        print(' ',end=' ')
    for digit2 in range(row,0,-1):
        print(digit2,end=' ')    
    print()
for botrow in range (9,0,-1):
    for spacesbot in range(9- botrow, 0, -1):
        print(' ',end=' ')
    for digit3 in range(1, botrow+1):
        print(digit3,end=' ')
    for digit4 in range(botrow,0,-1):
        print(digit4,end=' ')      
    print()