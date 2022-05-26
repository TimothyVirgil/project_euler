'''Solution to Project Euler Problem 53
Code by Timothy Virgil Payne Jr.
Started: 5/26/22
Completed: 5/26/22
https://projecteuler.net/problem=53'''

import math

mill_count = 0

for n in range(23, 101):

    for r in range(1, n):

        comb_count = ((int(math.factorial(n)) /
                       ((int(math.factorial(r))*int(math.factorial(n-r))))))

        if comb_count > 1000000:
            mill_count += 1

print(mill_count)
