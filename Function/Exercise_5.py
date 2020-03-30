"""
Exercise 5
Let's use functions to calculate your trip's costs:

Define a function called hotel_cost with one argument nights as input. The hotel costs $140 per night.
So, the function hotel_cost should return 140 * nights.
Define a function called plane_ride_cost that takes a string, city, as input.
The function should return a different price depending on the location, similar to the code example above.
Below are the valid destinations and their corresponding round-trip prices.
"Charlotte": 183
"Tampa": 220
"Pittsburgh": 222
"Los Angeles": 475
-Below your existing code, define a function called rental_car_cost with an argument called days.
Calculate the cost of renting the car: Every day you rent the car costs $40.(cost=40*days)
if you rent the car for 7 or more days, you get $50 off your total(cost-=50).
Alternatively (elif), if you rent the car for 3 or more days, you get $20 off your total.
You cannot get both of the above discounts. Return that cost. -Then, define a function called trip_cost that takes two arguments, city and days.
Like the example above, have your function return the sum of calling the rental_car_cost(days), hotel_cost(days), and plane_ride_cost(city) functions.
Modify your trip_cost function definion. Add a third argument, spending_money.
Modify what the trip_cost function does. Add the variable `spending_money to the sum that it returns.

"""
# !/usr/bin/env python
# -*- coding: utf-8 -*-
from pip._vendor.distlib.compat import raw_input

city_prices = {
    "charlotte": 183,
    "pittsburgh": 222,
    "tampa": 220,
    "los angeles": 475
}


def hotel_cost(nights):
    return nights * 140


def plane_ride_cost(city):
    try:
        return city_prices[city]
    except KeyError:
        print("Sorry wrong value.")


def rental_car_cost(trip_days):
    if trip_days >= 7:
        return (40 * trip_days) - 50
    elif 3 <= trip_days < 7:
        return (40 * trip_days) - 20
    else:
        return 40 * trip_days


def trip_cost(city, trip_days):
    spending_money = hotel_cost(trip_days) + plane_ride_cost(city) + rental_car_cost(trip_days)
    return print("Cost: ", spending_money)


city = raw_input("Which city: charlotte, pittsburgh, tampa, los angeles: ")
trip_day = int(raw_input("how many days will you stay: "))
trip_cost(city, trip_day)
