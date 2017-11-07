#!/usr/bin/env python3
#Lab 4 chapter 4 Camel
#Bethany DuMontelle
#3 November 2017

from random import randint

#sets up the variables needed
miles_left = 0
natives_range = -20
user_thirst = 0
canteen = 3
camel_rest = 0
done = False

#Introduces the player
print('Welcome to Camel!')
print('You have stolen a camel to make your way across the Great Mobi desert.')
print('The natives want their camel back and are chasing you down! Survive')
print('your desert trek and out run the natives.')

#begins the loop
while done != True:
    #tells the player how close they are, stops negative numbers from showing
    native_close = (miles_left) - (natives_range)
    
    #sets up if an oasis can be found every time the loop starts over
    oasis = randint(1,15) 
        
    #tells the player important information
    print('You have traveled', str(miles_left), 'miles.')
    
    if native_close < 15:
        print('The natives getting close!')
    else:
        print('The Natives are', str(native_close), 'miles away from you.')
        
    print('You have', str(canteen), 'drinks left in your canteen.')
    
    if user_thirst >= 4:
        print('You are thirsty!')
        
    if camel_rest >= 5:
        print('The camel is getting tired!')
        
    
    print('What would you like to do?')
    print('A. Drink from your canteen')
    print('B. Ahead moderate speed.')
    print('C. Ahead full speed.')
    print('D. Stop for the night.')
    print('E. Status check.')
    print('Q. Quit')
    
    user_choice = input()
    
    #allows the player to drink from their canteen
    #also prevents players from drinking water they don't have
    if user_choice.lower() == 'a':
        if canteen <= 0:
            print('You don\'t have any more water!')
        else:
            user_thirst = user_thirst - 1
            canteen = canteen - 1
        
    #moves the player, also can find an oasis if the random number was 1
    elif user_choice.lower() == 'b':
        miles_move = randint(5,12)
        miles_left = (miles_left) + (miles_move)
        natives_move = randint(7,14)
        natives_range = (natives_range) + (natives_move)
        camel_rest = (camel_rest) + 1
        user_thirst = user_thirst + 1
        print('You moved', + (miles_move), 'miles.')
        if oasis == 1:
            canteen_fill = randint(2,5)
            canteen = (canteen) + (canteen_fill)
            user_thirst = user_thirst + 2
            print('You found an oasis!')
            print('You can now drink', (canteen_fill), 'more times.')        
    
    #also moves the player, but with more random elements and an oasis can
    #be found as well
    elif user_choice.lower() == 'c':
        miles_move = randint(10,20)
        miles_left = (miles_left) + (miles_move)
        natives_move = randint(7,14)
        natives_range = (natives_range) + (natives_move)
        camel_tired = randint(1,3)
        camel_rest = (camel_rest) + (camel_tired)
        user_thirst = user_thirst + 1
        print('You moved', + (miles_move), 'miles.')
        if oasis == 1:
            canteen_fill = randint(2,5)
            canteen = (canteen) + (canteen_fill)
            user_thirst = user_thirst + 2
            print('You found an oasis!')
            print('You can now drink', (canteen_fill), 'more times.')        
        
    #sets camel_rest to 0, moves the natives up as well
    elif user_choice.lower() == 'd':
        camel_rest = 0
        natives_move = randint(7,14)
        natives_range = (natives_range) + (natives_move)
        print('The camel is happy.')
    
    #gives the player more stats
    elif user_choice.lower() == 'e':
        print('Miles left:', 200 - (miles_left))
        print('Native distance:', (native_close))
        print('Canteen drinks:', str(canteen))
        print('Days until water is needed:', 6 - (user_thirst))
        print('Camel tiredness:', (camel_rest), 'out of 8')
        
    #ends the game
    elif user_choice.lower() == 'q':
        print('You gave up. Your family is disappointed in you.')
        done = True
        
    #winning conditon
    if miles_left >= 200:
        print('You made it across the Mobi desert! Congradulations!')
        done = True
          
    #way to lose 
    if user_thirst >= 6:
        print('You died of thirst! Game over!')
        done = True
         
    #another way to lose   
    if camel_rest >= 8:
        print('Your camel died! Game over!')
        done = True
       
    #yet another way to lose 
    if natives_range >= miles_left:
        print('The Natives got you! Game over!')
        done = True