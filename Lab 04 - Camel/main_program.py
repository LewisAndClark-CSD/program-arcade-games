#!/usr/bin/env python3
#main_program.py
#Justin Riebow
#11/3/17

"""bring your car far away enough from the cops to escape before they catch you"""

import random
done = False
userMiles = 0
copMiles = 0
fuel = 8
thirst = 5
money = 3

print("Welcome to Drive!\nYou have stolen a car to make your way to California.\nThe cops found out and are chasing you down!\nSurvive your road trek and outrun the cops.")
while done == False:
    print("A. Grab a drink at the gas station.\nB. Ahead moderate speed.\nC. Ahead full speed\nD. Stop and fuel up\nE. Status check.")
    choice = input("Your choice?: ")
    if choice.lower() == "q":
        done = True
    if choice.lower() == "a":
        money = money - 1
        thirst = 5
        copMiles = copMiles + random.randint(10, 20)
        print("You take a drink.\nYou have enough money for", str(money), "more drinks.")
    elif choice.lower() == "b":
        userMiles = userMiles + random.randint(7,14)
        fuel = fuel - 1
        copMiles = copMiles + random.randint(3, 11)
        thirst = thirst - 1
        if thirst == 2:
            print("You are thirsty.")
        if thirst == 0:
            done = True
            print("You fainted frmo dehydration.")
        print("You travel at moderate speed.")
        if copMiles >= userMiles - 20:
            print("The cops are getting close!")
        if copMiles >= userMiles:
            print("The cops caught you!")
            done = True
        if fuel <= 2:
            print("You are almost out of fuel!")
        if fuel <= 0:
            print("You ran out of fuel!")
    elif choice.lower() == "c":
        userMiles = userMiles + random.randint(15, 22)
        fuel = fuel - 2
        copMiles = copMiles + random.randint(5, 12)
        thirst = thirst - 1
        if thirst == 2:
            print("You are thirsty.")
        if thirst == 0:
            done = True
            print("You fainted from dehydration.")
            print("You floor it ahead!")
        if copMiles >= userMiles - 20:
            print("The cops are getting close!")
        if copMiles >= userMiles:
            print("The cops caught you!")
            done = True
        if fuel <= 3:
            print("You are almost out of fuel!")
        if fuel <= 0:
            print("You ran out of fuel!")
            done = True
    elif choice.lower() == "d":
        fuel = 8
        copMiles = copMiles + random.randint(10, 20)
        print("You fuel up at a gas station")
    elif choice.lower() == "e":
        print("Miles traveled:", str(userMiles))
        print("How many more meals you have enough money for:", str(money))
        if thirst >= 4:
            print("You are not thirsty.")
        if thirst == 3:
            print("You are slightly thirsty.")
        if thirst == 2:
            print("You are thirsty.")
        if thirst == 1:
            print("You need to drink something ASAP.")
    if userMiles >= 200:
        copMiles == copMiles - 200
        done = True
        print("Congratulations! You escaped the cops!")

    

    
