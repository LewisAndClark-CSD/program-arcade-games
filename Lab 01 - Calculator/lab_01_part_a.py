#!/usr/bin/env python3
#Fahrenheit to Celsius conversion
#Ryan Rosvall
#11/1/17

temperature = int(input("Enter temperature in Fahrenheit: "))
conversion = ((temperature - int(32)) * 5/9)
print('The temperature in Celsius: ' + str(conversion))
