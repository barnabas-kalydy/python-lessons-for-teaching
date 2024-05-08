"""
🔍 This Python file serves as a demonstration of lambda functions in Python.
It includes examples and explanations of how to use lambda functions for simple, one-line operations.
"""

# 🎯 Example 1: Adding two numbers using lambda function
addition = lambda x, y: x + y
print("Addition:", addition(3, 5))

# 📚 Example 2: Multiplying a number by itself using lambda function
square = lambda x: x * x
print("Square:", square(4))

# 🌟 Example 3: Checking if a number is even using lambda function
is_even = lambda x: x % 2 == 0
print("Is 7 even?", is_even(7))

# ✨ Example 4: Sorting a list of tuples based on the second element using lambda function
students = [("Alice", 22), ("Bob", 18), ("Charlie", 25), ("David", 20)]
sorted_students_by_age = sorted(students, key=lambda x: x[1])
print("Sorted students by age:", sorted_students_by_age)

# Tasks:
# 💡 Create a lambda function to calculate the square root of a number.
# 🚀 Create a lambda function to convert a string to uppercase.
# 🎩 Create a lambda function to check if a string starts with a vowel.
# 🍕 Create a lambda function to check if a number is prime.
# 🏆 Create a lambda function to sort a list of dictionaries based on a specific key.
# 🍭 Create a lambda function to concatenate two strings with a space in between.
# 🎨 Create a lambda function to remove duplicates from a list.
