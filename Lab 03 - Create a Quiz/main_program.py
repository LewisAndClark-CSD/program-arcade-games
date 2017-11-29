#!/usr/bin/env python3
# Creating a quiz 
# Brady Ballmann
# 11/03/2017

percentage = 0

print('Ready for a quiz? :)')

question_one = input('Who won the 2017 World Series? ')
if question_one.lower() == "astros":
    print("Correct!")
    percentage += 1
else:
    print('Incorrect!')

question_two = int(input("What is 5 * 432 / 4? "))
if question_two == 540:
        print("Correct!")
        percentage += 1
else:
    print("Incorrect!")
    
print("What is the most common male name in the US?")
print("1. James")
print("2. Robert")
print("3. David")
print("4. Michael")
print("TIP! Enter the number not the name")
question_three = int(input('? '))
if question_three == 1:
    print('Correct!')
    percentage += 1
else:
    print("Incorrect!")
    
    
question_four = int(input("What is 10 to the power of 3? "))
if question_four == 1000:
        print("Correct!")
        percentage += 1
else:
    print("Incorrect!")
    
print('If an apple weighs about 3 and 1/2 ounces. What is the radius of the sun? ')
print("1. 432,288 mi")
print("2. 542,421 mi")
print("3. 674,321 mi")
print("4. 132,424 mi")
print("TIP! Enter the number not the name.")
question_five = int(input('? '))
if question_five == 1:
    print('Correct!')
    percentage += 1
else:
    print("Incorrect!")
    
percent = percentage * 20    
print("You got" , percentage, "out of 5")
print(percent, "percent! Congrats!")
    


    
    
    



