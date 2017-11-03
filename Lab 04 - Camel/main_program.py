#
import random

print("Welcome to Camel!")
print("You have stolen a camel to make your way across the great Mobi desert.")
print("The natives want their camel back and are chasing you down!" "\n" "Survive your desert trek and out run the natives.")

total_miles_traveled = 0
miles_traveled = 0
thirst = 0
camel_tiredness = 0
drinks_in_canteen = 3
native_location = -20

done = False

while done == False:
    print("A. Drink from your canteen.")
    print("B. Ahead moderate speed.")
    print("C. Ahead full speed.")
    print("D. Stop for the night.")
    print("E. Status check.")
    print("Q. Quit.")

    user_choice = input("Your choice? ")
    if user_choice.upper() == "Q":
        done = True


    elif user_choice.upper() == "E":
       print("Miles Traveled:", total_miles_traveled)
       print("Drinks in canteen:", drinks_in_canteen)
       print("The natives are", native_location*(-1), "miles behind you.")
       print("Camel tiredness:", camel_tiredness)
       print("Thirst", thirst)
       

    elif user_choice.upper() == "D":
        camel_tiredness = 0
        print("The camel is happy")
        native_location += random.randint(7, 14)
        if native_location >= 0:
            print("The natives have caught you")
            done = True
        if -10 <= native_location <= -15:
            print("The natives are getting close!")
        if -8 <= native_location <= -2:
            print("The natives are getting really close!")
        

    elif user_choice.upper() == "C":
        miles_traveled += random.randint(10,20)
        print("You traveled",miles_traveled,"miles")
        total_miles_traveled += miles_traveled
        native_location += random.randint(7,14) - miles_traveled
        miles_traveled = 0
        thirst += 2
        camel_tiredness += 2
        if 4<= thirst <= 6:
            print("You are thirsty.")
        if thirst > 6:
            print("You died of thirst!")
            done = True
        if 5<= camel_tiredness >=8:
            print("Your camel is getting tired.")
        if camel_tiredness > 8:
            print("Your camel is dead.")
            done = True
        if miles_traveled >= 200:
            print("You have won! Good Job")
            done = True
        if native_location >= 0:
            print("The natives have caught you")
            done = True
        if 10 <= native_location <= 15:
            print("The natives are getting close!")
        if 8 <= native_location <= 2:
            print("The natives are getting really close!")
        oasis = random.randint(1,20)
        lucky_oasis_number = 5
        if oasis == lucky_oasis_number:
            print("You found the oasis")
            thirst = 0
            camel_tiredness = 0
            drinks_in_canteen = 4


    elif user_choice.upper() == "B":
        miles_traveled += random.randint(5,12)
        print("You traveled",miles_traveled,"miles.")
        total_miles_traveled += miles_traveled
        native_location += random.randint(7,14) - miles_traveled
        miles_traveled = 0
        thirst += 1
        camel_tiredness += 1
        if 4<= thirst <= 6:
            print("You are thirsty.")
        if thirst > 6:
            print("You died of thirst!")
            done = True
        if 5<= camel_tiredness >=8:
            print("Your camel is getting tired.")
        if camel_tiredness > 8:
            print("Your camel is dead.")
            done = True
        if miles_traveled >= 200:
            print("You have won! Good Job")
            dont = True
        if native_location >= 0:
            print("The natives have caught you")
            done = True
        if 10 <= native_location <= 15:
            print("The natives are getting close!")
        if 5 <= native_location <= 2:
            print("The natives are getting really close!")
        oasis = random.randint(1,20)
        lucky_oasis_number = 5
        if oasis == lucky_oasis_number:
            print("You found the oasis")
            thirst = 0
            camel_tiredness = 0
            drinks_in_canteen = 4

    elif user_choice.upper() == "A":
        if drinks_in_canteen > 0:
            drinks_in_canteen = drinks_in_canteen - 1
            thirst = 0
            print("You have", drinks_in_canteen, "drinks left.")
        else:
            print("You're out of water")
