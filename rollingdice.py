from __future__ import print_function, division
from numpy import arange
from random import randint

"""
Simulation of two dice. Determines number
of times both roll a 6 in one million tries.
"""

count = 0

for i in arange(10e6):	
	d1 = randint(0,6)	
	d2 = randint(0,6)	
	
	if d1 == 6 and d2 == 6:
		count += 1

print(count/10e6)

"""
Results: 0.0204445
"""