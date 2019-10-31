#!/usr/bin/env python3
# camel
#jacob poncher
# 11/8/17

""" Camel Game """

import random
print('Welcome to Camel!')
print('You have stolen a camel to make your way across the great mobi desert')
print('The natives want their camel back and are chasing you down!')
print('Survive your desert trek and out run the natives')
miles_traveled = 0
thirst = 0
camel_tiredness =0 
natives_distance =-20
drinks = 5
done = False
while not done:
    print()
    print('A.Drink from your canteen.')
    print('b.ahead moderate speed. ')
    print('c.Ahead full speed.')
    print('d.stop for the night.')
    print('e.status check.')
    print('q .Quit')
    choice = input('choice: ')
    print()
    if choice == "q":
        done = True
    elif choice == "e":
        print()
        print("miles traveled: ",miles_traveled)
        print("drinks in canteen: ", drinks)
        print('the natives are',abs(natives_distance),"miles behind you.")
        print()
    elif choice == 'd':
        camel_tiredness = 0
        print('the camel is happy')
        natives_distance = natives_distance + random.randrange(7,14)
    elif choice == "c":
        miles_traveled = miles_traveled + random.randrange(10,21)
        print('miles traveled:',miles_traveled)
        thirst = thirst + 1
        camel_tiredness = camel_tiredness + random.randrange(1,4)
        natives_distance = natives_distance + random.randrange(7,14)
    elif choice == "b":
        miles_traveled = miles_traveled + random.randrange(5,12)
        print('miles traveled',miles_traveled)
        thirst = thirst + 1 
        camel_tiredness = camel_tiredness + 1
        natives_distance = natives_distance + random.randrange(7,14)
    elif choice == "a":
        if drinks > 0:
            drinks = drinks - 1
        else:
            print('error')
    else:
        print("That is not a valid choice! ")
        
        
    if thirst > 4 and thirst < 6:
        print('you are thirsty')
    if thirst > 6:
        print('you died of thirst')
        done = True 
    
    if natives_distance >= 0:
        print('the natives have caught up')
        done = True 
    elif natives_distance >= -15:
        print('The natives are getting close')
    
    if miles_traveled >= 200 and done == False:
        print('you win the game')
        miles_travled = 0
        thirst = 0 
        camel_tiredness = 0
        drinks = 5
        natives_distance = -20
