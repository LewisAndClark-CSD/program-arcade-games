#!/usr/bin/env python3
#Converting Fahrenheit to Celcius
#Ethan Dall
#11-1-17

"""Converting Fahrenheit to Celcuis"""

#Letting the User Define the Temperature

tempF = int(input('Enter temperature in Fahrenheit: '))

#Using the conversion forumula for Fahrenheit to Celcuis

tempC = (tempF - 32) * (5/9)

#print to console

print('The temperature in Celsius: ', tempC)
