'''Solution to Project Euler Problem 41
Code by Timothy Virgil Payne Jr.
Started: 12/9/21
Completed: 12/9/21

Straightforward. My code in the "old solutions" folder is pretty ghastly for this one ha.
The second attempt in my old folder is actually faster but the code is a monstrosity'''

from itertools import permutations

def pan_generator():
    poss_pans = permutations(['0','1','2','3','4','5','6','7','8','9'], 10)
    for i in poss_pans:
        if i[0] == '0':
            continue
        elif int(i[7]+i[8]+i[9]) % 17 != 0:
            continue
        elif int(i[6]+i[7]+i[8]) % 13 != 0:
            continue
        elif int(i[5]+i[6]+i[7]) % 11 != 0:
            continue
        elif int(i[4]+i[5]+i[6]) % 7 != 0:
            continue
        elif int(i[3]+i[4]+i[5]) % 5 != 0:
            continue
        elif int(i[2]+i[3]+i[4]) % 3 != 0:
            continue
        elif int(i[3]) % 2 != 0:
            continue        
        else:
            num = ''
            for a in i:
                num += a
            yield int(num)

find_pans = pan_generator()
pan_sum = 0
for a in find_pans:
    pan_sum += a

print(pan_sum)
