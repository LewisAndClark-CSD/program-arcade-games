#!/usr/bin/env python3
#part_2.py
#Jared Rhodes
#November 5, 2017

""" Part 2 of Chapter 6 Loopy Lab """

size = int(input("What size box would you like? "))


for width_Top in range(size * 2):
    print("o",end="")
print()

for height in range(size - 2):
    print("o" + (" " * (size * 2 - 2)) + "o")
    
for width_Bottom in range(size * 2):
    print("o",end="")
print()

#This is how to make real boxes!

"""

size = int(input("What size box would you like? "))


for width_Top in range(size * 2):
    print("▀",end="")
print()

for height in range(size - 2):
    print("█" + (" " * (size * 2 - 2)) + "█")
    
for width_Bottom in range(size * 2):
    print("▄",end="")
print()

"""