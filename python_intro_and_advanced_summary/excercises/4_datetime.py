# Topic Recap: Time, Date, Datetime, Timedelta, Timezone, strftime, strptime

# 3 Easy Exercises

# Exercise 1 (Easy): Current Date and Time
# Explanation: Write a Python program that prints the current date and time in the format "YYYY-MM-DD HH:MM:SS".
# Guidance: Use the `datetime` module's `datetime.now()` method and `strftime()` for formatting.
# Solution:

# Example Input:
# (No input required)
# Example Output:
# Current Date and Time: 2024-09-15 14:45:30


# Exercise 2 (Easy): Days Until Birthday
# Explanation: Write a program that takes a user's birthdate (YYYY-MM-DD) as input and calculates the number of days until their next birthday.
# Guidance: Use `datetime` module, convert the string input using `strptime()`, and calculate the difference with `timedelta`.
# Solution:


# Example Input:
# Enter your birthdate (YYYY-MM-DD): 1990-10-10
# Example Output:
# Days until your next birthday: 25


# Exercise 3 (Easy): Time Difference Calculator
# Explanation: Write a program that takes two times in "HH:MM" format as input and calculates the difference between them in minutes.
# Guidance: Use `strptime()` to convert strings to time objects, then use `timedelta` to find the difference.
# Solution:

# Example Input:
# Enter the first time (HH:MM): 09:30
# Enter the second time (HH:MM): 11:15
# Example Output:
# Difference in minutes: 105


# 2 Medium Exercises

# Exercise 4 (Medium): Meeting Scheduler with Time Zones
# Explanation: Write a program that takes two meeting times (one in UTC and another in any specified timezone) and calculates the local time of the second meeting based on the specified timezone using `pytz`.
# Solution:


# Example Input:
# Enter the meeting time in UTC (YYYY-MM-DD HH:MM): 2024-09-15 14:00
# Enter the target timezone (e.g., 'US/Eastern'): US/Eastern
# Example Output:
# Local time for the meeting: 2024-09-15 10:00 EDT


# Exercise 5 (Medium): Project Deadline Countdown
# Explanation: Write a program that calculates the number of weeks, days, hours, and minutes until a project deadline given in "YYYY-MM-DD HH:MM" format.
# Solution:


# Example Input:
# Enter the project deadline (YYYY-MM-DD HH:MM): 2024-10-01 09:00
# Example Output:
# Time until the deadline: 2 weeks, 1 day, 17 hours, 15 minutes


# 1 Hard Exercise

# Exercise 6 (Hard): Working Hours Tracker
# Explanation: Create a program that tracks working hours for a remote employee. The program should:
# - Take the start and end working times for each day of the week (in "HH:MM" format).
# - Calculate the total number of hours worked in a week.
# - If the total hours exceed 40, calculate the overtime worked and display it.
# Solution:


# Example Input:
# Enter start time for Monday (HH:MM): 09:00
# Enter end time for Monday (HH:MM): 17:00
# Enter start time for Tuesday (HH:MM): 09:00
# Enter end time for Tuesday (HH:MM): 17:00
# Enter start time for Wednesday (HH:MM): 09:00
# Enter end time for Wednesday (HH:MM): 17:00
# Enter start time for Thursday (HH:MM): 09:00
# Enter end time for Thursday (HH:MM): 17:00
# Enter start time for Friday (HH:MM): 09:00
# Enter end time for Friday (HH:MM): 19:00
# Example Output:
# Total hours worked: 42.00 hours
# Overtime worked: 2.00 hours
