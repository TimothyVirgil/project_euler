'''Solution to Project Euler Problem 78
Code by Timothy Virgil Payne Jr.
Started: 12/2/22
Completed: 12/19/22
https://projecteuler.net/problem=78
This solution uses the pentagonal number theorem'''


import sys
import path
directory = path.Path(__file__).abspath()
sys.path.append(directory.parent.parent)
from utils import timer


@timer
def solve():

    pent_list = [1]
    partition_dict = {0: 1}

    def generalized_pentagonal_numbers(n: int) -> int:
        '''Find the nth generalized pentagonal number'''
        if n % 2 == 0:
            k = -(n//2)
        else:
            k = (n+1)//2
        pent = k*(3*k-1)//2
        return pent

    found_ans = False
    a = 1

    while not found_ans:

        curr_p = 0
        add_sub = 1
        num_tik = 0

        # Use the pentagonal number theorem to recursively find p(n)
        # for the partition function
        for pent in pent_list:

            if a - pent >= 0:

                if add_sub == 1:
                    curr_p += partition_dict[a-pent]
                    num_tik += 1

                    if num_tik == 2:
                        add_sub *= -1
                        num_tik = 0
                else:
                    curr_p -= partition_dict[a-pent]
                    num_tik += 1

                    if num_tik == 2:
                        add_sub *= -1
                        num_tik = 0
            else:
                break
        else:
            # add a number to the pentagonal list if I had some leftover.
            # This is probably not the most efficient... but it works!
            pent_len = len(pent_list)
            pent_list.append(generalized_pentagonal_numbers(pent_len+1))

        partition_dict[a] = curr_p

        if curr_p % 1_000_000 == 0:
            return (a)

        # iterate until we find our answer
        else:
            a += 1


if __name__ == '__main__':
    ans = solve()
    print(f'The answer is {ans}.')
