# Euler 64: Square Fractions

import math
import os

oddcount = 0 #Tally odd periods

for n in range(0,10001):

	print(n)

	oddcount = 0
	
	if math.sqrt(n).is_integer():

		continue

	else:
		a = int(math.sqrt(n))

		b = n

		c = (b-a**2)
		
		for e in range(0,5000): #Algorithm for finding the first term			

			d = int((math.sqrt(n)+a)/c)			 		
						
			e = abs(a - c * d)

			a = e

			c = int((b-a**2)/c)

print(oddcount)

os.system('pause')






