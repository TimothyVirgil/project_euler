'''Solution to Project Euler Problem 57
Code by Timothy Virgil Payne Jr.
Started: 6/24/22
Completed: 6/24/22
https://projecteuler.net/problem=57'''

# fractions have a very simple algorithm


def solve():
    prev_numerator = 3
    prev_denominator = 2
    numerator = 7
    denominator = 5
    num_larger = 0

    for a in range(2, 1000):

        (prev_numerator,
         prev_denominator,
         numerator,
         denominator) = (numerator,
                         denominator,
                         numerator*2 + prev_numerator,
                         denominator*2 + prev_denominator)

        if len(str(numerator)) > len(str(denominator)):
            num_larger += 1

    print(num_larger)


if __name__ == "__main__":
    solve()
