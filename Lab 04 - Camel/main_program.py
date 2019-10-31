#Camel Coding Game

print('Welcome to Camel!')
print('You have stolen a camel to make your way across the great Mobi desert.')
print('The natives want their camel back and are chasing you down! Survive your desert trek and out run the natives.')

traveledMiles = 0
thirst = 0
camelTiredness = 0
nativesTraveled = -20
canteenDrinks = 20
import random

done = False 
while done == False:
    print('A. Drink from your canteen.')
    print('B. Ahead moderate speed.')
    print('C. Ahead full speed.')
    print('D. Stop for the night.')
    print('E. Status check.')
    print('Q. Quit.')
    user_choice = input('What is your choice? ')
    if user_choice.upper() == 'Q':
        done = True
    elif user_choice.upper() == 'E':
        print('Miles traveled:', traveledMiles)
        print('Drinks in canteen:', canteenDrinks)
        print('The natives are', nativesTraveled, 'miles behind you.')
    elif user_choice.upper() == 'D':
        camelTiredness = 0
        print('The camel is happy!')
        nativesTraveled += random.randint(7, 15)
    elif user_choice.upper() == 'C':
        traveledMiles += random.randint(10, 21)
        print('Miles traveled:', traveledMiles)
        thirst += 1
        camelTiredness += random.randint(1, 4)
        nativesTraveled += random.randint(7, 15)
    elif user_choice.upper() == 'B':
        traveledMiles += random.randint(5, 13)
        print('Miles traveled:', traveledMiles)
        thirst += 1
        camelTiredness += 1
        nativesTraveled += random.randint(7, 15)
    elif user_choice.upper() == 'A':
        if canteenDrinks > 0:
            canteenDrinks -= 1
            print('Drinks in canteen:', canteenDrinks)
            thirst = 0
        else:
            print('Error: no drinks in canteen.')

if thirst > 4:
    print('You are thirsty.')
elif thirst > 6:
    print('You died of thirst!')
    done = True
if camelTiredness > 5:
    print('Your camel is getting tired.')
elif camelTiredness > 8:
    print('Your camel is dead.')
if nativesTraveled == 0:
    print("You've been caught! Game over, try again.")
    done = True
elif nativesTraveled <= -15:
    print('The natives are getting close!')
if traveledMiles == 200:
    print('You won! Game over, play again!')
    done = True
