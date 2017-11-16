#!/usr/bin/env python3
#part_2.py
#Justin Riebow
#11/16/17

"""Creates a box made of o's"""

#Make an input for the number of o's in a row
row = int(input("Enter number: "))
#Draws top line
for toprow in range(row*2):
    print("o", end="")
print()
#Draws side
for side in range(row-2):
    print("o", (row-2) * "  ", "o")
#Draws bottom line
for bottomrow in range(row*2):
    print("o", end="")
print ()
