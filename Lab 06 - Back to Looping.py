'''
for i in range(10):
  print("", end = "* ")
print()
for i in range(5):
  print("", end = "* ")
print()
for i in range(20):
  print("", end = "* ")


for i in range(10):
    for row in range(10):
        print("*", end = " ")
    print()
    
for i in range(10):
    for j in range(i+1):
        print(j, end = " ")
    print()
    
for i in range(10):
    for space in range(i):
        print(" ",end= " ")
    for digit in range(10-i):
        print(digit,end= " ")
    print()
     
for i in range(1, 10):
    for digit in range(1, 10):
        print(digit * i, end = " ")
    print()
'''

for i in range(10):
    for j in range(10-i):
        print (" ",end=" ")
    for j in range(1,i+1):
        print (j,end=" ")
    for j in range(i-1,0,-1):
        print (j,end=" ")
    print()
