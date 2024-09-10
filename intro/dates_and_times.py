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








