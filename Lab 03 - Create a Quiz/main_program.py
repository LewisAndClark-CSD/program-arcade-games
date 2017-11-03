#
print("Welcome to Lyles' Quiz!")
result = 0
question1 = print('Question 1: What is 4 + 2?')
print('A. 4')
print('B. 2')
print('C. 6')
answer1 = input('Answer: ')
if answer1 == 'C':
    print('Correct')
    result = result + 1
else:
    print('Incorrect')


    
question2 = print('Question 2: What does USA stand for?')
print('A. United States America')
print('B. United States of America')
print('C. Undergoing Software Adaptations')
answer2 = input('Answer: ')
if answer2 == 'B':
    print('Correct')
    result = result + 1
else:
    print('Incorrect')
question3 = print("Question 3: Who is North Korea's leader?: ")
print('A. Kim Jong-un')
print('B. Donald Trump')
print('C. Trick Question?')
answer3 = input('Answer: ')
if answer3 == 'A':
    print('Correct')
    result = result + 1
else:
    print('Incorrect')
question4 = print('What is 43 times 2?: ')
print('A. 87')
print('B. 85')
print('C. 86')
answer4 = input('Answer: ')
if answer4 == 'C':
    print('Correct')
    result = result + 1
else:
    print('Incorrect')
question5 = print('Which actor was in "The Breakfast Club"?')
print('A. Judd Nelson')
print('B. Brad Pitt')
print('C. Megan Fox')
answer5 = input('Answer: ')
if answer5 == 'A':
    print('Correct')
    result = result + 1
else:
    print('Incorrect')
print('Total Answers Correct:', result)
