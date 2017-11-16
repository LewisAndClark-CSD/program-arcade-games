#!/usr/bin/env python3
#Camel Program
#Ryan Rosvall
#11/2/17

import random

milesTraveled = 0
thirst = 0
camelTiredness = 0
nativeDistance = -20
canteenDrinks = 3



print("Welcome to Camel!")
print("You have stolen a camel to make your way across the great Mobi desert.")
print("The naties want their camel back and are chasing you down! Survive your dsesert trek and out rin the natives.")
print()
done = False
while done == False:
    print("A. Drink from your canteen.")
    print("B. Ahead moderate speed.")
    print("C. Ahead full speed.")
    print("D. Stop for the night.")
    print("E. Status check.")
    print("Q. Quit.")
    choice = input("Your choice? ").upper()
    print()
    if thirst >= 6:
        if choice != "A":
            print("You died of thirst!")
            done = True
    elif thirst > 4:
        if choice != "A":
            print("You are thirsty.")
    if camelTiredness > 8:
        if choice != "D":
            print("Your camel is dead.")
            done = True
    elif camelTiredness > 5:
        if choice != "D":
            print("Your camel is getting tired.")
    if nativeDistance > milesTraveled:
        print("The natives caught you.")
        done = True
    if nativeDistance < 15:
        print("The natives are getting close.")
    if milesTraveled == 200:
        print("You won!")
        done = True
    if choice == "Q":
        done = True
    elif choice == "E":
        print("Miles traveled: " + str(milesTraveled))
        print("Drinks in canteen: " + str(canteenDrinks))
        print("The natives are " + str(milesTraveled - nativeDistance) + " miles behind you.")
        print()
    elif choice == "D":
        camelTiredness = 0
        print("Your camel is happy :)")
        print()
    elif choice == "C":
        m = random.randint(10, 20)
        milesTraveled = milesTraveled + m
        print("You traveled " + str(m) + ' miles')
        camelTiredness = camelTiredness + random.randint(1, 3)
        thirst = thirst + 1
        n = random.randint(7, 14)
        nativeDistance = nativeDistance + n
        print('The natives moved ' + str(n) + ' miles')
        print()
    elif choice == "B":
        m = random.randint(5, 12)
        milesTraveled = milesTraveled + m
        print("You traveled " + str(m) + " miles.")
        thirst = thirst + 1
        camelTiredness = camelTiredness + 1
        n = random.randint(5, 8)
        nativeDistance = nativeDistance + n
        print('The natives moved ' + str(n) + ' miles')

        print()
    elif choice == "A":
        if canteenDrinks > 0:
            canteenDrinks = canteenDrinks - 1
            thirst = 0
        else:
            print("You cannot drink from your canteen because it is empty.")
        
