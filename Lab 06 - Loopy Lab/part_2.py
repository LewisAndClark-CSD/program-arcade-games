#!/usr/bin/env python 3
# Lab 6 part 1
# Grant Headrick
# 11-15-17
number = int(input("How many o's: "))
spaces = (number * 2) -2
print("o" * ((number) * 2))
for i in range(1, number - 1):
    print("o" + (' ' * spaces) + "o")
print("o" * ((number) * 2))
