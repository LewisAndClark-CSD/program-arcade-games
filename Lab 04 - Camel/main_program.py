#!/usr/bin/env python3
# Lab 04 Camel
# Conner Walkenhorst
# 11/10/2017

"""the user is running from the natives in the great mobi desert on a stolen camel, the user decides what to do"""

from random import randint
print('Welcome to Camel!')
print('You have stolen a camel to make your way across the great Mobi desert.')
print('The natives want their camel back and are chasing you down! Survive your')
print('desert trek and out run the natives.')
done = False
milesTraveled = 0
thirst = 0
camelTiredness = 0
distanceNativesTraveled = -20
initialDrinks = 5
while done is False:
    print('A. Drink from your canteen.')
    print('B. Ahead moderate speed.')
    print('C. Ahead full speed.')
    print('D. Stop for the night.')
    print('E. Status check.')
    print('Q. Quit.')
    userChoice = input('What will you do? ')
    if userChoice.upper() == 'Q':
        done = True
    elif userChoice.upper() == 'E':
        print('Miles traveled:',milesTraveled)
        print('Drinks in canteen:',initialDrinks)
        print('The natives are ',distanceNativesTraveled,'miles behind you.')
    elif userChoice.upper() == 'D':
        camelTiredness = 0
        print('The camel is happy.')
        distanceNativesTraveled += 7
    elif userChoice.upper() == 'C':
        milesTraveled += randint(10,20)
        print('Miles Traveled:',milesTraveled)
        thirst += 1
        camelTiredness += randint(1,3)
        distanceNativesTraveled += 7
    elif userChoice.upper() == 'B':
        milesTraveled += randint(5,12)
        print('Miles Traveled:',milesTraveled)
        thirst += 1
        camelTiredness += 1
        distanceNativesTraveled += randint(7,14)
    elif userChoice.upper() == 'A':
        if initialDrinks > 0:
            initialDrinks -= 1
            thirst = 0
        else:
            print('Error, no drinks left.')
    if thirst > 4:
        print('You are thirsty.')
    elif thirst > 6:
        print('You died of thirst.')
        done = True
    if camelTiredness > 5:
        print('Your camel is getting tired.')
    elif camelTiredness > 8:
        print('Your camel is dead.')
        done = True
    if distanceNativesTraveled == milesTraveled:
        print('The natives caught you.')
        done = True
    elif distanceNativesTraveled == 15 < milesTraveled:
        print('The natives are getting close.')
    if milesTraveled == 200:
        print('You won.')
        done = True
