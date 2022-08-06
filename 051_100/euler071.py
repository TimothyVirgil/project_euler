'''Solution to Project Euler Problem 71
Code by Timothy Virgil Payne Jr.
Started: 8/6/22
Completed:
https://projecteuler.net/problem=71
'''


from fractions import Fraction
import sys
import path
directory = path.Path(__file__).abspath()
sys.path.append(directory.parent.parent)
from utils import timer


@timer
def solve():
    curr_max = 0
    for a in range(1_000_000, 1, -1):
        check = (3*a)//7
        curr_fract = Fraction(check, a)
        if (curr_fract > curr_max) and (curr_fract < Fraction(3, 7)):
            curr_max = curr_fract
    return curr_max.numerator


if __name__ == "__main__":
    ans = solve()
    print(f'The answer is {ans}.')
