#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number > 0:
    n = number % 10
else:
    n = number % -10

if n == 0:
    res = "and is 0"
elif n > 5:
    res = "and is greater than 5"
else:
    res = "and is less than 6 and not 0"

print("Last digit of {} is {} {}".format(number, n, res))
