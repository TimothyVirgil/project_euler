'''Solution to Project Euler Problem 61
Code by Timothy Virgil Payne Jr.
Started: 7/19/22
Completed: 7/19/22
https://projecteuler.net/problem=61

Start by doing some hand calculations to find the range of "n" to generate
4 digit numbers.

I don't love the nested loops but it does work quickly.
'''
from itertools import permutations
import path
import sys
directory = path.Path(__file__).abspath()
sys.path.append(directory.parent.parent)
from utils import timer


def cycle_match(num1: str, num2: str) -> bool:
    if num1[0:2] == num2[2:4]:
        return True
    else:
        return False


@timer
def solve():

    tri_list = [int((a**2+a)/2) for a in range(45, 141)]
    sq_list = [a**2 for a in range(32, 100)]
    pent_list = [int((a*(3*a-1))/2) for a in range(26, 82)]
    hex_list = [a*(2*a-1) for a in range(23, 71)]
    hept_list = [int(a*(5*a-3)/2) for a in range(21, 64)]
    oct_list = [a*(3*a-2) for a in range(19, 59)]

    poss_order = permutations(
        [tri_list, sq_list, pent_list, hex_list, hept_list, oct_list])

    for order in poss_order:
        for first_num in order[0]:
            for sec_num in order[1]:
                if not cycle_match(str(first_num), str(sec_num)):
                    continue
                else:
                    for thir_num in order[2]:
                        if not cycle_match(str(sec_num), str(thir_num)):
                            continue
                        else:
                            for four_num in order[3]:
                                if not cycle_match(str(thir_num), str(four_num)):
                                    continue
                                else:
                                    for five_num in order[4]:
                                        if not cycle_match(str(four_num), str(five_num)):
                                            continue
                                        else:
                                            for six_num in order[5]:
                                                if (cycle_match(str(five_num), str(six_num))
                                                        and cycle_match(str(six_num), str(first_num))):
                                                    return (first_num, sec_num, thir_num,
                                                            four_num, five_num, six_num)
                                                else:
                                                    continue


if __name__ == "__main__":
    ans = solve()
    print(f'The sum of the six numers is {sum(ans)}.')
