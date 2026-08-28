# Counting Sundays

# You are given the following information, but you may prefer to do some research for yourself.

#   -1 Jan 1900 was a Monday.
#   -Thirty days has September,
#    April, June and November.
#    All the rest have thirty-one,
#    Saving February alone,
#    Which has twenty-eight, rain or shine.
#    And on leap years, twenty-nine.
#   -A leap year occurs on any year evenly divisible by 4, but not on a century unless it is
#    divisible by 400.

# How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 
# 31 Dec 2000)?



days30 = [4, 6, 9, 11]
days31 = [1, 3, 5, 7, 8, 10, 12]

counter = 2 # 1 Jan 1901 is a Tuesday. Tuesday will be '2', making Sunday '0'
year = 1901

results = 0

while year < 2001:
    for month in range(1, 13):
        if counter % 7 == 0:
            results += 1

        if month in days31:
            counter += 31
        elif month in days30:
            counter += 30
        elif year % 4 == 0:
            counter += 29
        else:
            counter += 28

    year += 1

print(results)
