#!/usr/bin/env python3
# part_2.py
# Ryan Moore
# 11/15/2017

#user input 
height = int(input("E.g. n = "))
#top row
print("o"*(height*2))
#columns
for i in range(height- 2):
    print("o" + ' '*(height*2-2) +'o')
#bottom 
print("o"*(height*2))