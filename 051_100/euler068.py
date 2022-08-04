'''Solution to Project Euler Problem 68
Code by Timothy Virgil Payne Jr.
Started: 7/28/22
Completed: 7/28/22
https://projecteuler.net/problem=68
'''

import sys
import path
directory = path.Path(__file__).abspath()
sys.path.append(directory.parent.parent)
from utils import timer
from itertools import permutations


@timer
def solve():

    all_perms = permutations(range(1, 11))
    poss_perms = []

    for perm in all_perms:
        a, b, c, d, e, f, g, h, i, j = perm[0], perm[1], perm[2], perm[
            3], perm[4], perm[5], perm[6], perm[7], perm[8], perm[9]

        s = a + b + c

        if d + c + e != s:
            continue
        else:
            if f + e + g != s:
                continue
            else:
                if h + g + i != s:
                    continue
                else:
                    if j + i + b != s:
                        continue
                    else:
                        poss_perms.append(perm)

    max_poss = 0

    for perm in poss_perms:
        a, b, c, d, e, f, g, h, i, j = perm[0], perm[1], perm[2], perm[
            3], perm[4], perm[5], perm[6], perm[7], perm[8], perm[9]

        order_dict = {a: (a, b, c, d, c, e, f, e, g, h, g, i, j, i, b),
                      d: (d, c, e, f, e, g, h, g, i, j, i, b, a, b, c),
                      f: (f, e, g, h, g, i, j, i, b, a, b, c, d, c, e),
                      h: (h, g, i, j, i, b, a, b, c, d, c, e, f, e, g),
                      j: (j, i, b, a, b, c, d, c, e, f, e, g, h, g, i)}

        min_node = min(a, d, f, h, j)
        curr_order = order_dict[min_node]
        curr_str = ''
        for item in curr_order:
            curr_str += str(item)
        if len(curr_str) != 16:
            continue
        else:
            test_max = int(curr_str)
            if test_max > max_poss:
                max_poss = test_max

    return max_poss


if __name__ == "__main__":
    ans = solve()
    print(f'The answer is {ans}.')
