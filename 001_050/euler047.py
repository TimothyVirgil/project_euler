'''Solution to Project Euler Problem 47
Code by Timothy Virgil Payne Jr.
Started: 1/25/22
Completed: 2/3/22
'''

'''
1. Generate Prime factorization dictionary
2. Iterate through numbers, if dictionary has exactly 5 keys (original with 4 factors), enumerate counter
3. When we hit 4, return the number.'''

import path
import sys
directory = path.Path(__file__).abspath()
sys.path.append(directory.parent.parent)

from utils import prime_factorization, timer

@timer
def solve():
    pf_count = 0
    num_list = []
    check_num = 4

    while pf_count < 4:
        curr_fact = prime_factorization(check_num)
        if len(curr_fact) == 5:
            pf_count += 1
            num_list.append(check_num)
            check_num += 1
        else:
            pf_count = 0
            num_list = []
            check_num += 1

    print(num_list[0])

if __name__ == "__main__":
    solve()