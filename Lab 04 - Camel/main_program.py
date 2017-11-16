#!/usr/bin/env python
# 4.2 Sample Run of Camel
# Asia Robinson
# 11/6/2017

import random
print('Welcome to Camel!')
print('You have stolen a camel to make your way across the great Mobi desert.')
print('The natives want their camel back and are chasing you down! Survive your desert trek and out run the natives.')
print()
user_distance = 0
camel = 0
drinks = 3
thirst = 0
natives = -20
done = False
while done == False:
    print('A. Drink from your canteen.')
    print('B. Ahead moderate speed.')
    print('C. Ahead full speed.')
    print('D. Stop for the night.')
    print('E. Status check.')
    print('Q. Quit.')
    choice = input('Your choice? ').upper()
    if random.randint(1,20) == 5:
        drinks = 3
        camel = 0
        print('You found an oasis!')
    if (user_distance - natives) < 15:
        print('The natives are getting close')
    if natives >= user_distance:
        print('The natives caught you and took you back to their village')
        done = True
    if camel >= 8:
        print('Your camel is dead')
        done = True
    elif camel > 5:
        print('Your camel is tired')
    if thirst >= 6:
        print('You died!')
        done = True
    elif thirst > 4:
        print('You are thirsty!')

    if choice == 'Q':
        done = True

    elif choice == 'E':
        print('Miles traveled: ' + str(user_distance))
        print('Drinks in canteen: ' + str(drinks))
        print('The natives are ' + str(abs(user_distance-natives)) + ' miles behind you.')

    elif choice == 'D':
        camel = 0
        print('The camel is happy')
        natives = random.randint(7,14) + natives

    elif choice == 'C':
        r = random.randint(10,20)
        user_distance = r + user_distance
        print('You traveled ' + str(r) + ' miles!')
        thirst = thirst + 1
        camel = random.randint(1,3)
        n = random.randint(7,14)
        natives = n + natives
        print('The natives have moved ' + str(n) + ' miles!')

    elif choice == 'B':
        R = random.randint(5, 12)
        Ran = random.randint(7,14)
        user_distance = user_distance + R
        print('You have traveled ' + str(R) + ' miles!')
        thirst = thirst + 1
        camel = camel + 1
        natives = natives + Ran
        print('The natives have moved ' + str(Ran) + ' miles!')

    elif choice == 'A':
        if drinks > 0:
            drinks = drinks - 1
            thirst = 0
        else:
            print('You cannot drink from an empty canteen')

