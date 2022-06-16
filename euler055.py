'''Solution to Project Euler Problem 55
Code by Timothy Virgil Payne Jr.
Started: 6/16/22
Completed: 6/16/22
https://projecteuler.net/problem=55'''


lych_count = 0

for a in range(10, 10_000):
    counter = 0
    curr_num = a
    while counter < 50:
        curr_num = curr_num + int(str(curr_num)[::-1])
        if str(curr_num) == str(curr_num)[::-1]:
            break
        else:
            counter += 1
    else:
        lych_count += 1

print(lych_count)
