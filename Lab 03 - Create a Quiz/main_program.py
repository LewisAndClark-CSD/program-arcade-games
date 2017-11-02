#

questionOne = input('What color is the sky? ')
score = 0
if questionOne == 'blue' or 'Blue':
    print('Good job you are one for one!')
    score = score + 1
else:
    print('Awh darn, one wrong!')
print()
print('Next question')
print()
questionTwo = input('What has two wheels that people use for transportation? ')
if questionTwo == 'Bike' or 'bike':
    print('Woooo, thats how we get it done!')
    score = score + 1
else:
    print()
    print('You got the next one')
print()
print('Next question')
print()
questionThree = input('How many tires does a car have? ')
if questionThree == '4':
    print('Correct')
    print()
    score = score + 1
else:
    print('Wrong!')
print('Next question')
print()
questionFour = input('What go on your feet to protect them while you walk? ')
if questionFour == 'Shoes' or 'shoes':
    print('Correct!')
    print()
    score = score + 1
else:
    print(':( sad day with the wrong answer')
    print()
print('Final Question!')
questionFive = input('What is Lincoln"s first name? ')
if questionFive == 'Abraham' or 'abraham':
    print('You"re all done! Good job!')
    print()
    score = score + 1
else:
    print('It"s over! But what a terrible way to end')
    print()
print('Your total percent was ' + str((score/5) * 100))

    
