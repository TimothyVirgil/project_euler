'''Solution to Project Euler Problem 58
Code by Timothy Virgil Payne Jr.
Started: 6/28/22
Completed: 6/28/22
https://projecteuler.net/problem=58'''

import path
import sys
from fractions import Fraction
directory = path.Path(__file__).abspath()
sys.path.append(directory.parent.parent)
from utils import primecheck, timer


@timer
def solve():
    '''Use simple formulas for the diagonals of each square'''
    total_nums = 5
    total_primes = 3
    prime_rat = Fraction(total_primes, total_nums)
    curr_square = 3

    while prime_rat > Fraction(1, 10):
        curr_square += 2
        total_nums += 4
        diag1 = curr_square ** 2
        diag2 = diag1 - (curr_square - 1)
        diag3 = diag2 - (curr_square - 1)
        diag4 = diag3 - (curr_square - 1)
        diags = diag1, diag2, diag3, diag4

        for diag in diags:
            if primecheck(diag):
                total_primes += 1
            else:
                continue

        prime_rat = Fraction(total_primes, total_nums)

    print(curr_square)


if __name__ == '__main__':
    solve()
