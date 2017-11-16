#!/usr/bin/env python3
#quiz
#jacob poncher
#11/3/17
#
correct_answers = 0
answer1 = int(input('what is 5+6? '))
if answer1 == 11:
    print('correct')
    correct_answers = correct_answers + 1
else:
    print('incorrect')
print('what is 888 / 444? ')
print('a.1')
print('b.7')
print('c.3')
print('d.2')
answer2 = input('choice: ')
if answer2 == "d":
    print("correct")
    correct_answers = correct_answers + 1
else:
    print('incorrect')
print('we are learning java right now')
answer3 = input('true or false: ')
if answer3 == "false":
    print('correct')
    correct_answers = correct_answers + 1
else:
    print('incorrect')
answer4 = int(input("what is 2+11? "))
if answer4 == 13:
    print('correct')
    correct_answers = correct_answers + 1
else:
    print('incorrect')
answer5 = int(input('what is 20/5? '))
if answer5 == 4:
    print('correct')
    correct_answers = correct_answers + 1
else:
    print('incorrect')
print('you got',correct_answers*20,"%")
