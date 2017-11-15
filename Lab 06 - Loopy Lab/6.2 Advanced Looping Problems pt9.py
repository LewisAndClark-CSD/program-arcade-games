#!/user/bin/env python3
#print 10 *
#Ethan Dall
#11-13-17

"""Print 10 astericts with 10 rows"""

#Do this 10 times
  #Print the # then decrease a number on each new line
  #print a new line

for y in range(10):
    for x in range(y):
        print(' ', end=' ')
    for x in range(10-y):
        print(x, end=' ')
    print()