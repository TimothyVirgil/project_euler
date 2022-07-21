'''General use functions for Euler problems'''

from typing import Callable
import math
import time
from fractions import Fraction

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

    def inner_func(*args, **kwargs):
        start = time.time()
        run = func()
        print(f'total time: {(time.time()-start):3f} seconds')
        return run

    return inner_func


def continued_fractions(x: int) -> list[int, int, list[int]]:
    '''Returns a list where:
    first element: radicand
    second element: root integer
    third element: list of continued fractions
    Check https://projecteuler.net/problem=64 for more info.'''

    cont_frac = ''
    if math.sqrt(x).is_integer():
        cont_frac = [x, 0, []]
        return cont_frac
    else:
        a = int(math.sqrt(x))
        b = int((math.sqrt(x)+a)/(x-a**2))
        cont_frac = [x, a, [b]]
        if x - a**2 == 1 and a - b * x + b * a**2 == -a:
            return cont_frac
        u = a - b * x + b * a**2
        v = x - a**2
        while v != 1 or u != -a:
            c = int(((math.sqrt(x)-u)/((x-u**2)/v)))
            v = int((x-u**2)/v)
            u = -u - c * v
            cont_frac[2].append(c)
        return cont_frac


def find_convergents(rad: int, n:int) -> Fraction:
    '''For a square root, return the nth convergent fraction'''

    con = continued_fractions(rad)
    curr = 0
    con_len = len(con[2])
    for a in range(n-2, -1, -1):        
        curr = Fraction(1, con[2][a % con_len] + curr)      
    return con[1] + curr