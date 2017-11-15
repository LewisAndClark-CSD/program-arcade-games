#!/usr/bin/env python3
# The Dank Quiz
# Lauren Boehme
# 11/3/17
# Defining Score variables 
x = 0
score = x

# Question 1 
print("Who is impossible to defeat?")
answer_1 = input("a)Sans\nb)Flowey\nc)Asriel\nd)None if you are filled with determination\n:")
if answer_1.lower() == "d" or answer_1.lower() == "None":
    print("Correct")
    x = x + 1   
else:
    print("Incorrect, you are filled with determination.")

# Question 2
print("Who is the current president of the United States?")
answer_2 = input("a)Barack Obama\nb)Kanye\nc)A clown\nd)Walugi\n:")
if answer_2.lower() == "c" or answer_2.lower() == "a clown":
    print("Correct")
    x = x + 1
else:
    print("Incorrect , it's orange babyhand clownmcgee. Walugi 2020.")

# Question 3
print("True or False: Dogs are better than cats.")
answer_3 = input(":")
if answer_3.lower() == "true" or answer_3.lower() == "t":
    print("Correct")
    x = x + 1
else:
    print("Incorrect")  

# Question 4
print("Whos is the best Smash Bros character?")
answer_4 = input("a)Kirby\nb)Doctor Mario\nc)Olimar\nd)Fox\n:")
if answer_4.lower() == "a" or answer_4 == "Kirby":
    print("Correct")
    x = x + 1
else:
    print("You're wrong- everyone knows that Kirby is the roundest and the strongest.")

# Question 5 
print("True or False... Gun is the most powerful enemy in Contra?")
answer_5 = input(":")
if answer_5.lower() == "false" or answer_5.lower() == "f":
    print("Correct, watch out for Dog.")
    x = x + 1
else:
    print("Incorrect, watch out for Dog.")


# Score
score = float(x / 5) * 100
print(x,"correct. That's",score, "%")
