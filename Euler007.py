# Solution to Project Euler Problem 7
# Code by Timothy Virgil Payne Jr.
# Started: 09/26/19 1:08 PM
# Completed: 09/26/19 2:35 PM

# Need to make a quick prime checker - adjust range as needed

import sys

prime_list = [2] #add two so we can cycle through numbers faster later

prime_count = len(prime_list)

def primecheck(a):

	'This function checks to see if an integer is prime.'

	if a < 2:

		return False

	elif a == 2 or a == 3:

		return True

	else:
		
		for b in range(3, int(a**(0.5)) + 2, 2):

			if a % b == 0:

				return False
		else:

			return True

if __name__ =='main':

	for a in range(3,1000000,2):

		if prime_count == 10_001:

			print(f'The 10 001st prime number is {prime_list[-1]}.\n')

			wait = input("press a key to exit.")

			sys.exit()

		else:

			if primecheck(a):

			
				prime_list += [a]
				prime_count += 1






