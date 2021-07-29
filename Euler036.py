'''Solution to Project Euler Problem 36
Code by Timothy Virgil Payne Jr.
Started: 7/28/21
Completed: 7/28/21

In my old solution I didn't make use of Python's bin function... lol'''

def pal_checker_dec(a):

    str_num = str(a)
    rev_num = ''

    for x in range((len(str_num)-1), -1, -1):
        rev_num += str_num[x]

    if str_num == rev_num:
        return True

    else:
        return False

def pal_checker_bin(b):

    str_bin = str(b)
    str_bin = str_bin[2:]
    rev_bin = ''

    for x in range((len(str_bin)-1), -1, -1):
        rev_bin += str_bin[x]

    if rev_bin == str_bin:
        return True

    else:
        return False

pal_sum = 0

for x in range(1,1_000_000,2): #only need odds since binaries must end in 1

    if x % 10 == 0:
        continue
    
    elif pal_checker_dec(x):

        if pal_checker_bin(bin(x)):
            pal_sum += x
            continue

print(pal_sum)
