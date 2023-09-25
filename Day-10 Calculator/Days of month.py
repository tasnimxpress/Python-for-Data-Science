# this code will return total days of a month including leap year

# If the year is evenly divisible by 4, go to step 2. Otherwise, go to step 5.
# If the year is evenly divisible by 100, go to step 3. Otherwise, go to step 4.
# If the year is evenly divisible by 400, go to step 4. Otherwise, go to step 5.
# The year is a leap year (it has 366 days).
# The year is not a leap year (it has 365 days)

# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             return True
#         else:
#             return False
#     else:
#         return True
# else:
# return False

def is_leap(year):
    """
    This function take year as parameter
    and check whether it is a leap year or not.
    :param year:
    :return:
    """
    if year % 4 == 0 and year % 100 == 0 and year % 400 == 0:
        return True
    elif year % 4 == 0 and year % 100 != 0:
        return True
    else:
        return False


def days_in_month(year, month):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    number_days = month_days[month - 1]
    if is_leap(year) is True and month == 2:
        return 29
    else:
        return number_days


check_year = int(input("Enter a year: "))
check_month = int(input("Enter a month: "))
days = days_in_month(check_year, check_month)
print(days)
