# Project Euler

import math
import os
from decimal import *
getcontext().prec=20


dlist = [a for a in range(0,1001)if not math.sqrt(a).is_integer()]



#MY list of D is constructed. Now I need to find the minimum value for x
#where x^2-Dy^2=1 for all D's from 2 to 1001. (in my list)

xlist=[]
highd=0
highx=0


for a in dlist:

	for b in range(1,10000000000):

		if Decimal(a*b**2+1).sqrt() % 1 == 0:

			xlist += [Decimal(a*b**2+1).sqrt()]

			if Decimal(a*b**2+1).sqrt() > highx:

				highx = Decimal(a*b**2+1).sqrt()
				highd = a

			print(a,b,(Decimal(a*b**2+1).sqrt()))



			break

		if b == 9999999999:

			print(a)

print(len(dlist))
print(len(xlist))
print(highd)

os.system('pause')
