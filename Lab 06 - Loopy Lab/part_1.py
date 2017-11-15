#!/usr/bin/env python3
# Lab 06 Loopy Lab
# Conner Walkenhorst
# 11/13/2017

"""Lab 06 programs"""

# Starting Value at 10
start = 10

# Do 9 times
for i in range(9):
    # Loop to print digits
    for j in range(i + 1):
        # Prints starting variable and then adds 1 to it.
        print(start, end = ' ')
        start += 1
    # Prints new line
    print()