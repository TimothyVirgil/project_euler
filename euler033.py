'''Solution to Project Euler Problem 33
Code by Timothy Virgil Payne Jr.
Started: 7/15/21
Completed: 7/15/21

This could be done with pen and paper but I think it was a tad quicker
to use the fraction module.
'''

from fractions import Fraction

frac_prod = Fraction(1,1)

for a in range(10,99):
	c = int(str(a)[1])

	for b in range((10*c+1),10*(c+1)): #only need to check 9 numbers each time
		if b <= a:

			break

		first_dig_num = int(str(a)[0])
		sec_dig_den = int(str(b)[1])
		frac_1 = Fraction(a,b)
		frac_2 = Fraction(first_dig_num,sec_dig_den)

		if frac_1 == frac_2:
			frac_prod *= frac_2

		else:
			continue

print(frac_prod.denominator)