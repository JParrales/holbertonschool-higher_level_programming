#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if number >= 0:
    strnum = str(number)[-1]
else:
    strnum = '-' + str(number)[-1]

digit = ["and is greater than 5", "and is 0", "and is less than 6 and not 0"]

if strnum > '5':
    select = 0
elif strnum == '0':
    select = 1
else:
    select = 2

print("Last digit of {:d} is {:s} {:s}".format(number, strnum, digit[select]))
