#!/usr/bin/env python3
# Princess Theif
# Lauren Boehme
# 11/7/17

import random

print('Welcome to Camel! ')
print('You have stolen a camel to make your way across the great Mobi desert. The natives want their camel back and they are coming after you! Survive the desert and out run the natives. ')

done = False
c_thirst = 0
c_tired = 0
miles_traveled = 0
distance_natives = -20
drinks_canteen = 4


random_oasis = random.randrange(1,21)
random_forward = random.randrange(10,21)
random_native  = random.randrange(7,15)
random_tiredness = random.randrange(1,4)
random_moderate = random.randrange(5,13)


while not done:
    print('A. Drink from your canteen.')
    print('B. Ahead moderate speed.')
    print('C. Ahead full speed.')
    print('D. Stop and rest.')
    print('E. Status check.')
    print('Q. Quit.')
    print()
usranswer=input('Your choice: ')
if usranswer.upper() == 'Q':
    done = True
elif usranswer.upper() == 'E':
    print('Miles traveled: ', miles_traveled)
    print('Drinks in canteen: ', drinks_canteen)
    print('The natives are ', distance_natives, 'miles behind you. ')

elif usranswer.upper() == 'D':
    c_tired = 0
    print('The camel is happy!')
    distance_natives =distance_natives + random_native
elif usranswer.upper() == 'C':
    miles_traveled = miles_traveled + random_forward
    print('You traveled', str(miles_traveled) + ' miles.')
    camel_thirst = camel_thirst + 1
    camel_tired = camel_tired + 1
    distance_natives = distance_natives + random_native
elif usranswer.upper() == 'B':
    print('You traveled', str(random_moderate) + ' miles.')
elif usranswer.upper() == 'A':
