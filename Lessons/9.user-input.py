# Example 1: Getting user input for a string
name = input("Enter your name: ")
print("Hello,", name)

# Example 2: Getting user input for an integer
age = int(input("Enter your age: "))
print("You are", age, "years old.")

# Example 3: Getting user input for a float
height = float(input("Enter your height in meters: "))
print("Your height is", height, "meters.")

# Example 4: Getting multiple inputs using split()
numbers = input("Enter two numbers separated by space: ").split(",")
num1, num2 = map(int, numbers)
print("Sum of the numbers:", num1 + num2)

# Example 5: Getting user input with a prompt
password = input("Enter your password: ")

# Example 6: Handling user input as a list
items = []
isRunning = True
while isRunning:
    item = input("Enter an item (or 'done' to finish): ")
    if item == 'done':
        isRunning = False
    items.append(item)
print("Items entered:", items)

# Example 7: Using eval() to evaluate user input
expression = input("Enter an arithmetic expression: ")
result = eval(expression)
print("Result:", result)

# Example 8: Error handling for invalid input
try:
    num = int(input("Enter a number: "))
    print("You entered:", num)
except ValueError:
    print("Invalid input. Please enter a valid number.")

# Exercises
# Exercise 1: Ask the user for their favorite color.
# Exercise 2: Prompt the user for their birth year and calculate their age.
# Exercise 3: Get the radius of a circle from the user and calculate its area.
# Exercise 4: Ask the user for their email address and validate its format.
# Exercise 5: Take a list of numbers from the user and find their sum.
# Exercise 6: Ask the user for their username and check if it contains any special characters.
# Exercise 7: Prompt the user for a mathematical expression and evaluate it.
# Exercise 8: Handle the scenario where the user enters a non-numeric value when expecting a number.
