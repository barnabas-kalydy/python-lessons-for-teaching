"""
🐍 This Python file serves as a demonstration of while loops in Python.
It includes examples and explanations of how to use while loops for iterative execution.
"""

# While Loops

# 🔄 Example 1: Simple while loop
count = 0
while count < 5:
    print("Count is:", count)
    count += 1

# 🔢 Example 2: While loop with condition based on user input
number = int(input("Enter a number greater than 10: "))
while number <= 10:
    print("Number is not greater than 10.")
    number = int(input("Enter a number greater than 10: "))
print("Number is greater than 10.")

# 📝 Example 3: While loop with break statement
num = 1
while True:
    print(num)
    num += 1
    if num > 5:
        break

# 🛤️ Example 4: While loop with continue statement
i = 0
while i < 5:
    i += 1
    if i == 3:
        continue
    print("Current value is:", i)

# Tasks:
# 😎 Write a while loop to print numbers from 10 to 1 in descending order.
# 📏 Write a while loop to calculate the factorial of a number entered by the user.
# 🤔 Write a while loop to find the first Fibonacci number greater than 1000.
# 😄 Write a while loop to repeatedly ask the user for a password until they enter "password123".
# 🌈 Write a while loop to generate random numbers between 1 and 10 until a 7 is generated.
# 🎲 Write a while loop to check if a given number is a palindrome.
# 🌟 Write a while loop to print the multiplication table of a given number up to 10.
