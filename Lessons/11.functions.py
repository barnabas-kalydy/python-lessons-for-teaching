"""
🔧 This Python file serves as a demonstration of functions in Python.
It includes examples and explanations of how to define and use functions.
"""

# 🛠️ Example 1: Basic function definition and call
def greet():
    print("Example 1 - Hello, World!")

greet()

# 📝 Example 2: Function with parameters
def greet_person(name):
    print(f"Example 2 - Hello, {name}!")

greet_person("Alice")

# 🔄 Example 3: Function with return value
def add(a, b):
    return a + b

result = add(3, 5)
print("Example 3 - Sum:", result)

# 💡 Example 4: Function with default parameter
def greet_with_default(name="World"):
    print(f"Example 4 - Hello, {name}!")

greet_with_default()
greet_with_default("Bob")

# 🌟 Example 5: Recursive function
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

print("Example 5 - Factorial of 5:", factorial(5))

# Tasks:
# 🔍 Define a function called 'calculate_area' that takes 'radius' as a parameter and returns the area of a circle.
# 📏 Define a function called 'check_triangle' that takes three parameters 'a', 'b', and 'c' representing the lengths of the sides of a triangle, and calculates its area.
# 🍕 Define a function called 'pizza_party' that takes 'num_people' and 'num_slices_per_person' as parameters and returns the total number of pizza slices needed for a party.
# 🧹 Define a function called 'reverse_string' that takes a string as a parameter and returns the reverse of that string.
# 🎲 Define a function called 'is_prime' that takes a number as a parameter and returns True if it's a prime number, otherwise False.
# 📚 Define a function called 'book_info' that takes 'title', 'author', and 'year' as parameters and prints "The book <title> by <author> was published in <year>."
# 💭 Define a function called 'word_count' that takes a string as a parameter and returns the number of words in that string.
# 🌞 Define a function called 'celsius_to_fahrenheit' that takes 'celsius' as a parameter and returns the equivalent temperature in Fahrenheit.
