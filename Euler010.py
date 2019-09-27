# Solution to Project Euler Problem 10
# Code by Timothy Virgil Payne Jr.
# Started: 09/27/19 12:47 PM
# Completed: 09/27/19 01:19 PM

#Need to add up primes
#We'll use our primechecker from problem 7

import sys

def over3_prime_check(a): #Are there ways to speed up a prime check algorithm?

	'This function assumes you are checking primes greater than 3. This is for speed purposes.'

	for b in range(3, int(a**(0.5)) + 2, 2):

		if a % b == 0:

			return False
		
	else:

		return True

prime_sum = 5 #initialize prime sum. Start with 2 + 3 = 5 for speed purposes.

for x in range(5, 2_000_000, 2):

	elif over3_prime_check(x):

		prime_sum += x


print(f'The sum of all primes below two million is {prime_sum}.')

wait = input("Press enter to exit.")

sys.exit()

