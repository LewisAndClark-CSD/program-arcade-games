#!/usr/bin/env python3
# 1.2 Part B
# Conner Walkenhorst
# 11/2/2017
"""ask user for information needed to find area of trapazoid, then print area"""

print('Area of a trapezoid')
height = int(input('Enter the height of the trapezoid: '))
lenght_bottom = int(input('Enter the length of the bottom base: '))
lenght_top = int(input('Enter the length of the top base: '))
area1 = (lenght_bottom + lenght_top)
area2 = (0.5*area1*height)
print('The area is:',area2)
