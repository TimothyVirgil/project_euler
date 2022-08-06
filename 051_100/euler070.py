'''Solution to Project Euler Problem 70
Code by Timothy Virgil Payne Jr.
Started: 8/6/22
Completed: 8/6/22
https://projecteuler.net/problem=70
'''

from itertools import combinations
from fractions import Fraction
import sys
import path
directory = path.Path(__file__).abspath()
sys.path.append(directory.parent.parent)
from utils import timer, primecheck, prime_factorization


''' We can assume the number with a minimum will likely be a perfect square or
the product of two primes. A quick test shows there are no perfect squares that
fulfill the permutation property so we can make a test for large primes.
It's slightly guessy, but it works.
 I have a brute force way that takes 90 seconds, this way takes 2.'''


def totient(n):
    primes = prime_factorization(n)['factors'].keys()
    if len(primes) == 0:
        return n-1
    else:
        mult = 1
        for a in primes:
            mult *= (1-Fraction(1, a))
        return int(n * mult)


def perm_check(a, b):
    str_a = str(a)
    str_b = str(b)
    return sorted(str_a) == sorted(str_b)


@timer
def solve():
    high_primes = []
    for a in range(2001, 4000, 2):
        if primecheck(a):
            high_primes.append(a)
    poss_ans = combinations(high_primes, 2)
    mindiv = 2
    currmin = 0
    for b in poss_ans:
        poss_num = b[0] * b[1]
        if poss_num < 10_000_000:
            curr_tot = totient(poss_num)
            if perm_check(curr_tot, poss_num):
                if poss_num/curr_tot < mindiv:
                    mindiv = poss_num/curr_tot
                    currmin = poss_num

    return currmin


if __name__ == "__main__":
    ans = solve()
    print(f'The answer is {ans}.')
