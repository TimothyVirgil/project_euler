'''Solution to Project Euler Problem 60
Code by Timothy Virgil Payne Jr.
Started: 6/30/22
Completed: 7/18/22
https://projecteuler.net/problem=60
'''


from itertools import combinations
import path
import sys
directory = path.Path(__file__).abspath()
sys.path.append(directory.parent.parent)
from utils import timer, primecheck


def prime_concat_check(primes: tuple[int]) -> bool:
    pairs = combinations(primes, 2)
    # do not allow duplicates
    if len(set(primes)) < len(primes):
        return False
    for pair in pairs:
        num1 = str(pair[0])
        num2 = str(pair[1])
        if primecheck(int(num1+num2)) and primecheck(int(num2+num1)):
            continue
        else:
            return False
    else:
        return True


@timer
def solve():
    a = 7
    ans_dict = {3: []}
    while a < 10_000:
        if primecheck(a):
            ans_dict[a] = []
            temp_list = []
            for key in ans_dict.keys():
                if prime_concat_check((key, a)):
                    temp_list.append(key)
                    ans_dict[key].append((a,))
            for num in temp_list:
                item_tups = []
                for item in ans_dict[num]:
                    for elem in item:
                        if elem in temp_list:
                            continue
                        else:
                            break
                    else:
                        if len(item + (a,)) == 4:
                            five_concats = ((num,) + (item + (a,)))
                            return(five_concats, sum(five_concats))
                        item_tups.append(item + (a,))
                ans_dict[num].extend(item_tups)
        a += 2


if __name__ == '__main__':
    ans = solve()
    print(f'The sum is {ans[1]}.')
