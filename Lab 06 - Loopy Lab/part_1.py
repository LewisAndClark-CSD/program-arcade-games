#!/usr/bin/env python3
#Lab Part 1
#Bethany DuMontelle
#15 November 2017

#Establish starting number
start = 10

#loops it 9 times
for numbers in range(9):

#adds 1 plus the range when it does down
    for down in range(numbers + 1):
        print( start , end = ' ')
        start += 1

#new print statement at the end
    print()