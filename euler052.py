'''Solution to Project Euler Problem 51
Code by Timothy Virgil Payne Jr.
Started: 5/19/22
Completed: 5/19/22
https://projecteuler.net/problem=52'''


def dig_count(num):
    'Find number of each digit'
    str_num = str(num)
    dig_dict = {str(a): str_num.count(str(a)) for a in range(10)}
    return dig_dict


# hunt for our number
for p in range(1, 1000000):
    curr_dict = dig_count(p)

    for x in range(2, 7):
        test_num = p * x
        test_dict = dig_count(test_num)
        if test_dict == curr_dict:
            continue
        else:
            break
    else:
        print(p)
        break
