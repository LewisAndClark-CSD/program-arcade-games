#!/usr/bin/env python
# 6.2 Part 1
# Asia Robinson
# 11/16/2017

startnumber = 10

for row in range(1,10):
    for col in range(row):
        print(startnumber,end=" ")
        startnumber += 1
    print()
