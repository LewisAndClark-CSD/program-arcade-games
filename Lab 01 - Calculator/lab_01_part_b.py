#!/usr/bin/env python3
#Trapezoid Area
#Ethan Dall
#11-1-17

"""Using the Height and length of the top & bottom base of the Trapezoid we can find the area"""

#Title

print('Area of a trapezoid')

#define height, and length of Top & Bottom

height = int(input('Enter the height of the trapezoid: '))
botLength = int(input('Enter the length of the bottom base: '))
topLength = int(input('Enter the length of the top base: '))

#Formula

area = .5*(topLength + botLength)*height

#print

print('The area is:',area)
