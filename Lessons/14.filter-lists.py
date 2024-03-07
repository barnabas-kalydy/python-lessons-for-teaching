# Example 1: Filtering even numbers from a list
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("Even numbers:", even_numbers)

# Example 2: Filtering strings based on length
words = ["apple", "banana", "orange", "grape", "cherry"]
short_words = list(filter(lambda x: len(x) < 6, words))
print("Short words:", short_words)

# Example 3: Filtering positive numbers
positive_numbers = list(filter(lambda x: x > 0, numbers))
print("Positive numbers:", positive_numbers)

# Example 4: Filtering tuples based on a condition
tuples = [(1, 2), (3, 4), (5, 6), (7, 8)]
filtered_tuples = list(filter(lambda x: sum(x) > 5, tuples))
print("Filtered tuples:", filtered_tuples)

# Example 5: Filtering dictionaries based on a condition
people = [{"name": "Alice", "age": 25}, {"name": "Bob", "age": 30}, {"name": "Charlie", "age": 20}]
filtered_people = list(filter(lambda x: x["age"] < 30, people))
print("Filtered people:", filtered_people)

# Example 6: Filtering objects based on an attribute
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

people_objects = [Person("Alice", 25), Person("Bob", 30), Person("Charlie", 20)]
filtered_people_objects = list(filter(lambda x: x.age < 30, people_objects))
print("Filtered people objects:")
for person in filtered_people_objects:
    print(person.name, person.age)

# Example 7: Filtering strings containing a specific character
filtered_words = list(filter(lambda x: 'a' in x, words))
print("Words containing 'a':", filtered_words)

# Example 8: Filtering based on custom criteria
numbers2 = [-1, 2, -3, 4, -5, 6, -7, 8, -9, 10]
filtered_numbers2 = list(filter(lambda x: x > 0 and x % 2 == 0, numbers2))
print("Positive even numbers:", filtered_numbers2)

# Exercises
# Exercise 1: Filter the given list of numbers to get only the multiples of 3.
# Exercise 2: Filter the list of strings to get only the words starting with 'b'.
# Exercise 3: Filter the list of tuples to get only the tuples where both elements are even numbers.
# Exercise 4: Filter the list of dictionaries to get only the people whose age is less than 25.
# Exercise 5: Filter the list of objects to get only the people whose name starts with 'A'.
# Exercise 6: Filter the list of strings to get only the palindromes.
# Exercise 7: Filter the list of tuples to get only the tuples where the second element is greater than the first.
# Exercise 8: Filter the list of numbers to get only the primes.
