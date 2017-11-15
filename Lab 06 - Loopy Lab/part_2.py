#!/usr/bin/env python3
# part_2 of chapter 6 Lab
# Brady Ballmann
# 11/15/2017

# Input statement for the o's
numberos = int(input("How many o's do you want? "))
 

# Print for the top of the box
print('o'*(numberos*2 ))
# Loop for the spaces 
for i in range(numberos -2):
     print("o" + ' '*(numberos*2 -2 ) + 'o')
# Print the bottom o's
print('o'*(numberos*2))

