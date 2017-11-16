#!/usr/bin/env python3
#part_3.py
#Jared Rhodes
#November 5, 2017

""" Part 3 of Chapter 6 Loopy Lab """

size = int(input("What size shape would you like? "))

top_Number = 0
diget = 1
line_List = []

top_Number = size * 2

for row in range(size):
    print()
    for col in range(1 + (2 * row), top_Number + 1, 2):
        print(col,end=" ")
    print("    " * row,end="")
    for col2 in range(top_Number - 1, 0 + (2 * row), -2):
        print(col2,end=" ")        
   
    
for row2 in range(size, -1, -1):
    for col in range(1 + (2 * row2), top_Number + 1, 2):
        print(col,end=" ")
    print("    " * row2,end="")
    for col2 in range(top_Number - 1, 0 + (2 * row2), -2):
        print(col2,end=" ")    
    print()