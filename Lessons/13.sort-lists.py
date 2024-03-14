"""
🔍 This Python file serves as a demonstration of sorting lists in Python.
It includes examples and explanations of how to use built-in sorting functions and custom sorting functions.
"""

# Sorting Lists

# 🎯 Example 1: Sorting a list of numbers in ascending order
numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5]
sorted_numbers = sorted(numbers)
print("Sorted numbers:", sorted_numbers)

# 📚 Example 2: Sorting a list of strings in alphabetical order
fruits = ["apple", "banana", "orange", "grape", "kiwi"]
sorted_fruits = sorted(fruits)
print("Sorted fruits:", sorted_fruits)

# 🌟 Example 3: Sorting a list of tuples based on a specific element
students = [("Alice", 22), ("Bob", 18), ("Charlie", 25), ("David", 20)]
sorted_students_by_age = sorted(students, key=lambda x: x[1])  # Sorting based on age (second element)
print("Sorted students by age:", sorted_students_by_age)

# ✨ Example 4: Sorting a list of dictionaries based on a specific key
employees = [
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 25},
    {"name": "Charlie", "age": 35}
]
sorted_employees_by_age = sorted(employees, key=lambda x: x["age"])
print("Sorted employees by age:", sorted_employees_by_age)

# Tasks:
# 💡 Sort the list of temperatures [32, 25, 18, 27, 30] in descending order.
# 🚀 Sort the list of strings ["apple", "Orange", "banana", "Kiwi"] ignoring case sensitivity.
# 🎩 Sort the list of tuples [(3, 2), (1, 5), (4, 1), (2, 3)] based on the sum of their elements.
# 🍕 Sort the list of dictionaries based on the length of the "name" key's value.
# 🎸 Sort the list of numbers [100, 23, 45, 78, 95] and find the second highest number.
# 🏆 Sort the list of strings ["python", "java", "C++", "javascript"] based on their lengths in ascending order.
# 🍭 Sort the list of lists [[3, 1, 4], [1, 5, 9], [2, 6, 5], [3, 5, 8]] based on the sum of elements in each list.
# 🎨 Sort the list of strings ["apple", "banana", "cherry", "date"] based on the number of vowels in each word.
