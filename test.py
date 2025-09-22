# Author: Muhammad Adiputra
# Date: 22/9/2025
# Description: Unit tests for the fund_allocation module. Tests include happy case, not enough deposits, too much deposits, Empty deposits, and zero plans.

import unittest
from fund_allocation import calc_final_alloc  # import the main function

class TestFundAllocation(unittest.TestCase):

    def setUp(self):
        # Common deposit plans for all tests
        self.onetime = {"High Risk": 10000, "Retirement": 500}
        self.monthly = {"High Risk": 0, "Retirement": 100}

    # happy case: deposits exactly match total required
    def test_happy_case(self):
        deposits = [10500, 100]  # Total = 10600
        expected = {"High Risk": 10000, "Retirement": 600}
        result = calc_final_alloc(self.onetime, self.monthly, deposits)
        self.assertEqual(result, expected)

    # edge case: not enough deposits
    def test_not_enough_deposit_highrisk_only(self):
        deposits = [5000]  # Total < High Risk requirement
        expected = {"High Risk": 5000, "Retirement": 0}
        result = calc_final_alloc(self.onetime, self.monthly, deposits)
        self.assertEqual(result, expected)

    def test_not_enough_deposit_partial_retirement(self):
        deposits = [10500]  # Total < total required
        expected = {"High Risk": 10000, "Retirement": 500}
        result = calc_final_alloc(self.onetime, self.monthly, deposits)
        self.assertEqual(result, expected)

    # edge case: too much deposit
    def test_too_much_deposit(self):
        deposits = [12000]  # Total > total required
        expected = {"High Risk": 10000, "Retirement": 600}  # Cap at required
        result = calc_final_alloc(self.onetime, self.monthly, deposits)
        self.assertEqual(result, expected)

    # edge case: empty deposits
    def test_empty_deposits(self):
        deposits = []  # No deposit
        expected = {"High Risk": 0, "Retirement": 0}
        result = calc_final_alloc(self.onetime, self.monthly, deposits)
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
