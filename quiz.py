print("🎯 Welcome to Quiz Game")

score = 0

# Question 1
print("\n1. What is the capital of India?")
print("a) Mumbai")
print("b) Delhi")
print("c) Pune")
print("d) Goa")

answer = input("Enter your answer: ")

if answer == "b":
    print("Correct ✅")
    score += 1
else:
    print("Wrong ❌")

# Question 2
print("\n2. Which language is used in Python?")
print("a) English")
print("b) Java")
print("c) Python")
print("d) C++")

answer = input("Enter your answer: ")

if answer == "c":
    print("Correct ✅")
    score += 1
else:
    print("Wrong ❌")

# Final Score
print("\n🎉 Quiz Finished")
print("Your Score is:", score)