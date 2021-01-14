Euler 66

def continued(x):   # continued fractions

	cont_frac = ''

	if math.sqrt(x).is_integer():

		cont_frac = f'{x}:'+str(int(math.sqrt(x)))
		return cont_frac

	a = int(math.sqrt(x))

	b = int((math.sqrt(x)+a)/(x-a**2))

	cont_frac = f'{x}:{a};{b}'

	if x - a**2 == 1 and a - b * x + b * a**2 == -a:

		return cont_frac

	u = a - b * x + b * a**2

	v = x - a**2

	while v != 1 or u != -a:

		c = int(((math.sqrt(x)-u)/((x-u**2)/v)))

		v = int((x-u**2)/v)

		u = -u - c * v

		cont_frac += f',{c}'

	return cont_frac


# I will use the above but need to change the function