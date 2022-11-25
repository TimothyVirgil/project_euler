'''Solution to Project Euler Problem 77
Code by Timothy Virgil Payne Jr.
Started: 11/25/22
Completed: 11/25/22
https://projecteuler.net/problem=77'''

import sys
import path
directory = path.Path(__file__).abspath()
sys.path.append(directory.parent.parent)
from utils import primecheck
from utils import timer


@timer
def solve():

    sum_dic = {0: {}, 1: {}, 2: {}, 3: {}}
    primelist = [3, 2]
    a = 4
    curr_sum = 0
    while curr_sum <= 5_000:
        if primecheck(a):
            primelist.insert(0, a)
        sum_dic[a] = {}
        for b in primelist:
            if b == 2 and a % 2 != 0:
                sum_dic[a][2] = 0
                break
            elif b == 2 and a % 2 == 0:
                sum_dic[a][2] = 1
                break
            elif b == a-2 or b == a-3:
                sum_dic[a][b] = 1

            elif 2*b >= a:
                if a-b in primelist:
                    sum_dic[a][b] = sum(sum_dic[a-b].values()) + 1
                else:
                    sum_dic[a][b] = sum(sum_dic[a-b].values())
            else:
                sum_dic[a][b] = sum([sum_dic[a-b][x]
                                    for x in filter(lambda x: x <= b, primelist)])

        this_sum = sum(sum_dic[a].values())
        curr_sum = max(curr_sum, this_sum)
        a += 1
    return a-1


if __name__ == '__main__':
    ans = solve()
    print(f'The answer is {ans}.')
