#
#!/usr/bin/env python3
 +#Quizz
 +#Jordan Watt
 +#11-3-17
 +
 +"""Create a quiz that is 5 questions long"""
 +
 +#Accumulator for points
 +
 +total = 0
 +
 +#Question 1 [numbers]
 +
 +qOne = int(input('How many bits are in a byte? '))
 +if qOne == 8:
 +    total += 1
 +    print('Correct!')
 +else:
 +    print('EERRNNGGG!!!')
 +print('')
 +
 +#Question 2 [selection]
 +
 +qTwo = input('What is the name of Master Cheifs home planet?\nD-"Eridanus II"\n')
 +if qTwo.lower() == 'c':
 +    total += 1
 +    print('Correct!')
 +else:
 +    print('EERRNNGGG!!!')
 +print('')
 +
 +#Question 3 [text]
 +
 +qThree = input('What is the name of the national anthem? ')
 +if qThree.lower() == 'the star spangled banner':
 +    total += 1
 +    print('Correct!')
 +else:
 +    print('EERRNNGGG!!!')
 +print('')
 +
 +#Question 4 [number]
 +
 +qFour = int(input('"Sally sold seashells by the seashore,\nIf Sally sold seashells by the seashore,\nHow many seashells did sally sell?",\nHow many words start with s? '))
 +if qFour == 11:
 +    total += 1
 +    print('Correct!')
 +else:
 +    print('EERRNNGGG!!!')
 +print('')
 +
 +#Question 5 [text]
 +
 +qFive = input('What is the name of the "Gray Wizard",\nin the Lord of the Rings? ')
 +if qFive.lower() == 'gandalf':
 +    total += 1
 +    print('Correct!')
 +else:
 +    print('EERRNNGGG!!!')
 +print('')
 +
 +#Calculating Percentage
 +
 +perc = (total / 5) * 100
 +print(str(perc) + '%') 
