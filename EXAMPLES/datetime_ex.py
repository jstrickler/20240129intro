
from datetime import datetime, date, timedelta

today = date.today()
print("today:", today)  # get today's date
print("type(today): {}".format(type(today)))
print("today.month: {}".format(today.month))
print("today.day: {}".format(today.day))
print("today.year: {}".format(today.year))
print()

now = datetime.now()  # get today's date and time
print("now: {}".format(now))
print("now.day:", now.day)  # a datetime object has attributes for date/time parts
print("now.month:", now.month)
print("now.year:", now.year)
print("now.hour:", now.hour)
print("now.minute:", now.minute)
print("now.second:", now.second)
print("now.microsecond:", now.microsecond)
print()

d1 = datetime(2018, 6, 13, 4, 55, 27, 8082)  # create a date object
d2 = datetime(2018, 8, 24)
d3 = d2 - d1  # date objects can be subtracted from other date objects

print("raw time delta:", d3)
print("time delta days:", d3.days)  # timedelta has days, seconds, and microseconds

