#!/usr/bin/env python3
#part_1.py
#Jared Rhodes
#November 5, 2017

""" Part 1 of Chapter 6 Loopy Lab """

diget = 10

for row in range(1,10):
    for col in range(row):
        print(diget,end=" ")
        diget += 1
    print()