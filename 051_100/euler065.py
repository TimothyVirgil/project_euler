'''Solution to Project Euler Problem 63
Code by Timothy Virgil Payne Jr.
Started: 7/21/22
Completed: 7/21/22
https://projecteuler.net/problem=65'''

import sys
import path
directory = path.Path(__file__).abspath()
sys.path.append(directory.parent.parent)
from utils import timer, continued_fractions


@timer
def solve():
    numeratorlist = [2, 3, 8]
    for b in range(2, 35):
        numeratorlist.append(numeratorlist[-2]+numeratorlist[-1])
        numeratorlist.append(numeratorlist[-2]+numeratorlist[-1])
        numeratorlist.append(numeratorlist[-1]*2*b+numeratorlist[-2])
    digsum = 0
    for c in range(0, len(str(numeratorlist[99]))):
        digsum += int(str(numeratorlist[99])[c])
    return digsum


if __name__ == "__main__":
    ans = solve()
    print(f"The answer is {ans}.")
