"""
🎨 This Python file serves as a demonstration of 2D arrays (matrices) in Python.
It includes examples and explanations of how to work with 2D arrays for storing and manipulating data in a grid-like structure.
"""

# 2D Arrays (Matrices)

# 📦 Example 1: Creating a 2D array
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print("Matrix:")
for row in matrix:
    print(row)

# 🔄 Example 2: Accessing elements in a 2D array
print("\nElement at row 2, column 3:", matrix[1][2])

# 📝 Example 3: Modifying elements in a 2D array
matrix[0][0] = 10
print("\nModified matrix:")
for row in matrix:
    print(row)

# ➕ Example 4: Adding a new row to a 2D array
new_row = [11, 12, 13]
matrix.append(new_row)
print("\nMatrix with new row:")
for row in matrix:
    print(row)

# Tasks:
# 🚀 Create a 2D array representing a 3x3 tic-tac-toe board and print it.
# 🍔 Access and print the element at row 2, column 2 from the following matrix:
#    [[9, 8, 7], [6, 5, 4], [3, 2, 1]]
# 🎯 Modify the element at row 3, column 1 in the following matrix to be 100:
#    [[10, 20, 30], [40, 50, 60], [70, 80, 90]]
# 🌟 Add a new column [100, 200, 300] to the following 2D array:
#    [[1, 2], [3, 4], [5, 6]]
# 🏆 Create a 2D array representing a seating arrangement for a classroom with 5 rows and 4 columns, then print it.
# 💡 Access and print the element at row 4, column 3 from the seating arrangement you created.
# 🎉 Modify the element at row 2, column 1 in the seating arrangement to represent a student's name.
# 🎨 Add a new row to the seating arrangement representing additional seating, then print the updated arrangement.
