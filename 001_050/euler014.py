# Solution to Project Euler Problem 14
# Code by Timothy Virgil Payne Jr.
# Started: 10/02/19 4:49 PM
# Completed: 10/02/19 5:06 PM

#This solution works but it's a little slow. It's completely straightforward.

import sys

max_chain_count = (0,0)  #Initial declaration of the chain count

def Collatz(a):

	'This function returns the length of a Collatz chain.'

	chain_count = 0

	b = a

	while b != 1:

		if b % 2 == 0:

			b = b // 2

			chain_count += 1

		else:

			b = 3 * b + 1

			chain_count += 1

	return (a, chain_count)

if __name__ == '__main__':
	

	for x in range(1,1_000_000):

		curr_chain = Collatz(x)

		if curr_chain[1] > max_chain_count[1]:

			max_chain_count = curr_chain

		else:

			continue

	print(f'''{max_chain_count[0]} produces the longest Collatz chain. 
		It has {max_chain_count[1]} terms.''')

	wait = input('Press enter to exit.')

	sys.exit()


