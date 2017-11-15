#Do an input statement to make box any size user wants
n = int(input("Desired size: "))

#Variable for spaces
spaces = (n*2) - 2

#print the o times the variable and times 2
print('o' * ((n)*2))

#loop variable - 1
for i in range(1, n-1):
    
#print the o's + spaces times and then plus another o    
    print('o' + (' '*spaces) + 'o')
    
#print the final row of o's times the variable and 2.    
print('o'*(n)*2)
