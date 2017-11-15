#!/usr/bin/env python3
# Chapter 6 Lab Part 1
# Jessica Lyles
# 11/15/2017

# Variable for start
start = 10
# Do 9 times starting at 10 (row)
for i in range(9):
    # Loop to print the digits
    for j in range(i + 1):
        print(start, end=' ')
        start += 1
    #print new line
    print()