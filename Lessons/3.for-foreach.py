# Example 1: Basic for loop
for i in range(5):
    print(i, end=' ')
print()

# Example 2: Iterating over a list using foreach loop
fruits = ["apple", "banana", "orange", "grape"]
for fruit in fruits:
    print(fruit)

# Example 3: Iterating over a dictionary using foreach loop
person = {"name": "Alice", "age": 30, "city": "New York"}
for key, value in person.items():
    print(key + ":", value)

two_d_array = [
    [1, 3, 4, 5],
    [1, 5, 23, 23]
]
# Example 4: Nested for loop
for i in range(len(two_d_array)):
    for j in range(len(two_d_array[0])):
        print(two_d_array[i][j])

# Tasks
# Task 1: Print numbers from 1 to 10 using a for loop.
# Task 2: Calculate the sum of elements in a list using a foreach loop.
# Task 3: Find the maximum element in a list using a for loop.
# Task 4: Iterate over a string and count the number of vowels.
# Task 5: Print multiplication table of a given number using a for loop.
# Task 6: Calculate the factorial of a number using a foreach loop.
# Task 7: Iterate over a list of tuples and print each element.
# Task 8: Generate a pattern using nested for loops.
