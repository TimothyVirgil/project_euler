'''Solution to Project Euler Problem 50
Code by Timothy Virgil Payne Jr.
Started: 2/17/22
Completed: 2/17/22
https://projecteuler.net/problem=50
'''

from primecheck import primecheck

prime_list = [i for i in range(2, 1_000_000) if primecheck(i)]

# The length is 78498
prime_len = len(prime_list)

# The sum of the first 547 primes is over 1_000_000
# So our series has at most 546 numbers
prime_sum_search = True

while prime_sum_search:

    for a in range(546):
        if not prime_sum_search:
            break

        for b in range(a+1):
            last_prime_ind = b + 546 - a
            prime_sum = sum(prime_list[b: last_prime_ind])
            if prime_sum > 1_000_000:
                break
            if primecheck(prime_sum) and prime_sum < 1_000_000:
                print(prime_sum)
                prime_sum_search = False
                break
