# Completed Lab 4
import random
print("Welcome to Camel!")
print("You have stolen a camel to make your way across the great Mobi desert.")
print("The natives want their camel back and are chasing you down! Survive your desert trek and out run the natives.")
print("Hint: all capitals.")
print()

A = "A. Drink from your canteen."
B = "B. Ahead moderate speed."
C = "C. Ahead full speed."
D = "D. Stop for the night."
E = "E. Status check."
Q = "Q. Quit."
done = False
miles_traveled = 0
thirst = 0
camel_tiredness = 0
natives_distance = -20
canteen_drinks = 5

while not done:
  print(A)
  print(B)
  print(C)
  print(D)
  print(E)
  print(Q)
  user_choice= input("Your choice: ")
  if user_choice == "Q":
    done=True

  elif user_choice == "E":
    print()
    print("Miles traveled:", miles_traveled)
    print("Drinks in canteen:", canteen_drinks)
    print("The natives are", natives_distance, "miles behind you.")
    print()
  elif user_choice == "D":
    camel_tiredness= 0
    natives_distance+= random.randrange(7,14)
    print()
    print("Your camel is fully rested.")
    print()
  elif user_choice == "C":
    miles_traveled+= random.randrange(10,21)
    thirst= thirst+1
    camel_tiredness+= random.randrange(1,4)
    natives_distance+= random.randrange(7,14)
    print()
    print("Your miles traveled are:", miles_traveled)
    print()
  elif user_choice == "B":
    miles_traveled+= random.randrange(5,12)
    thirst+= 1
    camel_tiredness+= 1
    natives_distance+= random.randrange(7,14)
    print()
    print("Your miles traveled are:", miles_traveled)
    print()
  elif user_choice == "A":
    thirst= 0
    canteen_drinks-= 1
    print()
    print("Your thrist is:", thirst)
    print()
    
  if miles_traveled >= 200 and not done:
    print("You've won the game!")
    done= True
  if thirst > 4 and thirst <= 6 and not done:
    print("You are thirsty!")
    print()
  if thirst > 6:
    print("You died of thirst.")
    print("You lose.")
    print()
    done=True
  if camel_tiredness > 5 and camel_tiredness <= 8 and not done:
    print("Your camel is getting tired.")
    print()
  if camel_tiredness > 8:
    print("Your camel is dead.")
    print("You lose.")
    done= True
  if natives_distance >= miles_traveled:
    print("The natives have caught up to you.")
    print("You lose.")
    done= True
  if natives_distance > miles_traveled+15:
    print("The natives are getting close!")
    print()
