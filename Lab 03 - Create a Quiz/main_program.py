print("Time for a Quiz!")
print("")
total= 0

question_one = int(input("1. What is my favorite number? "))
if question_one == 8:
  total= total+1
  print("Correct!")
else:
  print("Incorrect.")
print("")

question_two = input("2. What did Jack break when he fell down? ")
if question_two == "his crown":
  print("Correct!")
  total= total+1
else:
  print("Incorrect.")
print("")
print("3. What do your eyes do?")
answer_one= "1. smell"
answer_two= "2. see"
answer_three= "3. hear"
print(answer_one)
print(answer_two)
print(answer_three)
question_three= input("? ")
if question_three == "see":
  print("Correct!")
  total= total+1
else:
  print("Incorrect!")
print("")

question_four= input("4. Is this the fourth question? ")
if question_four == "yes":
  print("Correct!")
  total= total+1
else:
  print("Incorrect.")
print("")

question_five= input("What is the radius of the sun in miles? ")
if question_five== "432,288":
  print("Correct!")
  total= total+1
else:
  print("Incorrect.")
print("")

print("Wow! You got", total, "questions right!")
print("That means your total score is", (100*(total/5)),"percent!")
print("")
