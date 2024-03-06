# Example 1: Creating a list
numbers = [1, 2, 3, 4, 5]

# Example 2: Accessing elements in a list
print("First element:", numbers[0])
print("Last element:", numbers[-1])

# Example 3: Slicing a list
print("Sliced list:", numbers[2:4])

# Example 4: Modifying elements in a list
numbers[1] = 10
print("Modified list:", numbers)

# Example 5: Appending elements to a list
numbers.append(6)
print("Appended list:", numbers)

# Example 6: Removing elements from a list
removed_element = numbers.pop(2)
print("Removed element:", removed_element)
print("List after removal:", numbers)

# Example 7: Iterating over a list
for number in numbers:
    print(number, end=' ')
print()

# Example 8: List comprehension
squared_numbers = [x ** 2 for x in numbers if x > 3]
print("Squared numbers:", squared_numbers)

# Exercises
# Exercise 1: Create a list of your favorite colors.
# Exercise 2: Access the second element of the list.
# Exercise 3: Slice the list to get the first three elements.
# Exercise 4: Change the third element of the list to a new color.
# Exercise 5: Append a new color to the list.
# Exercise 6: Remove the last color from the list.
# Exercise 7: Iterate over the list and print each color.
# Exercise 8: Create a new list containing the lengths of each color name.
