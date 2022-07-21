'''Solution to Project Euler Problem 63
Code by Timothy Virgil Payne Jr.
Started: 7/21/22
Completed: 7/21/22
https://projecteuler.net/problem=63

'''
import sys
import path
directory = path.Path(__file__).abspath()
sys.path.append(directory.parent.parent)
from utils import timer


@timer
def solve():
    dig_count = 0
    for a in range(0, 100):
        for b in range(0, 50):
            c = b**a
            if c < (10**(a-1)):
                continue
            if c >= (10**a):
                break
            else:
                dig_count += 1
    return dig_count


if __name__ == "__main__":
    ans = solve()
    print(f'The answer is {ans}.')
