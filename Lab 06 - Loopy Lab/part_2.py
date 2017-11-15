#!/user/bin/env python3
#part_2.py
#Ethan Dall
#11-14-17

"""User input determines height of box"""

#Ask Question
height = int(input('How tall do you want the box to be? '))

#Top line
print('o'*(height*2))

#colums
for x in range(height-2):
    print('o', ' '*((height*2)-2), 'o',sep='', end='\n')
        
#Bottom line
print('o'*(height*2))