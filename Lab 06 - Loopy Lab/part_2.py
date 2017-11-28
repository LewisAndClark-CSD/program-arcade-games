#!/usr/bin/env python3
#Lab Part 2
#Bethany DuMontelle
#15 November 2017

#ask user for number of zeros
number = int(input('How many o\'s? '))

#spaces used later
spaces = (number * 2) - 2

#print zeros times number times 2
print('o' * ((number) * 2))

#loop the number of times the user asked - 2 with o's, add the spaces from
#earlier, then add another o
for o1 in range(1, number - 1):
    print('o' + (' ' * spaces) + 'o')

#repeat zeros on bottom
print('o' * ((number) * 2))