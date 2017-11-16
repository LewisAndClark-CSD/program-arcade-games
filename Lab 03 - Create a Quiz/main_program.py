#!/usr/bin/env python3
# main_program.py
# Jared Rhodes
# 11/03/2017

""" This is the quiz game for chapter 3's lab """

num_Correct = 0



print("This is a quiz game to test your knowlege of random facts")
print("This quiz with consist of 6 questions on varying subjects")

print("Question Number 1")
print("What is the atomic number for Lithium?")
print("A. 6\nB. 8\nC. 5\nD. 3")
usr_Ans = input()

if usr_Ans.upper() == "D":
    print("Your answer was correct")
    num_Correct += 1
else:
    print("Your answer was incorrect")


print("Question Number 2")
print("What is the biggest animal?")
print("A. Elephant\nB. Blue Whale\nC. Sperm Whale\nD. Great White Shark")
usr_Ans = input()

if usr_Ans.upper() == "B":
    print("Your answer was correct")
    num_Correct += 1
else:
    print("Your answer was incorrect")

print("Question Number 3")
print("How many planets are there in our solar system?")
print("A. Eight\nB. Nine\nC. Seven\nD. Ten")
usr_Ans = input()

if usr_Ans.upper() == "A":
    print("Your answer was correct")
    num_Correct += 1
else:
    print("Your answer was incorrect")

print("Question Number 4")
print("What fictional universe do the Borg come from?")
print("A. Star Trek\nB. Firefly\nC. Star Wars\nD. Dark Matter")
usr_Ans = input()

if usr_Ans.upper() == "A":
    print("Your answer was correct")
    num_Correct += 1
else:
    print("Your answer was incorrect")

print("Question Number 5")
print("What percent of the earth's surface is water?")
print("A. 70%\nB. 72%\nC. 64%\nD. 71%")
usr_Ans = input()

if usr_Ans.upper() == "D":
    print("Your answer was correct")
    num_Correct += 1
else:
    print("Your answer was incorrect")

print("Question Number 6")
print("Which country borders China?")
print("A. Thailand\nB. South Korea\nC. India\nD. Japan")
usr_Ans = input()

if usr_Ans.upper() == "C":
    print("Your answer was correct")
    num_Correct += 1
else:
    print("Your answer was incorrect")

print("Congradulations on completing my Quiz")
print("You scored a", num_Correct, "out of 6")
print("This is a", str(num_Correct / 6) + "%")


