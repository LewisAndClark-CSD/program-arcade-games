#!/usr/bin/env python
# 3.1 Create a Quiz
# Asia Robinson
# 11/2/2017

print("Quiz Time!")
print()
quiz1 = input("1. What is 61,090 - 59,352 ? ")
correct = 0
incorrect = 0

if quiz1 == ("1738"):
    print("Ayee You're Right!")
    correct = correct + 1
else:
    print("Incorrect")
    incorrect = correct - 1
print()    
quiz2 = input("2. What is Fetty Wap government first name? ")
if quiz2 == ("willie"):
    print("Ayee You're Right!")
    correct = correct + 1
else:
    print("Incorrect")
    incorrect = correct - 1
print()    
quiz3 = ("3. What is Asia favorite color?")
print(quiz3)
print("a. Red")
print("b. Blue")
print("c. Green")
answer = input("Your choice: ")
if answer == "b":
    print("Ayee You're Right!")
    correct = correct + 1
else:
    print ("Incorrect")
    incorrect = correct - 1
print()
quiz4 = ("4. Why is a bad joke like a bad pencil?")
print(quiz4)
print("a. because it has no point")
print("b. because it's not sharp")
answer = input("Your choice: ")
if answer == "a":
    print("Ayee You're Right!")
    correct = correct + 1
else:
    print ("Incorrect")
    incorrect = correct - 1
print()
quiz5 = ("5. Mary's father has 5 daughters. Nana, Nene, NiNi, and NoNo. Who's the 5th daughter ?")
print(quiz5)
print("a. Nicki")
print("b. NuNu")
print("c. Mary")
answer = input("Your choice: ")
if answer == "c":
    print("Ayee You're Right!")
    correct = correct + 1
else:
    print ("Incorrect")
    incorrect = correct - 1
print()    
print ("Total score: " + str(correct) + "/5")
division = float(100)/float(5)
multiply = float(division*correct)
result = round(multiply)
print ("Total percentage is", int(result), "%")

