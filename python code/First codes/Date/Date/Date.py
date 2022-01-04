import datetime
nowdate = datetime.date.today()
print(nowdate)

# Acessing different parts of date

import datetime
nowdate = datetime.date.today()
print(nowdate)
print(nowdate.year)
print(nowdate.month)
print(nowdate.day)

# Using a different display format for date

import datetime
nowdate = datetime.date.today()
print(nowdate.strftime("%d %b, %Y"))

# Calculating days until my birthday

import datetime
nowdate = datetime.date.today()
birthday = input("What is your birthday? ")
birthday = datetime.datetime.strptime(birthday, "%m/%d/%Y")
print(birthday)

# Telling the user the prefered format

import datetime
nowdate = datetime.date.today()
birthday = input("What is your birthday? (mm/dd/yyyy) ")
birthday = datetime.datetime.strptime(birthday, "%m/%d/%Y")
print(birthday)

# Calculating dates

import datetime
nowdate = datetime.date.today()
nextdate = datetime.datetime.strptime("12/20/2014", "%m/%d/%Y").date()
diff = nextdate - nowdate
print(diff.days)

#
import datetime
nowdate = datetime.date.today()
birthday = input("What is your birthday? (mm/dd/yyyy) ")
birthday = datetime.datetime.strptime(birthday, "%m/%d/%Y").date()
print(birthday)
days = birthday - nowdate
print(days)

# Time

import datetime
nowtime = datetime.datetime.now()
print(nowtime)
print(nowtime.hour)
print(nowtime.minute)
print(nowtime.second)

#
import datetime
nowtime = datetime.datetime.now()
print(datetime.datetime.strftime(nowtime, "%H:%M"))

#
import datetime
nowtime = datetime.datetime.now()
print(datetime.datetime.strftime(nowtime, "%I:%M"))

#
import datetime
nowtime = datetime.datetime.now()
print(nowtime.minute)

#
import datetime
nowtime = datetime.datetime.now()
print(datetime.datetime.strftime(nowtime, "%I:%M"))