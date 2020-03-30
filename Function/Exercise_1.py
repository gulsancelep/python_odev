"""
Exercise 1
Write a shutting down program:

First, def a function, shut_down, that takes one argument s. Then, if the shut_down function receives an s equal to "yes",
it should return "Shutting down" Alternatively, elif s is equal to "no", then the function should return "Shutdown aborted".
Finally, if shut_down gets anything other than those inputs, the function should return "Sorry".

"""
# !/usr/bin/env python
# -*- coding: utf-8 -*-
from pip._vendor.distlib.compat import raw_input


def shut_down(s):
    if s == "yes":
        return print("Shutting down")
    elif s == "no":
        return print("Shutdown aborted")
    else:
        return print("Sorry")


input_name = raw_input("yes-no :")
shut_down(input_name)
