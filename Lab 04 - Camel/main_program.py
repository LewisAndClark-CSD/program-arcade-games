#!/usr/bin/env python3
# Camel game
# Brady Ballmann
# November 6th 2017

import random

print("Welcome to Camel!")
print("You have stolen a camel to make your way across the great Mobie desert.")
print("The natives want their camel back and are chasing you down! Survive your")
print("desert trek and out run the natives.")

done = False
camel_thirst = 0
camel_tired = 0
miles_traveled = 0
distance_natives = -20
drinks_canteen = 3


random_oasis = random.randrange(1 , 21)

random_forward = random.randrange(10 , 21)

random_native = random.randrange(7 , 15)

random_tiredness = random.randrange(1 , 4)

random_moderate = random.randrange(5, 13)


while not done:
print("A. Drink from your canteen.")
print("B. Ahead moderate speed.")
print("C. Ahead full speed.")
print("D. Stop for the night.")
print("E. Status check.")
print("Q. Quit.")
print()
user_answer = input("Your choice? ")
if user_answer.upper() == "Q":
     done = True
elif user_answer.upper() == "E":
     print("Miles traveled:", miles_traveled)
     print("Drinks in canteen: ", drinks_canteen)
     print("The natives are", str(distance_natives) + " miles behind you")
elif user_answer.upper() == "D":
     camel_tired = 0
     print("The camel is happy :D")
     distance_natives = distance_natives + random_native
elif user_answer.upper() == "C":
     miles_traveled = miles_traveled + random_forward
     print("You traveled", str(miles_traveled) + " miles.")
     camel_thirst = camel_thirst + 1
     camel_tired = camel_tired + random_tiredness
     distance_natives = distance_natives + random_native
elif user_answer.upper() == "B":
     print("You traveled", str(random_moderate) + " miles.")
     camel_thirst = camel_thirst + 1
     camel_tired = camel_tired + 1
     distance_natives = distance_natives + random_native
elif user_answer.upper() == "A":
     drinks_canteen = drinks_canteen - 1
     camel_thirst = 0
elif not done and camel_thirst < 4:
     print("You are thirsty")
elif not done and camel_thirst < 6:
     print("You died")
     done = True
elif camel_tired > 5:
     print("Your camel is getting tired")
elif camel_tired > 8:
     print("Your camel is dead")
     done = True
elif distance_natives >= miles_traveled:
     print("The natives have caught you")
     done = True
elif miles_traveled >= 200:
     print("YOU WON!")
elif random_oasis == 10:
     print("You found an oasis")
     drink_canteen = 3
     camel_thirst = 0
     camel_tired = 0
