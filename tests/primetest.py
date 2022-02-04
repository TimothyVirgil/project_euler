from primecheck import primecheck
from prime_factorization import prime_factorization
from unittest import TestCase

class Prime_test(TestCase):

    def test_prime(self):
        self.assertTrue(primecheck(431))
