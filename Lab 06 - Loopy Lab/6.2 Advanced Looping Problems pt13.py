#!/user/bin/env python3
#print 10 *
#Ethan Dall
#11-13-17

"""Print numbers counting up then down in rows"""

#Do 9 times starting at 1
for y in range(1, 10):
    
    #loop to print spaces
    for x in range(9 - y):
        print(' ', end=' ')
        
    #loop to print digits
    for x in range(y):
        print(x+1, end=' ')
    
    #loop to print digits2
    for x in range(y, 1, -1):
        print(x-1, end=' ')
    
    #print a new line
    print()

#prints 8 times from 8
for y in range(9, 1, -1):
    
    #loop to print spaces
    for x in range(10-y):
        print(' ', end=' ')
    
    #loop prints digits
    for x in range(1, y):
        print(x, end=' ')
    
    #loop prints digits2
    for x in range(y-1, 1, -1):
        print(x-1, end=' ')
        
    #print a new line
    print()