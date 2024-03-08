#!/bin/python3
# -*- coding: utf-8 -*-

"""
 This file is part of the TangoMan Python Lab package.

 (c) "Matthias Morin" <mat@tangoman.io>

 For the full copyright and license information, please view the LICENSE
 file that was distributed with this source code.
"""

from unittest import TestCase

from factorial import Factorial


class TestFactorial(TestCase):
    """TestFactorial"""

    def setUp(self):
        self.factorial = Factorial()
        self.fixture = (1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 3628800)

    def test_invalid_type(self):
        """==> number should raise TypeError when set to invalid type"""
        with self.assertRaises(TypeError):
            self.factorial.factorial('invalid_type')

    def test_negative_number_should_raise_error(self):
        """==> number should raise ValueError when set to negative value"""
        with self.assertRaises(ValueError):
            self.factorial.factorial(-1)

    def test_factorial_sequence(self):
        """==> factorial method should return expected sequence"""
        for i in range(0, 10):
            self.assertEqual(self.fixture[i], self.factorial.factorial(i + 1))

    def test_iterative_invalid_type(self):
        """==> number should raise TypeError when set to invalid type"""
        with self.assertRaises(TypeError):
            self.factorial.factorial_iterative('invalid_type')

    def test_iterative_negative_number_should_raise_error(self):
        """==> number should raise ValueError when set to negative value"""
        with self.assertRaises(ValueError):
            self.factorial.factorial_iterative(-1)

    def test_iterative_factorial_sequence(self):
        """==> factorial method should return expected sequence"""
        for i in range(0, 10):
            self.assertEqual(self.fixture[i], self.factorial.factorial_iterative(i + 1))
