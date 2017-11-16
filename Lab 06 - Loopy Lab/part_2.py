#!/usr/bin/env/ python3
#part 1 
#jacob poncher
#11/15/17
# input statement for number 
number =  int(input('number: '))
# print o times 2 for the input 
print('o'* (number*2 + 2  ))
# loop to print 2 times the number of o 
for i in range(number - 2):
    print('o' + ' '*(number*2) + 'o')
print('o'* (number*2 + 2))