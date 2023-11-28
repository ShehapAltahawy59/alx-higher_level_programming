#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = abs(number) % 10  # Get the last digit
if number < 0:
    last_digit = - last_digit
str = "Last digit of {} is".format(number)
if last_digit == 0:
    print(str + " 0 and is 0".format(number))
elif last_digit < 6:
    print(str + " {} and is less than 6 and not 0".format(last_digit))
else:
    print(str + " {} and is greater than 5".format(last_digit))
