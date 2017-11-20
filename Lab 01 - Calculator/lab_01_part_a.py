#!/usr/bin/env python3
#lab_01_part_1.py
#Justin Riebow
#11/2/17

"""Asks the user for temperature in fahrenheit and converts it to celsius"""

fahrenheit = int(input("Enter temperature in Fahrenheit: "))
print("The temperature in Celsius:", (float((fahrenheit - 32) * 5/9))) 
