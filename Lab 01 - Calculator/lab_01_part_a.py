#!/usr/bin/env python3
# 1.1 Part A
# Conner Walkenhorst
# 11/2/2017
"""ask the user for a temperature in Fahrenheit, then print the temperature in Celsius"""

temperature = int(input('Enter a temperature in Fehrenheit: '))
celsius = ((temperature - 32)/1.8)
print(celsius)
