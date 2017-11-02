#!/usr/bin/env python3
# Finding the area of a trapezoid
# Evan Witterholt
#11/2/2017
height = int(input("Enter the height of the trapezoid: "))
length = int(input("Enter the length of the bottom base: "))
length2= int(input("Enter the length of the top base : "))
part1 = length + length2
part2 = height * part1 * 0.5
print(part2)
