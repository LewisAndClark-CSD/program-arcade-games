# !/usr/bin/env python3
# camel game
# Ryan Moore
# 11/7/2017

print('Welcome to Camel!')
print('You have stolen a camel to make your way across the great Mobi desert.')
print('The natives want their camel back and are chasing you down! Survive your') 
print('desert trek and out run the natives.')
import random
done = False
miles_traveled = 0
thirst = 0
camel_tiredness =0
natives_traveled = -20

random_native = random.randrange(7, 15)

random_full
 
while not done: 
    user_choiceA = print('A. Drink from your canteen. ')
    user_choiceB = print('B. Ahead moderate speed. ')
    user_choiceC = print('C. Ahead full speed. ')
    user_choiceD = print('D. Stop for the night. ')
    user_choiceE = print('E. Status check. ')
    user_choiceQ = print('Q. Quit. ')
    user_input = input('Your choice? ')
    if user_input.upper() == "Q":
        done = True
    elif user_input == 'E':
        print('Miles traveled:',miles_traveled)
        print('Drinks in canteen:',thirst)
        print('The natives are',natives_traveled,'miles behind you')
    elif user_input == 'c':
