# Examples and exercises for learning Python functions

# Example 1: Creating a simple function
def greet():
    print("Hello, welcome!")

# Example 2: Calling a function
greet()

# Example 3: Function with parameters
def greet_user(name):
    print(f"Hello, {name}, welcome!")

# Example 4: Calling a function with arguments
greet_user("Alice")

# Example 5: Function with return value
def add_numbers(x, y):
    return x + y

# Example 6: Calling a function and using its return value
result = add_numbers(5, 3)
print("Sum:", result)

# Example 7: Default parameter values
def greet_person(name="Guest"):
    print(f"Hello, {name}, welcome!")

# Example 8: Function with variable number of arguments
def sum_numbers(*args):
    total = 0
    for num in args:
        total += num
    return total

# Examples
greet_person()  # Using default parameter
greet_person("Bob")
print("Sum of numbers:", sum_numbers(1, 2, 3, 4, 5))

# Exercises
# Exercise 1: Create a function to calculate the area of a rectangle given its
# length and width.
# Exercise 2: Write a function to check if a number is even or odd.
# Exercise 3: Create a function to find the maximum of three numbers.
# Exercise 4: Write a function to check if a string is a palindrome.
# Exercise 5: Create a function to generate Fibonacci series up to n terms.
# Exercise 6: Write a function to convert Celsius to Fahrenheit.
# Exercise 7: Create a function to find the factorial of a number.
# Exercise 8: Write a function to reverse a list.
