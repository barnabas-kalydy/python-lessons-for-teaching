"""
💡 This Python file serves as a demonstration of sets in Python.
It includes examples and explanations of how to use sets for storing unique elements.
"""

# 🔄 Example 1: Creating a set
my_set = {1, 2, 3, 4, 5, 5, 5}
print("Example 1 - Set elements:", my_set)

# ➖ Example 2: Adding elements to a set
my_set.add(6)
print("Example 2 - After adding 6:", my_set)

# ➖ Example 3: Removing elements from a set
my_set.remove(3)
print("Example 3 - After removing 3:", my_set)

# ✨ Example 4: Set operations - Union
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
union_set = set1.union(set2)
print("Example 4 - Union of sets:", union_set)

# 🎈 Example 5: Set operations - Intersection
intersection_set = set1.intersection(set2)
print("Example 5 - Intersection of sets:", intersection_set)

# Tasks:
# 🎯 Create a set containing your favorite colors.
# 🔍 Add a new color to the set and print the updated set.
# 🗑️ Remove a color from the set and print the updated set.
# 🧹 Create another set containing colors of the rainbow:
#    {"red", "orange", "yellow", "green", "blue", "indigo", "violet"} and check if "green" is in the set.
# ✨ Perform a union operation on both sets and print the result.
# 🌈 Perform an intersection operation on both sets and print the result.
# 🎲 Check if your favorite color set is a subset of the rainbow color set.
# 💬 Ask the user to enter their favorite fruit and add it to the favorite color set.
