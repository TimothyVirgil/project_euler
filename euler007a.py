# Solution to Project Euler Problem 7
# Code by Timothy Virgil Payne Jr.
# Started: 09/26/19 1:08 PM
# Completed: 09/26/19 2:35 PM

# Need to make a quick prime checker - adjust range as needed

from math import sqrt

prime_list = [2,3,5,7,11,13] #initial list of primes

prime_count = len(prime_list)

for a in range(17,1000000,2):

	if prime_count == 10_001:

		print(f'The 10 001st prime number is {prime_list[-1]}.\n')

		wait = input("press a key to exit.")

	else:

		for b in range(3, int(sqrt(a))+1):

			if a % b == 0:

				break

		else:
			
			prime_list += [a]
			prime_count += 1






