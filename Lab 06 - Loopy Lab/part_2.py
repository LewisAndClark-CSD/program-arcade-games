#!/usr/bin/env python3
# part_2.py
# Ryan Moore
# 11/15/2017

#user input 
numbero = int(input("E.g. n = "))
#increase user input
number = numbero*2
for row in range(number - 1):
    #print o's
    print("o", end="")
#for the left side
for column in range(numbero - 1):
    print("o")
    #for the right side
#for the bottom row
for row in range(number):
    print("o", end="")
