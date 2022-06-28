'''Solution to Project Euler Problem 38
Code by Timothy Virgil Payne Jr.
Started: 8/30/21
Completed: 8/30/21

I cleaned/sped up my old solution.
'''
max_conc_prod = 0

for a in range(9, 10_000):  # highest the number could be is 9 thousand something

    num_str = str(a)

    if int(num_str[0]) != 9:  # first digit must be 9
        continue

    else:
        curr_prod = 0
        conc_prod = ''

        for b in range(1, 6):  # n won't be higher than 6
            curr_prod = b*a
            conc_prod = conc_prod+str(curr_prod)

            if len(conc_prod) < 9:
                continue

            elif len(conc_prod) > 9:
                break

            elif len(conc_prod) == 9:

                for b in range(1, 10):

                    if str(b) not in conc_prod:
                        break

                else:
                    if int(conc_prod) > max_conc_prod:
                        max_conc_prod = int(conc_prod)

print(max_conc_prod)
