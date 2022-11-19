import unittest

from src.compound_interest import CompoundInterest
from src.compound_interest import *

class CompoundInterestTest(unittest.TestCase):

    # Tests
    def test_interest(self):
       
        P =100
        r = 10
        n = 12
        t = 20
        actual_output = CompoundInterest.formula(P, r, n, t)
        self.assertEqual(732.81, actual_output)


        # A = P(1 + r/n)nt
    # P is the principal amount
    # r is the annual rate of interest
    # t is the number of years the amount is invested
    # n is the number of times the interest is compounded per year
    # A is the amount at the end of the investment

    # Should return 732.81 given 100 principal, 10 percent, 20 years

    # Should return 181.94 given 100 principal, 6 percent, 10 years

    # Should return 149,058.55 given 100000 principal, 5 percent, 8 years

    # Should return 0.00 given 0 principal, 10 percent, 1 year

    # Should return 100.00 given 100 principal, 0 percent, 10 years


    # Extention tests

    # Should return 118,380.16 given 100 principal, 5 percent, 8 years, 1000 per month

    # Should return 156,093.99 given 100 principal, 5 percent, 10 years, 1000 per month

    # Should return 475,442.59 given 116028.86, 7.5 percent, 8 years, 2006 per month

    # Should return 718,335.96 given 116028.86 principal, 9 percent, 12 years, 1456 per month

