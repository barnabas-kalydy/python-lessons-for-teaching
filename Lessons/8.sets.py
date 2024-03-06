# Example 1: Creating a set
fruits = {"apple", "banana", "orange", "apple"}
print("Set of fruits:", fruits)  # Duplicate elements are automatically removed

# Example 2: Adding elements to a set
fruits.add("grape")
print("Set after adding grape:", fruits)

# Example 3: Removing elements from a set
fruits.remove("banana")
print("Set after removing banana:", fruits)

# Example 4: Checking membership in a set
print("Is 'orange' in the set?", "orange" in fruits)

# Example 5: Set operations
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

print("Union of sets:", set1 | set2)
print("Intersection of sets:", set1 & set2)
print("Difference of sets:", set1 - set2)

# Example 6: Iterating over a set
for fruit in fruits:
    print(fruit)

# Example 7: Frozenset -> can't remove or add elements
frozen_set = frozenset([1, 2, 3, 4])
print("Frozen set:", frozen_set)

# Example 8: Set comprehension
squared_numbers = {x ** 2 for x in range(1, 6)}
print("Squared numbers set:", squared_numbers)

# Exercises
# Exercise 1: Create a set containing your favorite colors.
# Exercise 2: Add a new color to the set.
# Exercise 3: Remove a color from the set.
# Exercise 4: Check if "red" is in the set.
# Exercise 5: Create another set of colors and find their union.
# Exercise 6: Find the common colors in both sets.
# Exercise 7: Create a frozenset of numbers and try to add a new element (observe the error).
# Exercise 8: Create a set of even numbers less than 10 using set comprehension.
