#!/user/bin/env python3
#loopy lab
#Jake Faucett
#11/16/17
n= int(input('E.g. n = '))

#Variable for spaces
spaces = (n*2) - 2

#print the o times the variable and times 2
print('o' * ((n)*2))

#loop variable -1
for i in range(1, n-1):
    
#print the o's + spaces times and then place another o
    print('o' + (' '*spaces) + 'o')
    
#print the final row of o's times the varaible and 2
print('o'*(n)*2)
