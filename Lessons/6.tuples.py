"""
🐍 This Python file serves as a demonstration of tuples in Python.
It includes examples and explanations of how to use tuples for immutable sequences.
"""

# 📋 Example 1: Creating a tuple - immutable sequences
colors = ("red", "green", "blue")
print(colors)

# 📊 Example 2: Accessing elements in a tuple
print("First color:", colors[0])
print("Last color:", colors[-1])

# 🔄 Example 3: Iterating over a tuple
for color in colors:
    print(color)

# 🔍 Example 4: Checking if an item exists in a tuple
if "green" in colors:
    print("Yes, green is in the tuple.")

# 📝 Example 5: Concatenating tuples
numbers = (1, 2, 3)
letters = ('a', 'b', 'c')
combined = numbers + letters
print("Combined tuple:", combined)

# Tasks:
# 😎 Create a tuple of your favorite fruits and print them.
# 📏 Create a tuple of your shoe sizes for different brands and print them.
# 🤔 Create a tuple of prime numbers less than 10 and print them.
# 😄 Create a tuple of your favorite animals and check if "elephant" is in the tuple.
# 🌈 Create two tuples of your favorite colors and concatenate them into a single tuple.
# 🦄 Create a tuple of your favorite sports and print them in reverse order.
# 🎲 Create a tuple of your birth year, month, and day, and print them separately.
# 🌟 Create a tuple of your favorite TV shows and print the length of the tuple.
