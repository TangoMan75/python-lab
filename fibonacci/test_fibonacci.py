#!/bin/python3
# -*- coding: utf-8 -*-

"""
 This file is part of the TangoMan Python Lab package.

 (c) "Matthias Morin" <mat@tangoman.io>

 For the full copyright and license information, please view the LICENSE
 file that was distributed with this source code.
"""

from unittest import TestCase

from fibonacci import Fibonacci


class TestFibonacci(TestCase):
    """TestFibonacci"""

    def setUp(self):
        self.fibonacci = Fibonacci()
        self.fixture = (1, 1, 2, 3, 5, 8, 13, 21, 34, 55)

    def test_invalid_type(self):
        """==> number should raise TypeError when set to invalid type"""
        with self.assertRaises(TypeError):
            self.fibonacci.fib(1.0)

    def test_number_negative_or_zero(self):
        """==> number should raise ValueError when set to negative value or zero"""
        with self.assertRaises(ValueError):
            self.fibonacci.fib(0)
        with self.assertRaises(ValueError):
            self.fibonacci.fib(-1)

    def test_fibonacci_sequence(self):
        """==> fibonacci method should return expected sequence"""
        for i in range(0, 10):
            self.assertEqual(self.fixture[i], self.fibonacci.fib(i + 1))
