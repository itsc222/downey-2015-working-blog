import time

#Floor division and modulus

minutes = 105

print(minutes / 60)
hours = minutes // 60

remainder = minutes - hours * 60

print(remainder)

remainder = minutes % 60

print(remainder)

#5.2 Boolean operators

print(5 == 5)

print(5 == 6)

print(type(True))

print(42 == 42 and True)

print(42 == 41 and True)

print(42 == 41 or True)

#5.4 Conditional Expressions

def pos_or_neg(x):
    if x > 0:
        print('x is positive')
    if x < 0:
        print('x is negative')
    if x == 0:
        print('x is zero')

pos_or_neg(5)
pos_or_neg(-5)

def odd_or_even(x):
    if x % 2 == 0:
        print('x is even')
    else:
        print('x is odd')

odd_or_even(1)

def less_than_or_more_than(x, y):
    if x < y:
        print('x is less than y')
    elif x > y:
        print('x is greater than y')
    else:
        print('x and y are equal')

less_than_or_more_than(4, 10)

def less_than_or_more_than(x, y):
    if x < y:
        print('x is less than y')
    else:
        if x > y:
            print('x is greater than y')
        else:
            print('x and y are equal')

less_than_or_more_than(2, 3)

def single_digit(x):
    if 0 < x:
        if x < 10:
            print('x is a positive single-digit number.')

def single_digit(x):
    if x < 0 and x > 10:
        print('x is a single-digit number.')

#5.8 recursion:

def countdown(n):
    if n <=0:
        print("Blastoff!")
    else:
        print(n)
        # time.sleep(1)
        countdown(n - 1)

# countdown(10)

def print_n(s, n):
    if n <=0:
        return
    print(s)
    print_n(s, n-1)

print_n('Yes!', 10)

def print_hello(n):
    if n <= 0:
        return(print("I'm done. Give me a cookie."))
    print("hello!")
    print_hello(n - 1)

print_hello(7)

import math

try:

    signal_power = 9
    noise_power = 10

    ratio = signal_power // noise_power

    decibels = 10 * math.log10(ratio)

    print(decibels)
except ValueError as e:
    print(f"there was an error: a {e}")

try:

    signal_power = 9
    noise_power = 10

    ratio = signal_power / noise_power

    decibels = 10 * math.log10(ratio)

    print(decibels)
except ValueError as e:
    print(f"there was an error: a {e}")

import time

gmt = time.time()

print(gmt)

current_year = 2024
epoch_year = 1970

passed_years = current_year - epoch_year
leap_seconds = ((passed_years / 4) * 24 * 60 * 60)
print(passed_years)

passed_seconds = passed_years * 365 * 24 * 60 * 60

print(passed_seconds)

print((gmt - passed_seconds - leap_seconds) / 60 / 60 / 24)


