'''Solution to Project Euler Problem 56
Code by Timothy Virgil Payne Jr.
Started: 6/20/22
Completed: 6/20/22
https://projecteuler.net/problem=56'''


def digit_sum(num: int) -> int:
    '''Find the sum of the digits of a number'''
    str_num = str(num)
    sum = 0
    for x in range(len(str_num)):
        sum += int(str_num[x])

    return sum


curr_sum = 0
max_sum = 0

for x in range(1, 100):
    for y in range(1, 100):
        num = x ** y
        curr_sum = digit_sum(num)
        if curr_sum > max_sum:
            max_sum = curr_sum

print(max_sum)
