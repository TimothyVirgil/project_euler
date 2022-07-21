'''Solution to Project Euler Problem 67
Code by Timothy Virgil Payne Jr.
Started: 7/21/22
Completed: 7/21/22
https://projecteuler.net/problem=67'''

import sys
import path
directory = path.Path(__file__).abspath()
sys.path.append(directory.parent.parent)
from utils import timer


@timer
def solve():
    f = open("p067_triangle.txt")  # open file

    tri_list = []
    for line in f:
        str_line = line.replace(" ", "")
        str_line = str_line.rstrip("\n")
        line_list = []
        for a in range(0, len(str_line), 2):
            num = int(str_line[a] + str_line[a+1])
            line_list.append(num)
        tri_list.append(line_list)
    f.close()
    prev_list = [tri_list[0][0] + tri_list[1]
                 [0], tri_list[0][0] + tri_list[1][1]]

    for a in range(2, len(tri_list)):
        curr_list = []
        curr_list.append(tri_list[a][0] + prev_list[0])
        for b in range(1, len(prev_list)):
            curr_list.append(
                max(prev_list[b-1], prev_list[b]) + tri_list[a][b])
        curr_list.append(tri_list[a][-1] + prev_list[-1])
        prev_list = curr_list

    return(max(curr_list))


if __name__ == "__main__":
    ans = solve()
    print(f'The answer is {ans}.')
