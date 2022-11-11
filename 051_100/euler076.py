'''Solution to Project Euler Problem 76
Code by Timothy Virgil Payne Jr.
Started: 10/7/22
Completed: 11/11/22
https://projecteuler.net/problem=76'''

import sys
import path
directory = path.Path(__file__).abspath()
sys.path.append(directory.parent.parent)
from utils import timer


@timer
def solve():

    sum_dic = {}

    for a in range(2, 101):
        sum_dic[a] = {}
        for b in range(a-1, 0, -1):
            if b == a-1:
                sum_dic[a][b] = 1
            elif b == 1:
                sum_dic[a][1] = 1
                break
            elif 2*b >= a:
                sum_dic[a][b] = sum(sum_dic[a-b].values()) + 1

            else:
                sum_dic[a][b] = sum([sum_dic[a-b][x] for x in range(b, 0, -1)])

    return sum(sum_dic[100].values())


if __name__ == '__main__':
    ans = solve()
    print(f'The answer is {ans}.')
