'''Solution to Project Euler Problem 69
Code by Timothy Virgil Payne Jr.
Started: 7/28/22
Completed: 8/6/22
https://projecteuler.net/problem=69
'''

import sys
import path
from math import prod
directory = path.Path(__file__).abspath()
sys.path.append(directory.parent.parent)
from utils import primecheck


def solve():
    a = 2
    curr_prod = 1
    prime_list = []
    while curr_prod < 1_000_000:
        if primecheck(a):
            prime_list.append(a)
            curr_prod = prod(prime_list)
        a += 1
    return curr_prod//prime_list[-1]


if __name__ == '__main__':
    ans = solve()
    print(f'The answer is {ans}.')
