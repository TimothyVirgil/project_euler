'''Solution to Project Euler Problem 34
Code by Timothy Virgil Payne Jr.
Started: 7/15/21
Completed: 7/15/21

They don't specify an upper limit here but there clearly must be one.

We can examine the single digit factorials to figure this out:

1! = 1
2! = 2
3! = 6
4! = 24
5! = 120
6! = 720
7! = 5,040
8! = 40,320
9! = 362,880

362,880 * 8 = 2,903,040
362,880 * 7 = 2,540,160
362,880 * 6 = 2,000,000

So the upper limit is definitely below 2,540,160. That is not our true upper limit
but with modern processor power, it should be close enough to make the brute force trivial.

Ok, this takes about 5 seconds so it's not totally trivial.
'''

from math import factorial
fac_sum = 0

for a in range(3,2_540_160):
	fac_num = str(a)
	temp_sum = 0

	for b in fac_num:
		temp_sum += factorial(int(b))

	else:
		if temp_sum == a:
			fac_sum += temp_sum


print(fac_sum)




