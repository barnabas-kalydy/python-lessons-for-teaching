# Example 1: Basic usage of lambda function
addition = lambda x, y: x + y
print("Result of addition:", addition(3, 5))

# Example 2: Using lambda with map() function
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x ** 2, numbers))
print("Squared numbers:", squared_numbers)

# Example 3: Using lambda with filter() function
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("Even numbers:", even_numbers)

# Example 4: Sorting list of tuples by the second element using lambda
tuples = [(1, 2), (3, 1), (5, 4), (7, 6)]
sorted_tuples = sorted(tuples, key=lambda x: x[1])
print("Sorted tuples by second element:", sorted_tuples)

# Example 5: Using lambda in a list comprehension
doubled_numbers = [(lambda x: x * 2)(num) for num in numbers]
print("Doubled numbers:", doubled_numbers)

# Example 6: Using lambda with reduce() function
from functools import reduce
product = reduce(lambda x, y: x * y, numbers)
print("Product of numbers:", product)

# Example 7: Creating a function that returns a lambda function
def make_incrementer(n):
    return lambda x: x + n

increment_by_5 = make_incrementer(5)
print("Result of increment by 5:", increment_by_5(10))

# Example 8: Using lambda to define simple logic
is_odd = lambda x: True if x % 2 != 0 else False
print("Is 7 odd?", is_odd(7))

# Exercises
# Exercise 1: Write a lambda function to calculate the area of a rectangle.
# Exercise 2: Create a lambda function to check if a number is prime.
# Exercise 3: Write a lambda function to capitalize the first letter of a string.
# Exercise 4: Create a lambda function to reverse a string.
# Exercise 5: Write a lambda function to calculate the average of a list of numbers.
# Exercise 6: Create a lambda function to check if a string is a palindrome.
# Exercise 7: Write a lambda function to check if a number is a perfect square.
# Exercise 8: Create a lambda function to find the factorial of a number.
