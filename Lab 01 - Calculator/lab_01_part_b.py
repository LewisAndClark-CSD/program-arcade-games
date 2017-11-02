#!/usr/bin/env python3
# trapazoid area calculator
#Cole Robinson
#11/01/17

h = int(input('Enter the height of the trapazoid: '))
bb = int(input('Enter the length of the bottom base: '))
tb = int(input('Enter the length of the top base: '))
a = (1/2)*(bb + tb)*h
print('The area is: ' + str(a))

