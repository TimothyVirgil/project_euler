'''Solution to Project Euler Problem 72
Code by Timothy Virgil Payne Jr.
Started: 8/6/22
Completed: 8/6/22
https://projecteuler.net/problem=72
'''

import sys
import path
directory = path.Path(__file__).abspath()
sys.path.append(directory.parent.parent)
from utils import timer, totient


@timer
def solve():
    total_elem = 0
    for a in range(2, 1_000_001):
        total_elem += totient(a)
    else:
        return total_elem


if __name__ == "__main__":
    ans = solve()
    print(f'The answer is {ans}.')
