#!/usr/bin/env python3
#Create a Quiz
#Evan Witterholt
#11/6/17

score = 0

question1 = int(input('How many states are in the US?: '))
if question1 == 50:
    score += 1   
print('That is correct!')

question2 = int(input('Pluto is a planet. 1 for True or 2 for False?: '))
if question2 == 2:
    score += 1
print('That is correct!')
                
question3 = int(input('What is 9+10?: '))
if question3 == 19:
    score += 1
print('That is correct!')
                
question4 = int(input('How many planets are between the Earth and the Moon?: '))
if question4 == 0:
    score += 1
print('That is correct!')
              
question5 = int(input('What question are you on?: '))
if question5 == 5:
    score += 1
print('That is correct!')
          
print (score, 'out of 5')
