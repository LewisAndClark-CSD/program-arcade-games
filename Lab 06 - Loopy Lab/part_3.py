#!/usr/bin/env python3
#part_3.py
#Ethan Dall
#11-15-17

"""Take the users input and print a indented diamond"""

#User Input
size = int(input('Choose an even number: '))

#Size for f(x)
for x in range(1,size*2, 2):
    
    #loop for digit
    for odds in range(1):
        print(x, end=' ')
    
    #print new line