# !/usr/bin/env python3
#Lab 6 part two
#Lauren Boehme
#11/15/17

numb = int(input("Enter number of o's: "))
spaces= (numb*2) - 2
print('o' * ((numb) * 2))
for i in range(1, numb -1):
    print('o' + (' '*spaces) + 'o')
print('o'*(numb)*2)
