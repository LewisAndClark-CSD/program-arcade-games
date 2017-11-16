#!/usr/bin/env python3
# Lab 06 Loopy Lab
# Conner Walkenhorst
# 11/15/2017

"""Lab 06 part 2"""

#input for user to say how many o's to print
numberOs = int(input("How many o's do you want? "))
spaces = ((numberOs*2) - 2)
#loop for o's on top corresponding to user's input
for i in range(numberOs):
    print('o'*2, end = '')
print()
#loop for o's on left side corresponding to user's input
for j in range(1, numberOs - 1):
    print('o' + (' ' * spaces) +'o')
#loop for o's on bottom corresponding to user's input
for row in range(numberOs):
    print('o'*2, end = '')