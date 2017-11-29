n = int(input("Enter your number of o's: "))

for row in range(n * 2):
    print("o", end = '')
print()

for rowLeft in range(n-1):
    print("o" + " " * ((n*2) -2) + "o")

for rowBottom in range(n * 2):
    print("o", end = '')
