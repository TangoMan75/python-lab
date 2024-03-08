#!/bin/python3
# -*- coding: utf-8 -*-

"""
 This file is part of the TangoMan Python Lab package.

 (c) "Matthias Morin" <mat@tangoman.io>

 For the full copyright and license information, please view the LICENSE
 file that was distributed with this source code.
"""

from unittest import TestCase

from prime_numbers import PrimeNumbers


class TestPrimeNumbers(TestCase):
    """TestPrimeNumbers"""

    def setUp(self):
        self.prime_numbers = PrimeNumbers()
        self.fixture = [
            (1, False),
            (2, True),
            (3, True),
            (4, False),
            (5, True),
            (6, False),
            (7, True),
            (8, False),
            (9, False),
            (10, False),
            (11, True),
            (12, False),
            (13, True),
            (14, False),
            (15, False),
            (16, False),
            (17, True),
            (18, False),
            (19, True),
            (20, False),
            (21, False),
            (22, False),
            (23, True),
            (24, False),
            (25, False),
            (26, False),
            (27, False),
            (28, False),
            (29, True),
        ]

    def test_invalid_type(self):
        """==> number should raise TypeError when set to invalid type"""
        with self.assertRaises(TypeError):
            self.prime_numbers.is_prime(1.0)

    def test_number_negative_or_zero(self):
        """==> n should raise ValueError when set to negative value or zero"""
        with self.assertRaises(ValueError):
            self.prime_numbers.is_prime(0)
        with self.assertRaises(ValueError):
            self.prime_numbers.is_prime(-1)

    def test_negative_number_should_raise_error(self):
        """==> number should raise ValueError when set to negative value"""
        with self.assertRaises(ValueError):
            self.prime_numbers.is_prime(-1)

    def test_is_prime_sequence(self):
        """==> is_prime method should return expected sequence"""
        for i in self.fixture:
            self.assertEqual(i[1], self.prime_numbers.is_prime(i[0]))
