#!/usr/bin/python3
import random
num = random.randint(-100, 100)
if num > 0:
	print('%s, is positive'%(num))
elif num < 0:
	print('%s, is negative'%(num))
else:
	print('%s, is zero'%(num))
