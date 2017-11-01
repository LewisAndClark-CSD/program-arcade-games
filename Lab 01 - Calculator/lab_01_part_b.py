#!/usr/bin/env python3
# lab_01_part_b.py
# Jared Rhodes
# 11/01/2017

""" This is the second part of Chapter 1 Lab Pygame """

print("Finding the Area of a Trapezoid")

height = int(input("Enter the height of the trapezoid: "))
base_One = int(input("Enter the length of the bottom base: "))
base_Two = int(input("Enter the length of the top base: "))

area = ((base_One + base_Two) * height) / 2

print('The area is:', area)