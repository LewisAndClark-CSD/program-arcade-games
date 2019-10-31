#!/usr/bin/env python3
#Chapter 3 quiz
#Bethany DuMontelle
#3 November 2017

print('Time for a quiz! Are you ready?')
print()

#Sets up score
score = int(0)

#q1
question_one = int(input('How many pokemon are there as of \
2017, not including other forms? '))

if question_one == 802:
    score = score + 1
    print('Correct!')
else:
    print('Incorrect! There are currently 802 pokemon.')
print()

#q2
print("What does pikachu's shiny look like?")
print('A. Blue')
print('B. Light yellow')
print('C. Dark yellow')
question_two = input()
if question_two.lower() == 'c':
    score = score + 1
    print('Correct!')
else:
    print('Incorrect! Pikachu is dark yellow when shiny.')
print()

#q3
print('Which of these pokemon are considered to have the worst shiny of \
all time?')
print('A. Pikachu')
print('B. Garchomp')
print('C. Charizard')
question_three = input()
if question_three.lower() == 'b':
    score = score + 1
    print('Correct!')
else:
    print('Incorrect! Garchomp is thought to have the worst shiny ever.')
print()

#q4
print('As of generation 6, what are the odds of finding a shiny pokemon? ')
question_four = int(input('1 in '))
if question_four == 4096:
    score = score + 1
    print('Correct!')
elif question_four == 8192:
    print('Wrong generation! It is now 1 in 4096.')
else:
    print('Incorrect! The odds are 1 in 4096.')
print()

#q5
print('True or false: pokemon can change their shinies when mega-evolved.')
question_five = input()
if question_five.lower() == 'true':
    score = score + 1
    print('Correct!')
else:
    print('Incorrect! Some do change their shinies when mega-evolved.')
print()

#results
percent = (int(score) / 5) * 100
print('Your total score is', str(score) + ' out of 5.')
print('This is also ' + str(percent) + ' percent.')
if score == 0 or score == 1:
    print('You didn\'t do very well.')
elif score == 2 or score == 3:
    print('Not very good, but not that bad either.')
elif score == 4:
    print('Pretty good!')
else:
    print('You did fantastic!')