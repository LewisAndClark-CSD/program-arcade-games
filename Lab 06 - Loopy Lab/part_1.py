#!/usr/bin/env python3
#Lab #6
#Christian Groves
#11-15-17

#for loop to add 
num = 10
for row in range(1,10):
    for col in range(row,0,-1):
        print(num,end=' ')
        num += 1
    print()
