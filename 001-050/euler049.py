'''Solution to Project Euler Problem 49
Code by Timothy Virgil Payne Jr.
Started: 2/10/22
Completed: 2/10/22
'''

import itertools
from primecheck import primecheck


def iter_arim_prime_check(prime):

    '''Create lists of permutated primes'''
    iter_list = []
    prime_iters = itertools.permutations(str(prime))
    iter_list = [int(''.join(tups)) for tups in prime_iters if primecheck(int(''.join(tups)))]
    iter_list = list(set(iter_list))
    iter_list.remove(prime)

    for poss_num in iter_list:
        poss_diff = abs(prime - poss_num)
        for poss_num2 in iter_list:
            if poss_num2 == poss_num:
                continue
            else:
                poss_diff2 = abs(poss_num-poss_num2)
                if poss_diff2 == poss_diff:                    
                    answer = sorted([prime, poss_num, poss_num2])
                    answer = [str(x) for x in answer]
                    answer = ''.join(answer)
                    if len(answer) == 12 and int(answer) != 148748178147:
                        return int(answer)
                else:
                    continue

for a in range(1001,10000,2):
    if primecheck(a):
        curr_check = iter_arim_prime_check(a)
        if curr_check and curr_check != 148748178147:
            print(iter_arim_prime_check(a))
            break
        