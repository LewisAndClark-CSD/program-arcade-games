#!/user/bin/env python3
#loopy lab
#Jake Faucett
#11/16/17

#Start at 10 for the triangle
begin = 10
#Do this 9 times
for row in range(9):
    # Loop to print the digits
    for j in range(row +1):
        #prints the variable
        print(begin, end= ' ')
        #Adds 1 to start so the line is higher
        begin += 1
    #Prints a new line 
    print()