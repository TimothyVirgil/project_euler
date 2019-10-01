# Solution to Project Euler Problem 11
# Code by Timothy Virgil Payne Jr.
# Started: 10/01/19 7:15 PM
# Completed: 10/01/19 7:30 PM

#We need to generate triangular numbers
#We need to count the factors of those numbers
#We can start at 28.

import sys

def fact_count(a):

	curr_fact_count = 0
	
	for b in range(1, int(a ** 0.5) + 1):

		if a % b == 0:

			curr_fact_count += 2

	if a % int(a ** 0.5) == 0:

		curr_fact_count -= 1

	if curr_fact_count > 500:

		return True

	else:

		return False

curr_tri = 28

for x in range(8,100000000):

	curr_tri += x

	if fact_count(curr_tri):

		print(f'The first triangular number with over 500 divisors is {curr_tri}.')

		wait = input('Press enter to exit.')

		sys.exit()

	else:

		continue


