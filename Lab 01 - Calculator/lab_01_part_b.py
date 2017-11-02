#!/usr/bin/env python3
# Calculator part a
# Christian Groves
# 11-1-17
print('Area of a trapezoid')
height = int(input('Enter the height of the trapezoid: '))
bottombase = int(input('Enter the length of the botom base: '))
topbase = int(input('Enter the length of the top base: '))
print('The area is: ' + str((1/2)*(bottombase + topbase) * height))