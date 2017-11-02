#!/usr/bin/env python3
#Quiz
#Ryan Rosvall
#11/1/17

print('Quiz time!')
totalRight = 0
print()
questionOne = input('The beaver is the national emblem of which country? ')
if questionOne == 'Canada' or questionOne == 'canada' or questionOne == 'CANADA':
    print()
    print('Correct!')
    print("You've gained a point! Great job!")
    print()
    totalRight = totalRight + 1
else:
    print()
    print('WRONG!, The correct answer is Canada.')
    print()

questionTwo = input('Who is the director of the Lord of The Rings trilogy? ')
if questionTwo == 'Peter Jackson' or questionTwo == 'peter jackson' or questionTwo == 'PETER JACKSON':
    print()
    print('Good Job!')
    print('Thats another point to your total!')
    totalRight = totalRight + 1
else:
    print()
    print('WRONG! The correct answer is Peter Jackson')
  
print()
print('Next Question!')
  
questionThree = input('What is 9 * 9? ')
if questionThree == str(81):
    print()
    print('Good Job!')
    totalRight = totalRight + 1
    if totalRight == 3:
        print("YOU'RE ON FIRE!!!")
        
else:
    print()
    print('WRONG! The correct answer is 81')
    
print()
print('How many cities are in Missouri? ')
a = print('a = 108')
b = print('b = 121')
c = print('c = 105')
d = print('d = 117')
print()
questionFour = input('Choose your answer: ')
if questionFour == "c":
    print()
    print('Outstanding!')
    totalRight = totalRight + 1
else:
    print()
    print('WRONG! The correct answer is c.')

print()
print('Next Question!')
questionFive = input('Al Capone was sentenced to 11 years in prison for what crime? ')
if questionFive == 'Tax Evasion' or questionFive == 'tax evasion' or questionFive == 'TAX EVASION':
    print()
    print('Good Job!')
    totalRight = totalRight + 1
else:
    print()
    print('WRONG! The correct answer is Tax Evasion')

print()
print('The amount you got right was: ' + str(totalRight) + '/5')
print()
print('Your % was ' + str((totalRight/5) * 100))
