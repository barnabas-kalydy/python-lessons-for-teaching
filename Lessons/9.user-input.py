"""
💬 This Python file serves as a demonstration of handling user input in Python.
It includes examples and explanations of how to prompt users for input and process their responses.
"""

# User Input in Python

# 📥 Example 1: Basic input prompt
name = input("Example 1 - Please enter your name: ")
print("Hello,", name + "!")

# 📝 Example 2: Integer input
age = int(input("Example 2 - Please enter your age: "))
print("You are", age, "years old.")

# 🍕 Example 3: Floating-point input
pizza_price = float(input("Example 3 - Enter the price of a pizza: "))
print("The price of the pizza is $", pizza_price)

# 🔢 Example 4: Multiple inputs
num1, num2 = input("Example 4 - Enter two numbers separated by a space: ").split()
num1 = int(num1)
num2 = int(num2)
print("Sum of the numbers:", num1 + num2)

# 🎲 Example 5: Evaluating user input
guess = input("Example 5 - Guess a number between 1 and 10: ")
if guess == "7":
    print("Congratulations! You guessed correctly.")
else:
    print("Sorry, better luck next time!")

# Tasks:
# 🍔 Prompt the user to enter their favorite food and print it.
# 🎸 Ask the user for their favorite music genre and print it.
# 📅 Ask the user to enter their birth year and calculate their age.
# 🌞 Ask the user to enter their current temperature in Celsius and convert it to Fahrenheit.
# 📚 Ask the user for their favorite book genre and print it.
# 🔑 Prompt the user to enter a password and check if it meets the criteria of at least 8 characters.
# 🎨 Ask the user to enter their favorite color and print it.
# 💭 Ask the user to enter a sentence and count the number of words in it.
