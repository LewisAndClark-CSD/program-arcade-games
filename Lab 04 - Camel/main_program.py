#!/usr/bin/env python3
#Lab 4 chapter 4 Camel
#Bethany DuMontelle
#3 November 2017

from random import randint

miles_left = 1000
natives_range = 1025
user_thirst = 6
canteen = 5
camel_rest = 10
done = False

print('Welcome to Camel!')
print('You have stolen a camel to make your way across the Great Mobi desert.')
print('The natives want their camel back and are chasing you down! Survive')
print('your desert trek and out run the natives.')

while done != True:
    
    native_close = (natives_range) - (miles_left)
    
    oasis = randint(1,20) 
        
    print('You are', str(miles_left), 'miles from crossing the Mobi dessert.')
    
    if native_close > 0 and native_close < 20:
        print('The natives are only', str(native_close), 'miles from you!')
    else:
        print('The Natives are', str(native_close), 'miles away from you.')
        
    print('You have', str(canteen), 'drinks left in your canteen.')
    
    if user_thirst <= 2:
        print('You are getting thirsty!')
        
    if camel_rest <= 2:
        print('The camel is getting tired!')
        
    
    print('What would you like to do?')
    print('A. Drink from your canteen')
    print('B. Ahead moderate speed.')
    print('C. Ahead full speed.')
    print('D. Stop for the night.')
    print('E. Status check.')
    print('Q. Quit')
    
    user_choice = input()
    
    if user_choice.lower() == 'a':
        if canteen <= 0:
            print('You don\'t have any more water!')
        else:
            user_thirst = user_thirst + 1
            canteen = canteen - 1
        
    elif user_choice.lower() == 'b':
        miles_move = randint(11,29)
        miles_left = (miles_left) - (miles_move)
        natives_move = randint(15,24)
        natives_range = (natives_range) - (natives_move)
        camel_rest = (camel_rest) - 1
        user_thirst = user_thirst - 1
        print('You moved', + (miles_move), 'miles.')
        if oasis == 1:
            canteen_fill = randint(2,5)
            print('You found an oasis!')
            print('You can now drink', (canteen_fill), 'more times.')        
        
    elif user_choice.lower() == 'c':
        miles_move = randint(25,36)
        miles_left = (miles_left) - (miles_move)
        natives_move = randint(15,24)
        natives_range = (natives_range) - (natives_move)
        camel_rest = (camel_rest) - 2
        user_thirst = user_thirst - 1
        print('You moved', + (miles_move), 'miles.')
        if oasis == 1:
            canteen_fill = randint(2,5)
            print('You found an oasis!')
            print('You can now drink', (canteen_fill), 'more times.')        
        
    elif user_choice.lower() == 'd':
        camel_shleep = randint(4,10)
        camel_rest = (camel_rest) + (camel_shleep)
        natives_move = randint(15,20)
        natives_range = (natives_range) - (natives_move)
        print('The camel is happy.')
    
    elif user_choice.lower() == 'e':
        print('Miles left:', str(miles_left))
        print('Native distance:', str(natives_range))
        print('Canteen drinks:', str(canteen))
        print('Your thirst:', str(user_thirst))
        print('Camel rest level:', str(camel_rest))
        
    elif user_choice.lower() == 'q':
        print('You gave up. Your family is disappointed in you.')
        done = True
        
    if miles_left <= 0:
        print('You made it across the Mobi desert! Congradulations!')
        done = True
            
    if user_thirst <= 0:
        print('You died of thirst! Game over!')
        done = True
            
    if camel_rest <= 0:
        print('Your camel died! Game over!')
        done = True
        
    if native_close <= 0:
        print('The Natives got you! Game over!')
        done = True