#!/usr/bin/env python3
#Trapezoid Area Calculator
#Ryan Rosvall
#11/1/17

print('Area of a trapezoid')
height = int(input('Enter the height of the trapezoid: '))
lengthBottom = int(input('Enter the length of the bottom base'))
lengthTop = int(input('Enter the length of the top base: '))
calculation = (1/2) * (lengthBottom + lengthTop) * height
print('The area is: ' + str(calculation))
