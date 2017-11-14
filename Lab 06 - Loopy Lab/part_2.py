#!/user/bin/env python3
#part_2.py
#Ethan Dall
#11-14-17

"""User input determines height of box"""

#Ask Question
height = int(input('How tall do you want the box to be? '))

#Top line
print('o'*10)

#colums
for x in range(height):
    print('o', ' '*6, 'o', end='\n')
        
#Bottom line
print('o'*10)