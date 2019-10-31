# !/usr/bin/env/ python3
#part 1 
#jacob poncher
#11/15/17

# start a variable at 10
x = 10 

#create a loop to do 9 rows
for i in range(1,10):
        #create a loop to print digits
        for j in range(i):
                #print the variable
                print(x, end=' ')
                #increment the variable
                x= x+1
        #print a new line
        print()