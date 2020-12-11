#!/usr/bin/env python
#
from dateutil import parser
from dateutil.relativedelta import relativedelta
from datetime import date

date_strings = [  # <1>
    'April 1, 2015',
    '4/1/2015',
    'Apr 1, 2015',
    'Apr 1 2015',
    '04/01/2015',
    '2/30/2018',
    '1 Apr 2015',
    'April 1st, 2015',
    'April 1, 2015 8:09',
    '4/1/2015 8:09 PM',
    'Apr 1, 2015 5 AM',
    '2/29/2019',
    'Apricot 4, 341',
]

for date_string in date_strings:
    try:
        dt = parser.parse(date_string)  # <2>
        print(dt)
    except ValueError as err:
        print("Can't parse", date_string)
print()

def first_last_days(year):
    first_last_pairs = []
    for month in range(1,13):
        first_day = date(year, month, 1)
        last_day = first_day + relativedelta(day=1, months=1, days=-1)
        first_weekday = first_day.strftime("%A")
        last_weekday = last_day.strftime("%A")
        first_last_pairs.append((first_day, first_weekday, last_day, last_weekday))
    return first_last_pairs

if __name__ == '__main__':

    pairs = first_last_days(2020)

    for first, fwd, last, lwd in pairs:
        print("{} {:9s} {} {:9s}".format(first, fwd, last, lwd))
    print()
