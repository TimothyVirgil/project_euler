#Euler 66

# solutions are of the form psubn = x and q sub n = y where psubn/qsubn in the nth convergent of root(D)
import math
import os

xlist = []
xdict = {}

def x_solution(x):

	global xlist
	global xdict

	alist = []

	plist = []

	a = int(math.sqrt(x))

	b = int((math.sqrt(x)+a)/(x-a**2))

	alist = [a,b]

	plist = [a,a * b + 1]

	if x - a**2 == 1 and a - b * x + b * a**2 == -a:

		xlist += [plist[-1]]

		xdict[plist[-1]] = x

		return

	u = a - b * x + b * a**2

	v = x - a**2

	while v != 1 or u != -a:

		c = int(((math.sqrt(x)-u)/((x-u**2)/v)))

		v = int((x-u**2)/v)

		u = -u - c * v

		alist += [c]

		plist += [c*plist[-1] + plist[-2]]

	xlist += [plist[-1]]

	xdict[plist[-1]] = x


for c in range(0,1001):

	if math.sqrt(c).is_integer():
		continue

	else:

		x_solution(c)


print(xdict[max(xlist)])

print(xdict)

os.system('pause')