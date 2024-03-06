# Example 1: Basic while loop
count = 0
while count < 5:
    print(count, end=' ')
    count += 1
print()

# Example 2: Infinite loop with user input
# Uncomment the code below and be cautious when running as it creates an infinite loop
"""
while True:
    user_input = input("Enter 'quit' to exit: ")
    if user_input.lower() == 'quit':
        break
"""

# Example 3: While loop with else statement
num = 5
while num > 0:
    print(num, end=' ')
    num -= 1
else:
    print("Loop finished.")

# Tasks
# Task 1: Print numbers from 1 to 10 using a while loop.
# Task 2: Calculate the sum of digits of a number using a while loop.
# Task 3: Determine if a number is a palindrome using a while loop.
# Task 4: Print a series of numbers until the sum exceeds 100 using a while loop.
# Task 5: Read numbers from the user until a negative number is entered using a while loop.
# Task 6: Calculate the factorial of a number using a while loop.
# Task 7: Print even numbers between 1 and 10 using a while loop.
