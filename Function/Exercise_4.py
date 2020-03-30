"""
Exercise 4
Rewrite your pay computation program (previus chapter) with time-and-a-half for overtime
and create a function called computepay which takes two parameters (hours and rate).

Enter Hours: 45
Enter Rate: 10
Pay: 475.0

"""

# !/usr/bin/env python
# -*- coding: utf-8 -*-
from pip._vendor.distlib.compat import raw_input


def compute_pay(hours, rate):
    if int(hours) <= 40:
        pay = int(hours) * int(rate)
        return print("Pay: ", pay)
    else:
        overtime = int(hours) - 40
        pay = (int(overtime) * int(rate) * 1.5) + (40 * int(rate))
        return print("Overtime + Pay: ", pay)


hour = raw_input("Enter Hours: ")
rates = raw_input("Enter Rate:")
compute_pay(hour, rates)
