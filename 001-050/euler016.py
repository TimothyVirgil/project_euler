# Solution to Project Euler Problem 16
# Code by Timothy Virgil Payne Jr.
# Started: 10/02/19 5:16 PM
# Completed: 10/07/19 12:52 PM

#straightforward

import sys

ans = sum([int(a) for a in str(2 ** 1000)])

print(f'The sum of the digits is {ans}.')

wait = input("Press enter to exit.")

sys.exit()