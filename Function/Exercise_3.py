"""
Exercise 3
First, def a function called distance_from_zero, with one argument (choose any argument name you like).
If the type of the argument is either int or float,
the function should return the absolute value of the function input. Otherwise, the function should return "Nope".
Check if it works calling the function with -5.6 and "what?".

"""


# !/usr/bin/env python
# -*- coding: utf-8 -*-


def distance_from_zero(argument):
    if type(argument) == int or type(argument) == float:
        return print(abs(argument))
    else:
        print("Nope")


distance_from_zero(-5.6)
