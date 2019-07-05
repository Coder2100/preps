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

def numberofSundays():
    numberofSundays= [[0,0,0]]  #initialize list with day, month, year
    for year in range(1900, 2001):#range for number of sundays fell between 1901 and 2000
        for month in range(1, 13):# 1 for january of 1901 and 13 for Dec of 2000, if use range to 1-12 it ends at 11
            if month in [4, 6, 9, 11]:#April-4, June-6,Sept-9, Nov-11
                dayRange = 30# days in month of 4,6,9,11
            elif not month - 2:#get index of seond last month
                if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):#getting the leap year and leap century
                        dayRange = 29
                else:
                    dayRange = 28
            else:
                dayRange = 31
            for day in range(1, dayRange + 1):
                numberofSundays.append([year, month, day])
    return numberofSundays

def listingSundays():
    allSundays = numberofSundays()
    sundayList = []
    for day in range(len(allSundays)):
        if not (day - 6) % 7 and allSundays[day][0] > 1900 and not allSundays[day][2] - 1:
            sundayList.append(allSundays[day])
    return len(sundayList)

print(listingSundays())