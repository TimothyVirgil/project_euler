'''Solution to Project Euler Problem 46
Code by Timothy Virgil Payne Jr.
Started: 1/20/22
Completed: 1/20/22
'''

import path
import sys
directory = path.Path(__file__).abspath()
sys.path.append(directory.parent.parent)
from utils import primecheck


def squarecheck(num):
    if ((num/2)**0.5).is_integer():
        return True
    else:
        return False


def comp_prime_builder(test_num):

    while primecheck(test_num):
        primes.append(test_num)
        test_num += 2

    else:
        for prime in primes:
            check_num = test_num - prime
            if squarecheck(check_num):
                return False, test_num
            else:
                continue
        else:
            return True, test_num


def solve():
    global primes
    primes = [2, 3, 5, 7]
    curr_num = 9

    curr_res = comp_prime_builder(curr_num)
    while curr_res[0] is False:
        curr_num = curr_res[1] + 2
        curr_res = comp_prime_builder(curr_num)

    else:
        print(curr_res[1])


if __name__ == "__main__":
    solve()
