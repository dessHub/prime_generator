import unittest
from primes import is_prime

class PrimesTestCase(unittest.TestCase):
    """Tests for `primes.py`."""

    def test_is_number(self):
        """Is arg a number?"""
        self.assertFalse(is_prime(8))

    def test_is_7_prime(self):
        """Is seven successfully determined to be prime?"""
        self.assertTrue(is_prime(7))

    def test_is_six_non_prime(self):
        """Is six correctly determined not to be prime?"""
        self.assertFalse(is_prime(6), msg='Six is not prime!')

    def test_is_zero_not_prime(self):
        """Is zero correctly determined not to be prime?"""
        self.assertFalse(is_prime(0))

    def test_negative_number(self):
        """Is a negative number correctly determined not to be prime?"""
        for index in range(-1, -10, -1):
            self.assertFalse(is_prime(index), msg='{} should not be determined to be prime'.format(index))

    def test_arg_less_than_two(self):
        """Is args less than two correctly checked"""
        self.assertRaises(ValueError)

    def test_is_not_a_string(self):
        """Arg is not a string"""
        self.assertRaises(TypeError)


if __name__ == '__main__':
    unittest.main()
