print("Time for a quiz!")
print("There are 5 questions. Let's begin.")
print()
PointTracker = 0
QuestionOne = input("Question 1. What is a helpful site for agile programming *hint: get* ")
if QuestionOne == "github":
    print("Correct! You got this!")
    PointTracker =   PointTracker + 1
else:
    print("Wrong...sorry.")
print()
QuestionTwo = input("What is 3*2+6-4+2 ? ")
if QuestionTwo == "10":
    print("Right! You are good at math!")
    PointTracker =   PointTracker + 1
else:
    print("Uh umm well math is hard.")
print()
QuestionThree = input("What is the easiest programming language? ")
if QuestionThree == "python":
    print("Yourrrr right!")
    PointTracker =   PointTracker + 1
else:
    print("Oh dear...")
print()
print("What is the most popular language?")
print("A. Java")
print("B. Python")
print("C. C++")
QuestionFour = input("Answer: ")
if QuestionFour =="a":
    print("Yay someone keeps up!")
    PointTracker =   PointTracker + 1
elif QuestionFour =="b":
    print("Personally I think it should be buttt..")
else:
    print("Really...come on, No.")
print()
print("last one!")
QuestionFive = input("What system did github orginally use? *hint: penguin * ")
if QuestionFive =="linux":
    print("Yay! Last question is correct!")
    PointTracker =   PointTracker + 1
else:
    print("Bummer last one wrong.")
print()
print("Here is your score")
print(PointTracker)
PrecentageRight = ( PointTracker / 5)*100
print ("With a precentage of:")
print(PrecentageRight)
