#This is the solution to Project Euler Problem 3
#Code by Timothy Payne
#Completed: 03/15/2019

def Max_Prime_Factor(a):

	from math import sqrt

	if a == 2:

		return 2

	if a == 3:

		return 3

	for x in range(3, int(sqrt(a) + 2), 2):

		if a % x == 0:

			for y in range(2, int(sqrt(x) + 2)):

				if x % y == 0:

					break

			else:

				max_prime = x

	print(max_prime)


if __name__ == '__main__':

	Max_Prime_Factor(600851475143)