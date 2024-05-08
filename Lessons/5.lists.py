"""
🐍 This Python file serves as a demonstration of lists in Python.
It includes examples and explanations of how to use lists for storing and manipulating data.
"""

# 📋 Example 1: Creating a list
fruits = ["apple", "banana", "cherry"]
print(fruits)

# 📊 Example 2: Accessing elements in a list
print("First fruit:", fruits[0])
print("Last fruit:", fruits[-1])

# 🔄 Example 3: Iterating over a list
for fruit in fruits:
    print(fruit)

# 🔍 Example 4: Checking if an item exists in a list
if "banana" in fruits:
    print("Yes, banana is in the list.")

# 📝 Example 5: Modifying elements in a list
fruits[1] = "grape"
print("Modified list:", fruits)

# 📦 Example 6: Adding elements to a list
fruits.append("orange")
print("After appending:", fruits)

# ➖ Example 7: Removing elements from a list
fruits.remove("cherry")
print("After removing:", fruits)

# Tasks:
# 😎 Create a list of your favorite movies and print them.
# 📏 Create a list of your friends' names and print the length of the list.
# 🤔 Create a list of numbers from 1 to 10 and print the sum of all elements.
# 😄 Create a list of your favorite colors and print the first and last colors.
# 🌈 Create a list of programming languages you want to learn and check if "Python" is in the list.
# 🦄 Create a list of your favorite books and add a new book to the list.
# 🎲 Create a list of your favorite foods and remove one food item from the list.
# 🌟 Create a list of your hobbies and print them in reverse order.
