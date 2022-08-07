'''Solution to Project Euler Problem 73
Code by Timothy Virgil Payne Jr.
Started: 8/6/22
Completed: 8/6/22
https://projecteuler.net/problem=73
'''

import sys
import path
directory = path.Path(__file__).abspath()
sys.path.append(directory.parent.parent)
from utils import timer, prime_factorization, primecheck


@timer
def solve():
    frac_count = 0
    for x in range(12_000, 2, -1):
        num_floor = x//3
        if num_floor * 3 <= x:
            num_floor += 1
        num_ceil = x//2
        if num_ceil * 2 <= x:
            num_ceil += 1
        if primecheck(x):
            frac_count += (num_ceil - num_floor)
            continue
        else:
            prime_fact_x = prime_factorization(x)['factors'].keys()
            for a in range(num_floor, num_ceil):
                for key in prime_fact_x:
                    if a % key == 0:
                        break
                    else:
                        continue
                else:
                    frac_count += 1
    else:
        return frac_count


if __name__ == "__main__":
    ans = solve()
    print(f'The answer is {ans}.')
