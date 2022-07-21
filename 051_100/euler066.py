'''Solution to Project Euler Problem 66
Code by Timothy Virgil Payne Jr.
Started: 7/21/22
Completed: 7/21/22
https://projecteuler.net/problem=66

Reference: https://mathworld.wolfram.com/PellEquation.html'''


from fractions import Fraction
import sys
import path
directory = path.Path(__file__).abspath()
sys.path.append(directory.parent.parent)
from utils import timer, continued_fractions


def find_convergents(rad: int, n: int) -> Fraction:

    con = continued_fractions(rad)
    curr = 0
    con_len = len(con[2])
    for a in range(n-2, -1, -1):
        curr = Fraction(1, con[2][a % con_len] + curr)
    return con[1] + curr


@timer
def solve():
    max_d = (0, 0)
    for a in range(2, 1000):
        conv = continued_fractions(a)
        conv_len = len(conv[2])
        if conv_len % 2 == 0:
            test = find_convergents(a, conv_len)
            if test.numerator > max_d[1]:
                max_d = (a, test.numerator)
        else:
            test = find_convergents(a, 2 * conv_len)
            if test.numerator > max_d[1]:
                max_d = (a, test.numerator)

    return(max_d)


if __name__ == "__main__":
    ans = solve()
    print(f"The answer is {ans[0]}")
