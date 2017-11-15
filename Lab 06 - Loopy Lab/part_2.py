#!/usr/bin/env python3
# part_2 of chapter 6 Lab
# Brady Ballmann
# 11/15/2017

# Input statement for the o's
numberos = int(input("How many o's do you want? "))
 
number = numberos * 2
# Loop for the top of the box
for row in range(number -1 ):
    print("o",end="")
    # Loop to print the sides
for column in range(numberos):
    print("o")
    


