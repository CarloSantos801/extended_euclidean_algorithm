"""Tests for the extended Euclidean algorithm implementation."""

import unittest

from extended_euclidean_algorithm import extended_gcd


class TestExtendedGCD(unittest.TestCase):
    def test_basic_coprime(self):
        gcd, x, y = extended_gcd(240, 46)
        self.assertEqual(gcd, 2)
        self.assertEqual(240 * x + 46 * y, 2)

    def test_identity_holds_for_small_positive_numbers(self):
        for a, b in [(3, 5), (5, 3), (12, 18), (18, 12), (7, 13)]:
            with self.subTest(a=a, b=b):
                gcd, x, y = extended_gcd(a, b)
                self.assertEqual(a * x + b * y, gcd)
                self.assertGreaterEqual(gcd, 0)

    def test_identity_holds_for_negative_numbers(self):
        for a, b in [(-3, 5), (3, -5), (-3, -5), (-12, 18), (12, -18)]:
            with self.subTest(a=a, b=b):
                gcd, x, y = extended_gcd(a, b)
                self.assertEqual(a * x + b * y, gcd)
                self.assertGreaterEqual(gcd, 0)

    def test_zero_first_argument(self):
        gcd, x, y = extended_gcd(0, 5)
        self.assertEqual(gcd, 5)
        self.assertEqual(0 * x + 5 * y, 5)

    def test_zero_second_argument(self):
        gcd, x, y = extended_gcd(5, 0)
        self.assertEqual(gcd, 5)
        self.assertEqual(5 * x + 0 * y, 5)

    def test_both_zero(self):
        gcd, x, y = extended_gcd(0, 0)
        self.assertEqual(gcd, 0)
        self.assertEqual(0 * x + 0 * y, 0)

    def test_large_numbers(self):
        a, b = 123456789, 987654321
        gcd, x, y = extended_gcd(a, b)
        self.assertEqual(gcd, 9)
        self.assertEqual(a * x + b * y, 9)

    def test_one_input_one(self):
        gcd, x, y = extended_gcd(1, 1)
        self.assertEqual(gcd, 1)
        self.assertEqual(1 * x + 1 * y, 1)

    def test_gcd_is_non_negative_for_negative_inputs(self):
        gcd, _, _ = extended_gcd(-12, -18)
        self.assertGreaterEqual(gcd, 0)

    def test_modular_inverse_example(self):
        # For a and m coprime, the Bézout coefficient of a gives the
        # modular inverse modulo m.
        a, m = 7, 26
        gcd, x, _ = extended_gcd(a, m)
        self.assertEqual(gcd, 1)
        self.assertEqual((a * x) % m, 1 % m)

    def test_modular_inverse_when_coefficient_negative(self):
        # The coefficient may be negative; the modular inverse should
        # be taken modulo m to be positive.
        a, m = 3, 11
        gcd, x, _ = extended_gcd(a, m)
        self.assertEqual(gcd, 1)
        inverse = x % m
        self.assertEqual((a * inverse) % m, 1)

    def test_diophantine_solution_existence(self):
        # For 12x + 18y = 6, a solution exists and satisfies the
        # equation.
        gcd, x, y = extended_gcd(12, 18)
        self.assertEqual(gcd, 6)
        self.assertEqual(12 * x + 18 * y, 6)


if __name__ == "__main__":
    unittest.main()
