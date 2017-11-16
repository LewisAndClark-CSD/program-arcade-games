#!/usr/bin/env python
# 6.2 Part 2
# Asia Robinson
# 11/15/2017

number = int(input("enter number of o: "))
for row in range(number):
    for column in range(2*number):
        print('o' if row in(0,number-1) or column in(0,(2*number)-1) else ' ', end=' ')
    print()
