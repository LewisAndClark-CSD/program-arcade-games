#!/usr/bin/env python3
#lab_01_part_b.py
#Justin Riebow
#11/2/17

"""Prints area of trapezoid"""

print("Area of a trapezoid")
trapezoidHeight = int(input("Enter the height of the trapezoid: "))
trapezoidBottomLength = int(input("Enter the length of the bottom base: "))
trapezoidTopLength = int(input("Enter the lenght of the top base: "))
trapezoidArea = (0.5 * (trapezoidBottomLength + trapezoidTopLength) * trapezoidHeight)
print("The area is:", (trapezoidArea))
