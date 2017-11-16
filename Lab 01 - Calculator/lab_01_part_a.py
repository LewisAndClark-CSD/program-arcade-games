#!/usr/bin/env python3
# lab_01_part_a.py
# Jared Rhodes
# 11/01/2017

""" This is the first part of Chapter 1 Lab Pygame """

temp_Fahrenheit = float(input("Enter temperature in Fahrenheit: "))

temp_Celsius = (temp_Fahrenheit - 32) * .5556 

print("The temperature in Celsius:", temp_Celsius)
