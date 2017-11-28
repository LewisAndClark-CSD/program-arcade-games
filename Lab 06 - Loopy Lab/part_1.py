#!/user/bin/env python3
#part_1.py
#Ethan Dall
#11-14-17

"""print numbers 10-54 growing"""

#Accumulator
grow = 10

#Do 9 times starting at 1
for rows in range(9):
    
    #loop to print digits
    for x in range(rows+1):
        print(grow, end=' ')
        grow += 1
        
    #print new line
    print()