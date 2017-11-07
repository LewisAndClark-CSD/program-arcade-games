import random

print("Welcome to Camel!")
print("You have stolen a camel to make your way across the great Mobi desert")
print("The natives want their camel back and are chasing you down!")
print("Survive crossing the desert, and outrun those natives!")

done = False
miles = 0
thirst = 0
tiredness = 0
native_Miles = -20
canteen_Drinks = 3

while done == False:
    print("Your choices are -----------")
    print("A. Drink from your canteen")
    print("B. Ahead moderate speed")
    print("C. Ahead full speed")
    print("D. Stop for the night")
    print("E. Status check")
    print("Q. Quit")
    usr_Decision = input()
    
    if usr_Decision.upper() == "Q":
        done = True
        
    if usr_Decision.upper() == "E":
        print("You currently have", canteen_Drinks, 
              "drinks left in your canteen")
        print("You currently have traveled", miles, 
              "miles")  
        print("The natives are currently", miles - native_Miles, 
              "miles behind you")    
    
    if usr_Decision.upper() == "D":
        print("Your camel thanks you!")
        tiredness = 0
        native_Miles += random.randint(7, 14)\
    
    if usr_Decision.upper() == "C":
        miles_Traveled = random.randint(10, 20)
        print("You traveled", miles_Traveled, "miles")
        miles += miles_Traveled
        tiredness += random.randint(1, 3)
        thirst += 1
        native_Miles += random.randint(7, 14)
        
    if usr_Decision.upper() == "B":
        miles_Traveled = random.randint(5, 12)
        print("You traveled", miles_Traveled, "miles")
        miles += miles_Traveled
        tiredness += 1
        thirst += 1
        native_Miles += random.randint(7, 14) 
        
    if usr_Decision.upper() == "A":
        if canteen_Drinks >= 1:
            print("You take a drink, and feel refreshed")
            canteen_Drinks -= 1
            thirst = 0
        else:
            print("You don't have any drinks left :(")
            
    if thirst > 4:
        print("You are thirsty")
    elif thirst > 6:
        print("You died of thirst")
        done = True
        
    if tiredness > 5:
        print("Your camel is getting tired")
    elif tiredness > 8:
        print("Your camel died")
        done = True    
        
    if native_Miles >= miles:
        print("You done got caught, by the natives")
        done = True
    elif native_Miles >= miles - 15:
        print("The natives are getting close!")
        
    if miles >= 200:
        print("You made it through the desert!")
        print("You win, you didn't die, that is equaivalent to winning!")
        done = True
    
    chance = random.randint(1, 20)
    
    if chance == 1:
        print("You stumbled on an oasis")
        canteen_Drinks = 3
        thirst = 0
        tiredness = 0
    