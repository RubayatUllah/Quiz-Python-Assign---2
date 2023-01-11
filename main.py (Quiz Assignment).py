# Python Simple Quiz Start 
print("WELCOME TO THE CHESS QUIZ")

# Score
score = 0 

# Question 1 
answer1 = input("1. What is the most IMPORTANT piece in chess? ")
if answer1 == "King" or answer1 == "The King" or answer1 == "king": 
    print("Q1 Answer: " + answer1)
    print("Correct! ")
    score = score + 1 
else:
    print("Incorrect")

# Question 2
answer2 = input("2. What is the most POWERFUL piece in chess? ")
if answer2 == "The Queen" or answer2 == "Queen" or answer2 == "queen": 
    print("Q2 Answer: " + answer2)
    print("Correct!")
    score = score + 1 
else:
    print("Incorrect")

# Question 3
answer3 = input("3. How many small are on a chess board? ")
if answer3 == "64" or answer3 == "sixty four":
    print("Q3 Answer. " + answer3)
    print("Correct!")
    score = score + 1 
else:
    print("Incorrect")

# Question 4
answer4 = input("4. What is the only chess piece that can jump over other pieces? ")
if answer4 == "The Knight" or answer4 == "Horse" or answer4 == "Knight":
    print("Q4 Answer: " + answer4)
    print("Correct!")
    score = score + 1 
else:
    print("Incorrect")

# Fraction to decimal process
fraction = score / 4
percentage = fraction * 100
percentage = "{:.0f}%".format(percentage)

# Output Result of Quiz 
print("YOUUR RESULTS:")
print(str(score) + "/4.")  
print(str(percentage))

# Response to grade
if score == 3 < 4:
    print("Excellent!")
else: 
    print("Try Again!") 