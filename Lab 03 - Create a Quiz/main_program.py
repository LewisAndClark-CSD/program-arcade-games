#!/user/bin/env python3
#Create a Quiz
#Christian Groves
#11-3-17
counter = 0
print('Pop Quiz')
answer1 = input('''What is the largest free to play game on PC: ''')
if answer1.lower() == 'warframe':
    print('Correct')
    counter += 1
else:
    print('Incorrect')

answer2 = input('''When comes after 20013: ''')
if answer2 == '20014':
    print('Correct')
    counter += 1
else:
    print('Incorrect')
    
answer3 = input('''What is the powerhouse of the cell: ''')
if answer3.lower() == 'mitochondria':
    print('Correct')
    counter += 1
else:
    print('Incorrect')

answer4 = input('''What is the answer to the universe: ''')
if answer4 == '42':
    print('Correct')
    counter += 1
else:
    print('Incorrect')

print('A. You')
print('B. Bill Gates')
print('C. Rick and Morty')    
answer5 = input('''Who is dead: ''')

if answer5.lower() == 'b':
    print('Correct')
    counter += 1
else:
    print('Incorrect')
if counter >= 4:
    print("Congrats, you didn't fail")
    print('Your score is ' + str(counter * 20) +'.0 percent.')
else:
    print('Your score was terrible only a ' + str(counter * 20) + '.0 percent.')