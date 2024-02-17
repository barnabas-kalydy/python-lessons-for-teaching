# Examples and exercises for learning tuples in Python

# Example 1: Creating a tuple
person = ("John", 30, "New York")

# Example 2: Accessing elements in a tuple
print("Name:", person[0])
print("Age:", person[1])
print("City:", person[2])

# Example 3: Unpacking a tuple
name, age, city = person
print("Unpacked variables:", name, age, city)

# Example 4: Tuples are immutable
# Uncomment the code below to see the error
# person[1] = 40

# Example 5: Combining tuples
person_info = person + ("Engineer",)
print("Combined tuple:", person_info)

# Example 6: Repeating elements in a tuple
numbers = (1, 2) * 3
print("Repeated tuple:", numbers)

# Example 7: Counting occurrences of an element in a tuple
letters = ('a', 'b', 'c', 'a', 'b')
print("Count of 'a':", letters.count('a'))

# Example 8: Finding the index of an element in a tuple
print("Index of 'c':", letters.index('c'))

# Exercises
# Exercise 1: Create a tuple containing your name, age, and country.
# Exercise 2: Access the second element of the tuple.
# Exercise 3: Unpack the tuple into separate variables.
# Exercise 4: Try to modify an element in the tuple and observe the error.
# Exercise 5: Combine two tuples into a new tuple.
# Exercise 6: Repeat a tuple three times.
# Exercise 7: Count the number of occurrences of a specific element in the tuple.
# Exercise 8: Find the index of a specific element in the tuple.
