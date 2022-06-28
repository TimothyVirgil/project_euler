'''General use functions for Euler problems'''

from typing import Callable

'''script to import utils:
import path
import sys
directory = path.Path(__file__).abspath()
sys.path.append(directory.parent.parent)
'''


def primecheck(a: int) -> bool:
    'This function checks to see if an integer is prime.'

    if a == 2 or a == 3:
        return True
    elif a < 2 or a % 2 == 0:
        return False
    else:
        for b in range(3, int(a**(0.5)) + 2, 2):
            if a % b == 0:
                return False
            else:
                continue
        else:
            return True


def prime_factorization(num: int) -> dict:
    '''Return a dictionary with the prime factors as keys
    and their exponents as values.'''

    pf_dict = {'number': num}

    # if prime... done
    if primecheck(num):
        return pf_dict

    else:
        # case: even num
        if num % 2 == 0:
            num = num // 2
            pf_dict[2] = 1

            while num % 2 == 0:
                pf_dict[2] += 1
                num = num // 2

    # case: odd composite num
        else:
            for a in range(3, int(num**(0.5)) + 2, 2):
                if num % a == 0:
                    pf_dict[a] = 1
                    num = num // a
                    break

        if num == 1:
            return pf_dict

        # number must be odd at this point
        while not (primecheck(num) or num == 1):
            for a in range(3, int(num**0.5)+2, 2):
                if num % a == 0:
                    if a in pf_dict:
                        # if factor exists iterate its exponent
                        pf_dict[a] += 1
                        num = num // a

                    else:
                        # initial factor
                        pf_dict[a] = 1
                        num = num // a

        else:
            if num == 1:
                return pf_dict
            else:
                if num in pf_dict:
                    # if factor exists
                    pf_dict[num] += 1
                    return pf_dict

                else:
                    pf_dict[num] = 1
                    return pf_dict


def timer(func: Callable) -> Callable:
    '''Decorator to time functions'''

    import time

    def inner_func(*args, **kwargs):
        start = time.time()
        func()
        print('total time: {} seconds'.format((time.time()-start)))

    return inner_func
