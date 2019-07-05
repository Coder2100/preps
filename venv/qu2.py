def say_hello():
    print('Hello, World')


for i in range(5):
    say_hello()


#
# Your previous Plain Text content is preserved below:
#
# You are given the following information, but you may prefer to do some research for yourself.
#
# 1 Jan 1900 was a Monday.
# Thirty days has September,
# April, June and November.
# All the rest have thirty-one,
# Saving February alone,
# Which has twenty-eight, rain or shine.
# And on leap years, twenty-nine.
# A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
#
# How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
#
# Feel free to check your answers by submitting to Project Euler
# https://projecteuler.net/problem=19
# This problem has a difficulty rating of 5%

def numberofSundays(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return 1
            else:
                return 0
        return 1
    else:
        return 0


def numberofMonthList(year):
    monthList = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if numberofSundays(year) == 1:
        monthList[1] = 29
    return monthList


startDay = 1

count = 0
for year in range(1900, 2001):
    monthNumber = numberofMonthList(year)
    for month in range(0, 12):
        startDay = (startDay + monthNumber[month]) % 7  # 7 days of the week
        if year > 1900 and startDay == 0:
            count = count + 1
print()
print(
    f"There are, {count}, sundays that fell between the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000).")
