#!/usr/bin/env python3
#Space Hopper
#Ethan Dall
#11-2-17

"""You stolen a camel and must fight, nature and man to survive!"""

#Imports

import random

#Accumulators

miles = 0
hunger = 0
fuel = 6
nasa = -20
rations = 4

#Introduction

print('\nWelcome to Space Hopper!\n\nYou have stolen a space ship to make your way across the Milky-Way.\nNASA want their space ship back and are chasing you down!\nSurvive your space trek and out run NASA.\n')

#While choices

done = False
while done == False: #Choices
    
    #most-recent
    
    oasis = random.randint(1, 21)
    nasatra = random.randint(7, 15)
    milestra = random.randint(10, 21)
    
    print('A. Open a bag of rations.\nB. Ahead moderate speed.\nC. Ahead full speed.\nD. Stop for the night.\nE. Status check.\nQ. Quit.')
    user_choice = input('Your choice? ')

    #Quits Game

    if user_choice.upper() == 'Q':
        done = True
    
    #Check Status
    
    elif user_choice.upper() == 'E':
        print('\nMiles traveled: ' + str(miles) + '\nRations left:' + str(rations) + '\nNASA is', str(nasa * -1), 'miles behind you.')
    
    #Stop for the night
    
    elif user_choice.upper() == 'D':
        fuel = 3
        print('\nYou found more fuel!')
        nasa = nasa - (milestra - nasatra)
        
    #Full Speed
        
    elif user_choice.upper() == 'C':
        miles = miles + milestra
        print('\nYou traveled:', str(milestra), 'miles\n')
        hunger += 1
        fuel = fuel - random.randint(1, 4)
        nasa = nasa - (milestra - nasatra)
        
    #Moderate Speed
        
    elif user_choice.upper() == 'B':
        miles = miles + random.randint(5, 13)
        print('\nYou traveled:', str(milestra), 'miles\n')
        hunger += 1
        fuel -= 1
        nasa = nasa - (milestra - nasatra)
        
    #Eat Rations
        
    elif user_choice.upper() == 'A':
        if rations != 0:
            rations -= 1
            hunger = 0
        else:
            print('No rations left!\n')
            
    #Conditons:
    #Hunger
            
    if hunger >= 4:
        print('You are hungry!\n')
    if hunger > 6:
        print('You died of starvation!\n')
        done = True
        
    #Fuel
        
    if -3 < fuel <= 0:
        print('Your running on fumes!\n')
    if  -3 >= fuel:
        print('Your ship ran out of gas\nNASA caught you :(\n')
        done = True
        continue
        
    #NASA
        
    if nasa >= 0:
        print('NASA has caught you!\n')
        done = True
        continue
    elif 0 > nasa >= -15:
        print('NASA is gaining on you!\n')
        
    #Winning
        
    if miles >= 200:
        print('YOU MADE IT ACROSS THE MILKY WAY!!!\n')
        
    #Oasis
    
    oasis = random.randint(1, 21)
    if oasis == 2:
        print('You found the International Space Station!\n')
        hunger = 0
        fuel = 3
        rations = 4
