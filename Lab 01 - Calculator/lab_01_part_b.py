#!/usr/bin/env python
# 1.2 Part B
# Asia Robinson
# 11/2/2017

print("Area of a trapezoid")
trapazoid_height_int = int(input("Enter the height of the trapezoid: "))
trapazoid_length_bottom_int = int(input("Enter the length of the bottom base: "))
trapazoid_length_top_int = int(input("Enter the length of the top base: "))

trapazoid_area_int = ( .5 * (trapazoid_length_bottom_int + trapazoid_length_top_int) * trapazoid_height_int)

print('The area is:', trapazoid_area_int)
