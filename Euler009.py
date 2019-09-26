# Solution to Project Euler Problem 8
# Code by Timothy Virgil Payne Jr.
# Started: 09/26/19 6:11 PM
# Completed: 09/26/19 6:24 PM

#We need to test for Pyth triples and find products
#We are looking for three numbers that add to 1000 and form a Pyth triple
#The third number will always be 1000 - a - b.

from math import sqrt
import sys

for a in range(1,1000):

	for b in range(1,1000):

		if (1000 - a - b)**2 == a**2 + b**2:

			c = (1000 - a - b)

			print(f'The product abc is {a*b*c}')

			wait = input('press a key to continue')
			sys.exit()



