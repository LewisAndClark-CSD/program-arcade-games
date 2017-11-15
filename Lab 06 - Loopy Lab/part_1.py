#!/usr/bin/env python3
# part_1.py
# Ryan Moore
# 11/15/2017
start = 10
#loop 9 times 
for row in range(9):
#increase by one,two,three etc each time you go do     
     for column in range(row+1):
          print(start ,end=" ")
          start += 1            
     #print new line
     print()