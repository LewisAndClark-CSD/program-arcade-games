#!/usr/bin/env python3
#Lab #6
#Christian Groves
#11-15-17

#input for desired size
boxsize = int(input('Desired size: '))
horizontal = boxsize*2
spaces = (boxsize*2) -3
verticle = boxsize-1

#for loop to add the rows of o's
for row in range(1):
    print('o'*horizontal)
#for loop to add the col
for col in range(1,verticle):
    print('o',' '*spaces,end='o\n')
#for loop to add the rows at the end with o's
for row in range(1):
    print('o'*horizontal)    
