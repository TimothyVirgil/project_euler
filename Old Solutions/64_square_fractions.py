# Euler 64: Square Fractions

import math
import os

oddcount = 0

for n in range(0,10001): # run through numbers
	
	print(n)

	if math.sqrt(n).is_integer():

		continue

	else:  # this part uses the algorithm for finding periods of continued square root functions
		a = int(math.sqrt(n)) 

		b = n

		c = b - a**2

		if c == 1:

			oddcount += 1

			continue

		for e in range(0,5000): #No period should be longer than 5000

			
			d = int((math.sqrt(b)+a)/c)

			f = abs(a - c * d)

			a = f

			c = int((b-a**2)/c)			

			if c == 1:

				if e % 2 != 0:

					oddcount += 1

				break

			
						

print(oddcount)

os.system('pause')






