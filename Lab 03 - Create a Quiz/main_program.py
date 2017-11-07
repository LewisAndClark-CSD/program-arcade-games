#!/usr/bin/env python3
#main_program.py
#Justin Riebow
#11/3/17

"""A quiz that asks questions for the user to answer"""

average = 0


print("Find the sum of: 2(15 + 12) * 4")
answerQ1 = int(input("Answer: "))
if answerQ1 == 216:
    average += 1
    print("Correct!")
else:
    print("Incorrect!")

print("Who was the 16th president of the United States?\nA: George Washington\nB: Abraham Lincoln\nC: Donald Trump\nD: Thomas Jefferson")
answerQ2 = input("Answer: ")
if answerQ2.lower() == "b":
    average += 1
    print("Correct!")
elif answerQ2.lower() == "c":
    print("... Are you serious?")
    q2seriously = input("Y/N: ")
    if q2seriously.lower() == "y":
        print("How unfortunate. Next Question.")
    else:
        print("Then who is the 16th president?")
        q2seriouslyanswer = input("Answer: ")
        if q2seriouslyanswer.lower() == "abraham lincoln":
            average += 1
            print("Good. Next question.")
        else:
            print("You disgust me. Next question.")
else:
    print("Incorrect!")
    
print("What is the capital of Illinois?")
answerq3 = input("Answer: ")
if answerq3.lower() == "springfield":
    average += 1
    print("Correct!")
else:
    print("Incorrect!")

print("You are running a race and you passed the person in second place. What place are you in now?")
answerq4 = input("Answer(without using numbers): ")
if answerq4.lower() == "second" or answerq4.lower() == "second place":
    average += 1
    print("Correct!")
else:
    print("Incorrect!")
    
print("In League of Legends, what is the name of Yasuo's ultimate ability?\nA: Last Breath\nB: Wind Slash\nC: Slice and Dice\nD: Exodia")
answerq5 = input("Answer: ")
if answerq5.lower() == "a":
    average += 1
    print("Correct!")
elif answerq5.lower() == "d":
    print("Incorrect! Completely different game, but nice try!")
else:
    print("Incorrect")
    
averagePercent = (average/5) * 100
print("You got", str(average), "correct.")
print("You got", averagePercent, "percent on this quiz.")
    
