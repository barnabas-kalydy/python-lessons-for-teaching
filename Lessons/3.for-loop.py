"""
🐍 This Python file serves as a demonstration of for loops and forEach loops in Python.
It includes examples and explanations of how to use for loops and forEach loops for iteration.
"""

# 🔄 Example 1: Iterate over a list using a for loop
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    print("Actual number: ", num)

# 🔢 Example 2: Iterate over a range using a for loop
for i in range(5):
    print("Actual i value: ", i)

# 📝 Example 3: Iterate over a string using a for loop
word = "hello"
for char in word:
    print(char)

# 🛤️ Example 4: Iterate over a dictionary using a for loop
person = {"name": "Alice", "age": 30, "city": "New York"}
for key, value in person.items():
    print(key, ":", value)

# 🔄 Example 5: Iterate over a list using a forEach loop (list comprehension)
numbers = [1, 2, 3, 4, 5]
[print(num) for num in numbers]

# Tasks:
# 😎 Write a for loop to print all even numbers from 0 to 10.
# 📏 Write a for loop to double each number in the list [1, 2, 3, 4, 5] and print the result.
# 🤔 Write a for loop to count the number of vowels in the string "programming".
# 😄 Write a for loop to convert each name in the list ["Alice", "Bob", "Charlie"] to uppercase and print them.
# 🌈 Write a for loop to find the sum of all numbers in the list [10, 20, 30, 40, 50].
# 🦄 Write a for loop to concatenate each word in the list ["hello", "world", "python"] and print the result.
# 🎲 Write a for loop to find the maximum number in the list [5, 8, 2, 10, 6].
# 🌟 Write a for loop to print the length of each word in the list ["apple", "banana", "cherry"].
