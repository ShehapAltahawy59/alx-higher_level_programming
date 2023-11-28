#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = abs(number) % 10  # Get the last digit
if last_digit == 0:
    print("Last digit of {} is 0".format(number))
elif last_digit < 6:
    print("Last digit of {} is {} and is less than 6".format(number, last_digit))
else:
    print("Last digit of {} is {} and is not less than 6 or 0".format(number, last_digit))

