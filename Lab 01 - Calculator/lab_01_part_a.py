#
#!/usr/bin/env python3
 +#Converting Fahrenheit to Celcius
 +#Jordan Watt
 +#11-2-17
 +
 +"""Converting Fahrenheit to Celcuis"""
 +
 +#Letting the User Define the Temperature
 +
 +tempF = int(input('Enter temperature in Fahrenheit: '))
 +
 +#Using the conversion forumula for Fahrenheit to Celcuis
 +
 +tempC = (tempF - 32) * (5/9)
 +
 +#print to console
 +
 +print('The temperature in Celsius: ', tempC)
