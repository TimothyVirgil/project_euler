'''Solution to Project Euler Problem 21
Code by Timothy Virgil Payne Jr.
Started: 10/17/19 8:30 AM
Completed: 10/20/19 8:35 AM'''


import sys

def prop_div_sum(a): # This function has been tested and appears to work as intended.

	if a == 1 or a == 2 or a == 3:

		return 1

	div_sum = 1

	for x in range(2, int(a**0.5) + 1):

		if a % x == 0:

			div_sum += (x + a//x)

	if a % int(a ** 0.5) == 0:

		div_sum -= (int(a ** 0.5))

	return div_sum

ami_sum = 0

for b in range(2, 10000):

	curr_sum = prop_div_sum(b)

	if curr_sum != 1 and curr_sum != b: # 1 can't be amicable since 1 is not less than 1

		pair_sum = prop_div_sum(curr_sum)

		if pair_sum == b:

			ami_sum += b

	else:

		continue



print(f'The sum of all amicable numbers under 10000 is {ami_sum}.\n')

wait = input("Press enter to exit.")

sys.exit()



	
