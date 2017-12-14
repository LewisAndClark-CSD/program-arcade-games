#!/usr/bin/env python3
#Camel
#Christian Groves
#11/9/17
import random
print('Welcome to Camel!')
print('You have stolen a camel to make your way across the great Mobi desert.')
print('The natives want their camel back and are chasing you down! Survive your')
print('desert trek and out run the natives.')
done = False
oasis = 0
miles = 0
thirst = 0
cameltired = 0
nativestravel = -20
cantinedrinks = 3
alive = True
while done is False:
    print('A. Drink from your canteen.')
    print('B. Ahead moderate speed.')
    print('C. Ahead full speed.')
    print('D. Stop for the night.')
    print('E. Status check.')
    print('Q. Quit.')
    userchoice = input('Your choice? ')
    oasis = random.randrange(0, 20)
    if userchoice.upper() == 'Q':
        done = True
    elif userchoice.upper() == 'D':
        cameltired = 0
        print('Your camel is happy.')
        nativestravel += random.randrange(7, 14)
    elif userchoice.upper() == 'E':
        print('Miles traveled: '+ str(miles))
        print('Drinks in canteen: ' + str(cantinedrinks))
        print('The natives are '+ str(nativestravel) + ' miles behind you.')
    elif userchoice.upper() == 'C':
        randomint = random.randrange(10, 20)
        miles += randomint
        print('Miles traveled ' + str(randomint))
        nativestravel += random.randrange(7, 14)
        cameltired += random.randrange(1, 3)
        thirst += 1
    elif userchoice.upper() == 'B':
        randomint = random.randrange(5, 12)
        miles += randomint
        print('Miles traveled ' + str(randomint))
        nativestravel += random.randrange(7, 14)
        cameltired += 1
        thirst += 1
    elif userchoice.upper() == 'A':
        if cantinedrinks > 0:
            cantinedrinks -= 1
            thirst = 0
        else:
            print('Error')
    if thirst > 4 and not thirst > 7 and done != True:
        print('You are thirsty.')
    elif thirst > 6 and done != True:
        print('You died of thirst!')
        done = True
        alive = False
    if cameltired > 5 and not cameltired > 9 and done != True:
        print('Your camel is getting tired')
    elif cameltired > 8 and done != True:
        print('Your camel is dead.')
        done = True
        alive = False
    if nativestravel > miles and done != True:
        print('They have caught you')
        alive = False
    elif (nativestravel + 15) > miles and not nativestravel > miles:
        print('The natives are getting close')
    if oasis == 2:
        print('You have found a oasis')
        cantinedrinks = 3
        cameltired = 0
        thirst = 0
    if miles >= 200:
        if done != True:
            print('You win')
            done = True
            