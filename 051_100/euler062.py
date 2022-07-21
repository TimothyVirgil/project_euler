'''Solution to Project Euler Problem 62
Code by Timothy Virgil Payne Jr.
Started: 7/21/22
Completed: 7/21/22
https://projecteuler.net/problem=62

I used a dictionary of digits here.
It seems like sorting the digits as strings and doing a count
would have been quicker and more elegant.'''

import path
import sys
directory = path.Path(__file__).abspath()
sys.path.append(directory.parent.parent)
from utils import timer


def dig_dic(num):
    str_num = str(num)
    count_dic = {}
    count_dic['count'] = {x: str_num.count(str(x)) for x in range(10)}
    count_dic['nums'] = [str_num]
    return count_dic


@timer
def solve():
    list_of_num_dics = []
    curr_len = 0
    for x in range(0, 200000):
        new_len = len(str(x))
        if new_len > curr_len:
            list_of_num_dics = []
            curr_len = new_len
        cube = x**3
        curr_dic = dig_dic(cube)

        for dicts in list_of_num_dics:
            if curr_dic['count'] == dicts['count']:
                dicts['nums'].append(curr_dic['nums'])
                if len(dicts['nums']) == 5:
                    return (dicts['nums'])
                break
        else:
            list_of_num_dics.append(curr_dic)


if __name__ == "__main__":
    ans = solve()
    print(f'The answer is {ans[0]}.')
