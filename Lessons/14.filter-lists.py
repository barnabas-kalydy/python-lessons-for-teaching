"""
🔍 This Python file serves as a demonstration of filtering lists in Python.
It includes examples and explanations of how to use built-in filtering functions and list comprehensions for filtering.
"""

# Filtering Lists

# 🎯 Example 1: Filtering even numbers from a list using list comprehension
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = [num for num in numbers if num % 2 == 0]
print("Even numbers:", even_numbers)

# 📚 Example 2: Filtering strings starting with 'A' from a list using list comprehension
names = ["Alice", "Bob", "Charlie", "David", "Anna", "Andrew"]
names_starting_with_a = [name for name in names if name.startswith('A')]
print("Names starting with 'A':", names_starting_with_a)

# 🌟 Example 3: Filtering positive numbers from a list using filter() function
numbers = [-2, -1, 0, 1, 2, 3, 4, 5]
positive_numbers = list(filter(lambda x: x > 0, numbers))
print("Positive numbers:", positive_numbers)

# ✨ Example 4: Filtering dictionaries based on a specific condition using list comprehension
students = [
    {"name": "Alice", "age": 22},
    {"name": "Bob", "age": 18},
    {"name": "Charlie", "age": 25},
    {"name": "David", "age": 20}
]
adult_students = [student for student in students if student['age'] >= 18]
print("Adult students:", adult_students)

# Tasks:
# 💡 Filter numbers greater than 50 from the list [20, 35, 50, 65, 80, 90].
# 🚀 Filter strings containing the letter 'o' from the list ["apple", "banana", "orange", "grape", "kiwi"].
# 🎩 Filter tuples with even sums from the list [(3, 4), (1, 5), (6, 2), (2, 3)].
# 🍕 Filter dictionaries with ages greater than or equal to 30 from the list of employees (create the list first).
# 🎸 Filter strings longer than 5 characters from the list ["python", "java", "C++", "javascript"].
# 🏆 Filter lists containing the number 5 from the list of lists [[3, 5, 4], [1, 6, 7], [9, 2, 8], [5, 4, 2]].
# 🍭 Filter strings containing at least two vowels from the list ["apple", "banana", "cherry", "date"].
# 🎨 Filter tuples where the first element is greater than the second from the list [(3, 2), (1, 5), (4, 1), (2, 3)].
