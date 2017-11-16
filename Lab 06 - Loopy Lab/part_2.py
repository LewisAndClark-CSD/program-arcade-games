#Chapter 6 Lab 2
number = int(input("Number = "))
letter = "o"
spaces = " " * ((number * 2) - 3)
for row in range(number):
    print(letter*2, end="")
print()
for row in range(number-2):
    print(letter, spaces, end="")
    print(letter)
for row in range(number):
    print(letter*2, end="")
print()
