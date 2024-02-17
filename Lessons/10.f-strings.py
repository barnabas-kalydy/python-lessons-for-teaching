# Examples and exercises for learning f-strings in Python

# Example 1: Basic usage of f-strings
name = "Alice"
age = 30
print(f"Hello, my name is {name} and I am {age} years old.")

# Example 2: Evaluating expressions inside f-strings
x = 10
y = 20
print(f"The sum of {x} and {y} is {x + y}.")

# Example 3: Using formatting options in f-strings
pi = 3.14159
print(f"Value of pi: {pi:.2f}")

# Example 4: Calling methods inside f-strings
message = "hello"
print(f"Uppercase message: {message.upper()}")

# Example 5: Using dictionary values in f-strings
person = {"name": "Bob", "age": 25}
print(f"Person: {person['name']}, Age: {person['age']}")

# Example 6: Using f-strings in loops
for i in range(1, 4):
    print(f"Current value of i: {i}")

# Example 7: Using f-strings for alignment
for i in range(1, 6):
    print(f"Number: {i:2}")

# Example 8: Using f-strings with multiline strings
name = "Alice"
message = (
    f"Hello, {name},\n"
    f"How are you today?\n"
    f"Have a great day!"
)
print(message)

# Exercises
# Exercise 1: Create an f-string to greet the user with their name.
# Exercise 2: Calculate the area of a circle with radius 5 using an f-string to display the result.
# Exercise 3: Use an f-string to print the current date and time.
# Exercise 4: Create an f-string to display the first and last name of a person.
# Exercise 5: Print a multiplication table using f-strings (with for loop).
# Exercise 6: Format a floating-point number with precision using an f-string.
# Exercise 7: Use an f-string to print a dictionary with its keys and values.
# Exercise 8: Create a multiline string using f-strings to display a poem or a quote.
