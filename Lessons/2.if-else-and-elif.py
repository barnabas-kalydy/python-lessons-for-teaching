"""
🚥 This Python file serves as a demonstration of conditional statements in Python.
It includes examples and explanations of if statements, if-else statements, if-elif-else statements, and ternary operators.
"""

# If Statements
# 🛑 Example 1: Simple if statement
age = 18
if age >= 18:
    print("You are old enough to vote.")

# If-Else Statements
# 🚦 Example 2: If-else statement
temperature = 25
if temperature > 30:
    print("It's hot outside!")
else:
    print("It's not too hot outside.")

# If-Elif-Else Statements
# 🌞 Example 3: If-elif-else statement
time_of_day = "morning"
if time_of_day == "morning":
    print("Good morning!")
elif time_of_day == "afternoon":
    print("Good afternoon!")
else:
    print("Good evening!")

# Ternary Operator
# ➕ Example 4: Ternary operator
number = 10
result = "Even" if number % 2 == 0 else "Odd"
print("Number is:", result)

# Tasks:
# 😎 Write an if-else statement to check if your age is above 25 or not.
# 🎉 Write an if-elif-else statement to determine which season is it based on the current month.
# 💼 Write a ternary operator to check if the year 2024 is a leap year or not.
# 😄 Write an if-else statement to check if a password "P@ssw0rd" meets these criteria:
#	- length > 8, contains uppercase, contains lowercase, and contains special characters.
# 🍂 Write an if-else statement to check if the temperature 22 is within the comfortable range (20-25).
# 🦄 Write an if-else statement to determine if the year 2100 is a century year or not (ending with 00).
# 🎭 Write a ternary operator to determine if 532 is divisible by both 5 and 7.
# 🌈 Write an if-else statement to check if your favorite color is blue or not.
