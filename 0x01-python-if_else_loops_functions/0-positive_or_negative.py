#!/usr/bin/python3
import random
number = random.randint(-10, 10)
if number > 0:
    print("{} is positive".format(number))
elif number == 0:
    print("{} is zero".format(number))
elif number < 0:
    print("{} is negative".format(number))
num = random.randint(-100, 100)
if num > 0:
	print('%s, is positive'%(num))
elif num < 0:
	print('%s, is negative'%(num))
else:
	print('%s, is zero'%(num))
