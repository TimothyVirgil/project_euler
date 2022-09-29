'''Solution to Project Euler Problem 75
Code by Timothy Virgil Payne Jr.
Started: 9/1/22
Completed: 9/29/22
https://projecteuler.net/problem=75'''

from math import gcd
import pandas as pd
import sys
import path
directory = path.Path(__file__).abspath()
sys.path.append(directory.parent.parent)
from utils import timer


def triple_gen(m: int, n: int) -> int:
    '''Return the perimiter of pythagorean triple
    using Euclid's formula'''
    a = m**2 - n**2
    b = 2*m*n
    c = m**2 + n**2
    return a+b+c


@timer
def solve():
    p_list = []
    # iter through value 1 for euclid's formula
    for m in range(2, 2_800):
        # iter through value 2 for euclid's formula
        for n in range(1, m):
            # iter through leg 2

            # conditions for primitive tripls
            if (gcd(m, n) == 1 and
                    ((m % 2 == 0 and n % 2 != 0) or
                     (m % 2 != 0 and n % 2 == 0))):
                p = triple_gen(m, n)
                if p > 1_500_000:
                    continue
                else:
                    p_list.append(p)
    perim_list = p_list.copy()
    for p in p_list:
        prod = p
        p += prod
        while p <= 1_500_000:
            perim_list.append(p)
            p += prod
    perim_s = pd.Series(perim_list)
    res = perim_s.drop_duplicates(keep=False)
    return len(res)


if __name__ == '__main__':
    ans = solve()
    print(f'The answer is {ans}.')
