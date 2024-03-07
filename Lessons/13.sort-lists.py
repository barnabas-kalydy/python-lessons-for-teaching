# Example 1: Sorting a list of numbers
numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
sorted_numbers = sorted(numbers)
print("Sorted numbers:", sorted_numbers)

# Example 2: Sorting a list in reverse order
reverse_sorted_numbers = sorted(numbers, reverse=True)
print("Reverse sorted numbers:", reverse_sorted_numbers)

# Example 3: Sorting a list in place
print("Original list:", numbers)
numbers.sort()
print("Sorted list in place:", numbers)

# Example 4: Sorting a list of strings
words = ["apple", "banana", "orange", "grape", "cherry"]
sorted_words = sorted(words)
print("Sorted words:", sorted_words)

# Example 5: Sorting a list of tuples by a specific element
students = [("Alice", 22), ("Bob", 20), ("Charlie", 25)]
sorted_students = sorted(students, key=lambda x: x[1])
print("Sorted students by age:", sorted_students)

# Example 6: Sorting a list of dictionaries by a specific key
people = [{"name": "Alice", "age": 22}, {"name": "Bob", "age": 20}, {"name": "Charlie", "age": 25}]
sorted_people = sorted(people, key=lambda x: x["age"])
print("Sorted people by age:", sorted_people)

# Example 7: Sorting a list of objects by a specific attribute
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

people_objects = [Person("Alice", 22), Person("Bob", 20), Person("Charlie", 25)]
sorted_people_objects = sorted(people_objects, key=lambda x: x.age)
print("Sorted people objects by age:")
for person in sorted_people_objects:
    print(person.name, person.age)

# Example 8: Sorting a list of strings with custom sorting criteria
words = ["banana", "apple", "Orange", "Grape", "cherry"]
sorted_words_custom = sorted(words, key=lambda x: x.lower())
print("Case-insensitive sorted words:", sorted_words_custom)

# Exercises
# Exercise 1: Sort the given list of numbers in descending order.
# Exercise 2: Sort the list of strings based on their length in ascending order.
# Exercise 3: Sort the list of tuples based on the sum of their elements.
# Exercise 4: Sort the list of dictionaries based on the value of a nested key.
# Exercise 5: Sort the list of objects based on multiple attributes.
# Exercise 6: Sort the list of strings based on the number of vowels in each string.
# Exercise 7: Sort the list of tuples based on the product of their elements.
# Exercise 8: Sort the list of strings based on the presence of a specific character.
