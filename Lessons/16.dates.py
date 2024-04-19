"""
📅 This Python file serves as a demonstration of date handling in Python.
It includes examples and explanations of how to work with dates using the datetime module.
"""

# Date Handling in Python

# 📆 Example 1: Creating a Date Object
from datetime import date

# Create a date object representing today's date
today = date.today()
print("Today's date:", today)

# 📅 Example 2: Formatting Dates
# Format the date as YYYY-MM-DD
formatted_date = today.strftime("%Y-%m-%d")
print("Formatted date:", formatted_date)

# 🗓️ Example 3: Extracting Components from a Date
# Extract year, month, and day from the date object
year = today.year
month = today.month
day = today.day
print("Year:", year)
print("Month:", month)
print("Day:", day)

# 📆 Example 4: Calculating the Difference Between Dates
from datetime import timedelta

# Create a date object for a future date
future_date = today + timedelta(days=30)

# Calculate the difference between future_date and today
date_difference = future_date - today
print("Days until future date:", date_difference.days)

# Tasks:
# 📅 Write a program to display the current date and time.
# 🎂 Write a program to calculate the age of a person born on April 10, 1995.
# 📆 Write a program to find the number of days between two given dates.
# 📅 Write a program to check if the year 2024 is a leap year or not.
# ⏰ Write a program to add 5 hours and 30 minutes to the current time.
# 🎉 Write a program to congratulate a user on their upcoming birthday if it's within the next 7 days.
# 🎃 Write a program to determine if today's date is a Halloween (October 31st).
# 📆 Write a program to find the day of the week for the given date December 25, 2023.
