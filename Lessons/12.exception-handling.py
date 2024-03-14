"""
🚨 This Python file serves as a demonstration of exception handling in Python.
It includes examples and explanations of how to handle errors and exceptions.
"""

# Exception Handling in Python

# 🛑 Example 1: Handling ZeroDivisionError
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Example 1 - Cannot divide by zero.")

# 🔍 Example 2: Handling IndexError
try:
    my_list = [1, 2, 3]
    print("Example 2 - Element at index 5:", my_list[5])
except IndexError:
    print("IndexError: Index is out of range.")

# 💡 Example 3: Handling ValueError
try:
    value = int("abc")
    print("Example 3 - Parsed integer:", value)
except ValueError:
    print("ValueError: Cannot convert 'abc' to an integer.")

# 🌟 Example 4: Handling multiple exceptions
try:
    num = 10 / 0
    value = int("abc")
except ZeroDivisionError:
    print("Example 4 - Cannot divide by zero.")
except ValueError:
    print("Example 4 - Cannot convert 'abc' to an integer.")

# 🎉 Example 5: Handling generic exception
try:
    result = 10 / 0
except Exception as e:
    print("Example 5 - An error occurred:", str(e))

# Tasks:
# 📏 Handle a FileNotFoundError when trying to open a non-existent file for reading.
# 🍕 Handle a TypeError when trying to concatenate a string with a number.
# 📊 Handle a KeyError when accessing a non-existent key in a dictionary.
# 💭 Handle an AttributeError when trying to access an attribute of a non-existent object.
# 🚀 Handle a NameError when trying to use a variable that is not defined.
# 📝 Handle a ValueError when trying to convert user input to an integer.
