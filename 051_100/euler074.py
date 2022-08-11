'''Solution to Project Euler Problem 74
Code by Timothy Virgil Payne Jr.
Started: 8/11/22
Completed: 8/11/22
https://projecteuler.net/problem=74
'''

from math import factorial
import sys
import path
directory = path.Path(__file__).abspath()
sys.path.append(directory.parent.parent)
from utils import timer


def find_loop(num, num_list=None) -> int:
    num_sum = 0
    if num_list is None:
        num_list = [num]
    for digit in str(num):
        num_sum += factorial(int(digit))
    if num_sum not in num_list:
        num_list.append(num_sum)
        return find_loop(num_sum, num_list)
    else:
        return len(num_list)


@timer
def solve():
    sixty_sum = 0
    for a in range(0, 1_000_000):
        if find_loop(a) == 60:
            sixty_sum += 1
    return sixty_sum


if __name__ == "__main__":
    ans = solve()
    print(f'The answer is {ans}.')
