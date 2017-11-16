#!/usr/bin/env python3
#part_1.py
#Justin Riebow
#11/15/17

"""Prints out numbers in a certain order"""

i = 10
for row in range(1, 10):
    for column in range(row):
        print(i,end=" ")
        i += 1
    print()
