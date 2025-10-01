#method 1
from datetime import datetime #module ka naam bhi datetime hai and uske andar ek class hai uska naam bhi datetime hai 
now= datetime.now() #for current time
print(now)
#or
#method 2
import datetime
now = datetime.datetime.now() #for current time

today = datetime.date.today() #for today's date
print(now)
print(today)
time = datetime.time(15,34,34) #for showing the time in 
print(time)

#The datetime module in Python provides classes to manipulate dates and times easily. It's widely used for tasks like:

#Getting the current date and time
#Formatting dates and times
#Performing arithmetic with dates (e.g., finding the difference between two dates)
#Working with time zones
a = datetime.datetime.now().minute
print(a)