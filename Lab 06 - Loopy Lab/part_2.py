#Chapter 6 Lab 2
number = int(input("Number = "))
letter = "o"
for row in range(number):
    print(letter*2, end="")
print()
for row in range(number-2):
    print(letter)              
for row in range(number):
    print(letter*2, end="")
print()
