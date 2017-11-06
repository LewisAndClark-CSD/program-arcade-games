#This will be a quiz.
question_1 = input("1. What is Master Chief's name? ")
correct = 0
incorrect = 0
if question_1 == "John":
    correct += 1
    print("Correct.")
else:
    print("Incorrect.")
question_2 = int(input("2. What is Master Chief's service tag number? "))
if question_2 == 117:
    correct += 1
    print("Correct.")
else:
    print("Incorrect.")
question_3 = input("3. What is Master Chief's partner's name? ")
if question_3 == "Cortana":
    correct = correct + 1
    print("Correct.")
else:
    print("Incorrect.")
question_4 = input("4. Who is the Master Chief uneasy allies with? ")
if question_4 == "Arbiter":
    correct += 1
    print("Correct.")
else:
    print("Incorrect.")
question_5 = input("5. What is the name of Master Chief's armor? ")
if question_5 == "MJOLNIR":
    correct += 1
    print("Correct.")
else:
    print("Incorrect.")

print("You got", correct, "right.")
print("Your score was", (correct/5)*100)
