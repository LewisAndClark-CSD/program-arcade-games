#!/usr/bin/env python3
# Lab 03 - Create a Quiz
# Conner Walkenhorst
# 11/7/2017

"""Make my own quiz from scratch"""

total = 0
print('Welcome to My Quiz')
answer1 = int(input('Question #1: What is 2+2? '))
if answer1 == 4:
    total += 1
    print(answer1,'is correct.')
else:
    print('Sorry',answer1,'is incorrect.')
answer2 = int(input('Question #2: How many letters does the color blue have in its name? '))
if answer2 == 4:
    total += 1
    print(answer2,'is correct.')
else:
    print('Sorry',answer2,'is incorrect.')
answer3 = input('Question #3: What is the name of the United States National Anthem? ')
if answer3 == 'The Star-Spangled Banner' or answer3 == 'the star-spangled banner' or answer3 == 'The Star Spangled Banner' or answer3 == 'the star spangled banner':
    total += 1
    print(answer3,'is correct.')
else:
    print('Sorry',answer3,'is incorrect.')
answer4 = int(input('Question #4: How many letters does the color red have in its name? '))
if answer4 == 3:
    total += 1
    print(answer4,'is correct.')
else:
    print('Sorry',answer4,'is incorrect.')
answer5 = input('Question #5: What is the best soda ever made? ')
if answer5 == 'Mountain Dew' or answer5 == 'mountain dew' or answer5 == 'mt. dew' or answer5 == 'mt dew':
    total += 1
    print(answer5,'is correct.')
else:
    print('Sorry',answer5,'is incorrect.')
percentCorrect = (total/5)*100
print(str(percentCorrect) + '%')
