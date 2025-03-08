#/usr/bin/python3
# Function to check if a year is a leap year
def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    return False


for year in range(1900, 2101):
    if is_leap_year(year):
        print(year)
