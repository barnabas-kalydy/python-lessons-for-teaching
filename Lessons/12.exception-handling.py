# Examples and exercises for learning error handling in Python

# Example 1: Handling division by zero error
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Error: Division by zero")

# Example 2: Handling type error
try:
    num = int("abc")
except ValueError:
    print("Error: Invalid conversion")

# Example 3: Using try-except-else block
try:
    num = int(input("Enter a number: "))
except ValueError:
    print("Error: Invalid input")
else:
    print("You entered:", num)

# Example 4: Handling multiple exceptions
try:
    file = open("nonexistent.txt", "r")
    data = file.read()
    file.close()
except FileNotFoundError:
    print("Error: File not found")
except IOError:
    print("Error: Unable to read file")

# Example 5: Handling exceptions with finally block
try:
    num = 10 / 0
except ZeroDivisionError:
    print("Error: Division by zero")
finally:
    print("Execution complete")

# Example 6: Raising exceptions
def divide(x, y):
    if y == 0:
        raise ValueError("Division by zero")
    return x / y

try:
    result = divide(10, 0)
except ValueError as e:
    print("Error:", e)

# Example 7: Custom exception
class MyError(Exception):
    pass

try:
    raise MyError("An error occurred")
except MyError as e:
    print("Custom error:", e)

# Example 8: Assertion error
num = 10
try:
    assert num > 100
except AssertionError:
    print("Assertion failed")

# Exercises
# Exercise 1: Handle the FileNotFoundError exception and print a custom message.
# Exercise 2: Write a function to divide two numbers and handle the ZeroDivisionError.
# Exercise 3: Create a custom exception called NameTooShortError and raise it when a name is less than 3 characters.
# Exercise 4: Use assert statement to check if a number is positive, if not raise an AssertionError.
# Exercise 5: Handle the IndexError exception when accessing elements in a list and print a custom message.
# Exercise 6: Write a function to open a file, read its contents, and close it. Handle all possible exceptions.
# Exercise 7: Raise a ValueError if a user enters a negative number in input.
# Exercise 8: Use try-except block to handle the ValueError when converting user input to an integer.
