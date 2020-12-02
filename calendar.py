import calendar
print(calendar.weekheader(3)) #prints the week names
print()  #adding a new line
print(calendar.firstweekday())  #printing the index of monday
print()

print(calendar.month(2019,3))  #printing the 3rd month of 2019
print()
print(calendar.monthcalendar(2020,11))  #printing the month in matrix form
print(calendar.calendar(2020))   #printing the year 2020
day_of_the_week = calendar.weekday(2020,12,2)  #taking the specific day to day_of_the_week
print(day_of_the_week) #printing the corresponding day
is_leap = calendar.isleap(2020) #checking whether a year is leap or not
print(is_leap)  
how_many_leap_days = calendar.leapdays(2000,2001)  #taking no. of leap days 
print(how_many_leap_days)
