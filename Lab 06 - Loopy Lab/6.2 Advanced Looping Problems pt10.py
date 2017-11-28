#!/user/bin/env python3
#print 10 *
#Ethan Dall
#11-13-17

"""Print multiples of each number in 9 rows"""

#Do this 9 times
  #Print the # then increases by the multiple on each new line
  #print a new line

for y in range(1,10):
    for x in range(1,10):
        if (y*x) < 10:
            print(y*x, end='  ')
        else:
            print(y*x, end=' ')
    print()