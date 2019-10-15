'''Solution to Project Euler Problem 20
Code by Timothy Virgil Payne Jr.
Started: 10/15/19 4:06 PM
Completed: 10/15/19 4:12 PM

This is a straightforward solution. Took me five minutes.'''

from math import factorial

import sys

dig_sum = 0
fact_100 = factorial(100)

for a in str(fact_100):

	dig_sum += int(a)


print(f'The sum of the digits in 100! is {dig_sum}.\n')

wait = input("Press enter to exit.")

sys.exit()
