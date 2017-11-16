#!/usr/bin/env python3
# Chapter 6 Lab Part 2
# Jessica Lyles
# 11/15/2017

# User Input for value of n/how many o's (row wise not column)
userInput = int(input('Please enter a value for n: '))
# Variable for spaces between
spaces = (userInput*2) - 2
# Loop to print top line of o's
for i in range(userInput):
    print('o'*2, end = '')
# Print new line
print()
# Loop to print o's between
for row in range(1, userInput - 1):
    print('o' +  (' ' * spaces) + 'o')
# Loop to print bottom line of o's
for j in range(userInput):
    print('o'*2, end = '')

    
    

