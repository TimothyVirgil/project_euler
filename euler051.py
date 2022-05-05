'''Solution to Project Euler Problem 51
Code by Timothy Virgil Payne Jr.
Started: 3/29/22
Completed:
https://projecteuler.net/problem=51

What will happen here is that we will have some smallest prime which will
form a finite arithmetic sequence of at most ten numbers which at least 8
will have to be prime.

Obviously we can't change the ones digit, as that will result in and even.

This means the difference in the sequence will be some type of factor of 10.
Since we will be iterating the selected digits by 1, the differences will be
of the form 1010, 100100, 10010, etc.

Whatever our difference is, we will need to add it 9, 8, or 7 times
and result in 8 primes.

Ff the difference itself does not divide 3, every third time we add it we'll
hit a number divisible by 3.

Our difference must therefor divide 3 and 10.

Our difference must also divide 7. If it doesn't, after 6 additions, we will
hit a multiple of 7.

After 8 additions, we'll reach a a multiple of 9, but it may be possible to
hit 8 primes by just accoutning for 3 and 7.

So, we're looking for a number that divides, 3, 7, and 10 and only has ones
and zeros in its digits.

3*7*10 = 210

The first script tells us the smallest number that satisifies this is
101010.

The second script scans six digit numbers for the first sequence of
8 primes.'''

from primecheck import primecheck

not_found = True
a = 1
while not_found:
    test = 210 * a
    for dig in str(test):
        if dig != '1' and dig != '0':
            a += 1
            break
    else:
        diff = test
        not_found = False

for a in range(100001, 1000000, 2):
    if primecheck(a) and str(a)[0] == str(a)[2] == str(a)[4]:
        success = 1
        for b in range(9):
            test_prime = a + (b+1) * diff
            if primecheck(test_prime) and test_prime < 1_000_000:
                success += 1
        if success >= 8:
            print(a)
            break
