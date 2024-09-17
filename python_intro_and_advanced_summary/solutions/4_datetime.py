# Topic Recap: Time, Date, Datetime, Timedelta, Timezone, strftime, strptime

# 3 Easy Exercises

# Exercise 1 (Easy): Current Date and Time
# Explanation: Write a Python program that prints the current date and time in the format "YYYY-MM-DD HH:MM:SS".
# Guidance: Use the `datetime` module's `datetime.now()` method and `strftime()` for formatting.
# Solution:
from datetime import datetime

current_time = datetime.now()
formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
print(f"Current Date and Time: {formatted_time}")

# Example Input:
# (No input required)
# Example Output:
# Current Date and Time: 2024-09-15 14:45:30


# Exercise 2 (Easy): Days Until Birthday
# Explanation: Write a program that takes a user's birthdate (YYYY-MM-DD) as input and calculates the number of days until their next birthday.
# Guidance: Use `datetime` module, convert the string input using `strptime()`, and calculate the difference with `timedelta`.
# Solution:
from datetime import datetime, timedelta

birthdate_str = input("Enter your birthdate (YYYY-MM-DD): ")
birthdate = datetime.strptime(birthdate_str, "%Y-%m-%d")
today = datetime.now()
next_birthday = birthdate.replace(year=today.year)

if next_birthday < today:
    next_birthday = next_birthday.replace(year=today.year + 1)

days_until_birthday = (next_birthday - today).days
print(f"Days until your next birthday: {days_until_birthday}")

# Example Input:
# Enter your birthdate (YYYY-MM-DD): 1990-10-10
# Example Output:
# Days until your next birthday: 25


# Exercise 3 (Easy): Time Difference Calculator
# Explanation: Write a program that takes two times in "HH:MM" format as input and calculates the difference between them in minutes.
# Guidance: Use `strptime()` to convert strings to time objects, then use `timedelta` to find the difference.
# Solution:
from datetime import datetime

time1_str = input("Enter the first time (HH:MM): ")
time2_str = input("Enter the second time (HH:MM): ")

time1 = datetime.strptime(time1_str, "%H:%M")
time2 = datetime.strptime(time2_str, "%H:%M")

time_difference = abs((time2 - time1).seconds // 60)
print(f"Difference in minutes: {time_difference}")

# Example Input:
# Enter the first time (HH:MM): 09:30
# Enter the second time (HH:MM): 11:15
# Example Output:
# Difference in minutes: 105


# 2 Medium Exercises

# Exercise 4 (Medium): Meeting Scheduler with Time Zones
# Explanation: Write a program that takes two meeting times (one in UTC and another in any specified timezone) and calculates the local time of the second meeting based on the specified timezone using `pytz`.
# Solution:
from datetime import datetime
import pytz

utc_time_str = input("Enter the meeting time in UTC (YYYY-MM-DD HH:MM): ")
timezone_str = input("Enter the target timezone (e.g., 'US/Eastern'): ")

utc_time = datetime.strptime(utc_time_str, "%Y-%m-%d %H:%M")
utc_time = pytz.utc.localize(utc_time)
target_timezone = pytz.timezone(timezone_str)

local_time = utc_time.astimezone(target_timezone)
print(f"Local time for the meeting: {local_time.strftime('%Y-%m-%d %H:%M %Z')}")

# Example Input:
# Enter the meeting time in UTC (YYYY-MM-DD HH:MM): 2024-09-15 14:00
# Enter the target timezone (e.g., 'US/Eastern'): US/Eastern
# Example Output:
# Local time for the meeting: 2024-09-15 10:00 EDT


# Exercise 5 (Medium): Project Deadline Countdown
# Explanation: Write a program that calculates the number of weeks, days, hours, and minutes until a project deadline given in "YYYY-MM-DD HH:MM" format.
# Solution:
from datetime import datetime, timedelta

deadline_str = input("Enter the project deadline (YYYY-MM-DD HH:MM): ")
deadline = datetime.strptime(deadline_str, "%Y-%m-%d %H:%M")
now = datetime.now()

time_difference = deadline - now
weeks = time_difference.days // 7
days = time_difference.days % 7
hours, remainder = divmod(time_difference.seconds, 3600)
minutes, _ = divmod(remainder, 60)

print(f"Time until the deadline: {weeks} weeks, {days} days, {hours} hours, {minutes} minutes")

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
from datetime import datetime, timedelta

total_minutes = 0
days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

for day in days_of_week:
    start_time_str = input(f"Enter start time for {day} (HH:MM): ")
    end_time_str = input(f"Enter end time for {day} (HH:MM): ")

    start_time = datetime.strptime(start_time_str, "%H:%M")
    end_time = datetime.strptime(end_time_str, "%H:%M")

    daily_minutes = (end_time - start_time).seconds // 60
    total_minutes += daily_minutes

total_hours = total_minutes / 60
overtime = max(0, total_hours - 40)

print(f"Total hours worked: {total_hours:.2f} hours")
if overtime > 0:
    print(f"Overtime worked: {overtime:.2f} hours")
else:
    print("No overtime worked")

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
