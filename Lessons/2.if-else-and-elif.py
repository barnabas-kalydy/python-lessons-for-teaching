# Examples of if-else and elif statements in Python

# Example 1: Simple if-else statement
num = 10
if num > 0:
    print("Positive number")
else:
    print("Non-positive number")

# Example 2: if-elif-else ladder
score = 85
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"
print("Your grade is:", grade)

# Example 3: Nested if-else statements
num = 15
if num % 2 == 0:
    if num % 3 == 0:
        print("Divisible by both 2 and 3")
    else:
        print("Divisible by 2 but not by 3")
else:
    print("Not divisible by 2")

# Tasks
# Task 1: Check if a number is positive, negative, or zero.
# Task 2: Determine if a person is eligible to vote based on their age.
# Task 3: Find the largest of three numbers.
# Task 4: Determine if a year is a leap year or not.
# Task 5: Check if a character is a vowel or consonant.
# Task 6: Determine if a number is even or odd.
# Task 7: Classify a triangle based on its sides (equilateral, isosceles, scalene).
# Task 8: Check if a number is prime or composite.
