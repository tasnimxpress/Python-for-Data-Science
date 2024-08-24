"""
This program take input year and month, 
and return the days in that year and month."""


def is_leap(year):
    if year % 100 == 0:
        if year % 400 == 0:
            return True
        else:
            return False
    elif year % 4 == 0:
        return True
    else:
        return False


def days_in_month(year, month_number):
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leap(year) == True:
        days[1] = 29

    month_number = days[month_number - 1]
    return month_number


year = int(input('Year: '))
month = int(input('Month: '))

days_of_month = days_in_month(year, month)
print(days_of_month)
