from datetime import datetime, date, time, timedelta, timezone
"""
datetime - combines date and time
time - only time
date - only date
timedelta - difference between two dates
timezone - zones of time
"""

current_datetime = datetime.now()
print(f'Current datetime: {current_datetime}')
print(type(current_datetime))




current_date = datetime.now().date()
current_time = datetime.now().time()
print(f'Current date: {current_date}')
print(f'Current time: {current_time}')
print(type(current_date))
print(type(current_time))


specific_datetime = datetime(2001, 9, 11, 13, 30, 14)
specific_date1 = date(2001, 9, 11)
specific_time1 = time(9, 30)
specific_time2 = time(9, 30, 15)
print(specific_datetime)

"""
%Y - four digit year
%m - two digit month
%d - two digit day
%H - two digit hour (24 format)
"""
# input: 2001-09-11 12:30:00
# output: 11/09/01:12-30
print(specific_datetime.strftime("%d/%m/%y:%H-%M"))
print(specific_datetime.strftime("%A, %B %d, %Y"))



date_string = "20-08-2024 15:30:45"
print(type(date_string))
parsed_datetime = datetime.strptime(date_string, "%d-%m-%Y %H:%M:%S")
print(parsed_datetime)
print(type(parsed_datetime))


now = datetime.now()
future_date = now + timedelta( days=2, hours=3, milliseconds=4578)
past_date = now - timedelta(hours=3, minutes=46, milliseconds=4578)
print(future_date)
print(past_date)


# working with timezone
now_datetime = datetime.now()
print(f"now_datetime: {now_datetime}")
utc_datetime = datetime.now(timezone.utc)
print(f"utc_datetime: {utc_datetime}")
utc_plus_2_time = utc_datetime + timedelta(hours=2)


import zoneinfo

# Will return a long list of timezones (opens many files!)
print(zoneinfo.available_timezones())



# Import ZoneInfo
from zoneinfo import ZoneInfo

jerus = ZoneInfo("Asia/Jerusalem")

# Aware datetime object with UTC timezone
dt_jerus = datetime.now(tz=jerus)

# The type of an aware object implemented with ZoneInfo is zoneinfo.ZoneInfo
print(type(dt_jerus.tzinfo))
print(dt_jerus)

# Task 1 (Easy): Calculate Working Days Between Two Dates
# Explanation:
# Write a function `working_days_between` that takes two dates as input and calculates the number of working days (Monday to Friday)
# between them, excluding weekends. Use `datetime` and list comprehensions, and apply `enumerate` to label each working day.





# Example Input:
# start_date = '2024-08-01'
# end_date = '2024-08-10'

# Example Output:


# Output: (7, [(1, datetime(2024, 8, 1)), (2, datetime(2024, 8, 2)), (3, datetime(2024, 8, 5)), ...])

# ----------------------------------------------------------------------

# Task 2 (Easy): Calculate Daily Interest
# Explanation:
# Write a function `calculate_daily_interest` that calculates the daily compound interest for each day of a month given
# the principal, rate, and days. Use `zip` to pair days with interest rates.



# Example Input:
# principal = 1000
# rate = 0.05
# days = 31

# Example Output:
# Output: [1001.37, 1002.74, 1004.12, ...]

# ----------------------------------------------------------------------

# Task 3 (Medium): Group Transactions by Week
# Explanation:
# Write a function `group_transactions_by_week` that takes a list of transaction dates and amounts and groups them by week number.
# Use `groupby` to group transactions by the week and `enumerate` to label each week's transactions.





# Example Input:
# transactions = [
#     ('2024-08-01', 500),
#     ('2024-08-03', 300),
#     ('2024-08-05', 200),
#     ('2024-08-07', 150),
#     ('2024-08-10', 100)
# ]

# Example Output:
# Output: {31: [(1, (datetime(2024, 8, 1), 500)), (2, (datetime(2024, 8, 3), 300)), ...]}

# ----------------------------------------------------------------------

# Task 4 (Medium): Calculate Net Position Over Time
# Explanation:
# Write a function `calculate_net_position` that takes a list of deposits and withdrawals with their respective dates,
# computes the net position per week, and returns a summary. Use `reduce` to compute the net position.






# Example Input:
# transactions = [
#     ('2024-08-01', 500),
#     ('2024-08-03', -300),
#     ('2024-08-05', 200),
#     ('2024-08-07', -150),
#     ('2024-08-10', -100)
# ]

# Example Output:


# Output: {31: 150, 32: -250}

# ----------------------------------------------------------------------

# Task 5 (Hard): Forecast Monthly Cash Flow
# Explanation:
# Write a function `forecast_cash_flow` that takes a list of daily transactions for a month and forecasts the net cash flow
# at the end of the month. Use `zip`, `map`, `filter`, and `datetime` to perform the analysis.




# Example Input:
# transactions = [
#     ('2024-08-01', 500),
#     ('2024-08-02', -200),
#     ('2024-08-05', 300),
#     ('2024-08-07', -100),
#     ('2024-08-10', 400)
# ]

# Example Output:


# Output: 900

# ----------------------------------------------------------------------

# Task 6 (Hard): Calculate Average Transaction Time Difference by Time Zone
# Explanation:
# Write a function `average_time_difference` that calculates the average time difference between transactions
# grouped by their time zones. Use `datetime`, `timedelta`, `groupby`, `map`, and `reduce` to perform this task.




# Example Input:
# transactions = [
#     ('2024-08-01 10:00:00', 'IST', 500),
#     ('2024-08-01 15:00:00', 'IST', -200),
#     ('2024-08-02 09:00:00', 'PST', 300),
#     ('2024-08-02 17:00:00', 'PST', -100),
#     ('2024-08-03 12:00:00', 'IST', 400)
# ]

# Example Output:
# Output: {'IST': 18000.0, 'PST': 28800.0}






