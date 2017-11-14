#!/usr/bin/env python3
# Loops
# Brady Ballmann
# 11/13/2017

# Do 9 times starting at 1
for row in range(1, 10):
    # Loop to print spaces
    for space in range(9 - row):
        print(" ", end=" ")
    # Loop to print digits 
    for digits in range(1, row + 1):
        print(digits, end=" ")
    # Loop to print digits2
    for digits2 in range(row -1, 0, -1):
        print(digits2, end=" ")
    # Print a new line
    print()
for row in range(10):
    # Print spaces Loop
    for space in range(row+1):
        print(" ", end=" ")
    # Loop to print digits
    for digits in range(1,9-row):
        print(digits, end=" ")
    # Loop to print digits2
    for digits2 in range(7-row,0,-1):
        print(digits2,end=" ")
    # Print new line
    print()