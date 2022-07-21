'''Solution to Project Euler Problem 63
Code by Timothy Virgil Payne Jr.
Started: 7/21/22
Completed: 7/21/22
https://projecteuler.net/problem=64'''

import sys
import path
directory = path.Path(__file__).abspath()
sys.path.append(directory.parent.parent)
from utils import timer, continued_fractions

@timer
def solve():

    num_odd = 0
    for x in range(2, 10001):
        rep = continued_fractions(x)
        if len(rep[2]) % 2 != 0:
            num_odd += 1

    return num_odd


if __name__ == "__main__":
    ans = solve()
    print(f'The answer is {ans}.')
