"""
🐍 This Python file serves as a demonstration of for loops and forEach loops in Python.
It includes examples and explanations of how to use for loops and forEach loops for iteration.
"""

# For Loops

# 🔄 Example 1: Iterate over a list using a for loop
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    print(num)

# 🔢 Example 2: Iterate over a range using a for loop
for i in range(5):
    print(i)

# 📝 Example 3: Iterate over a string using a for loop
word = "hello"
for char in word:
    print(char)

# 🛤️ Example 4: Iterate over a dictionary using a for loop
person = {"name": "Alice", "age": 30, "city": "New York"}
for key, value in person.items():
    print(key, ":", value)

# ForEach Loops

# 🔄 Example 5: Iterate over a list using a forEach loop (list comprehension)
numbers = [1, 2, 3, 4, 5]
[print(num) for num in numbers]

# 🔢 Example 6: Iterate over a range using a forEach loop (list comprehension)
[print(i) for i in range(5)]

# 📝 Example 7: Iterate over a string using a forEach loop (list comprehension)
word = "hello"
[print(char) for char in word]

# 🛤️ Example 8: Iterate over a dictionary using a forEach loop (dictionary comprehension)
person = {"name": "Bob", "age": 25, "city": "London"}
[print(key, ":", value) for key, value in person.items()]

# Tasks:
# 😎 Write a for loop to print all even numbers from 0 to 10.
# 📏 Write a forEach loop to double each number in the list [1, 2, 3, 4, 5] and print the result.
# 🤔 Write a for loop to count the number of vowels in the string "programming".
# 😄 Write a forEach loop to convert each name in the list ["Alice", "Bob", "Charlie"] to uppercase and print them.
# 🌈 Write a for loop to find the sum of all numbers in the list [10, 20, 30, 40, 50].
# 🦄 Write a forEach loop to concatenate each word in the list ["hello", "world", "python"] and print the result.
# 🎲 Write a for loop to find the maximum number in the list [5, 8, 2, 10, 6].
# 🌟 Write a forEach loop to print the length of each word in the list ["apple", "banana", "cherry"].
