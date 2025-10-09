#!/bin/python3
# -*- coding: utf-8 -*-

"""
 This file is part of the TangoMan Python Lab package.

 (c) "Matthias Morin" <mat@tangoman.io>

 For the full copyright and license information, please view the LICENSE
 file that was distributed with this source code.
"""

from unittest import TestCase

from fizzbuzz import FizzBuzz


class TestFizzBuzz(TestCase):
    """TestFizzBuzz"""

    def setUp(self):
        self.fizzbuzz = FizzBuzz()

    def test_invalid_type(self):
        """==> number should raise TypeError when set to invalid type"""
        with self.assertRaises(TypeError):
            self.fizzbuzz.fizzbuzz('invalid_type')

    def test_number_negative(self):
        """==> number should raise ValueError when set to negative value"""
        with self.assertRaises(ValueError):
            self.fizzbuzz.fizzbuzz(-1)

    def test_number_equals_zero(self):
        """==> number should raise ValueError when set to zero"""
        with self.assertRaises(ValueError):
            self.fizzbuzz.fizzbuzz(0)

    def test_fizz(self):
        """==> fizzbuzz should return 'Fizz' when n set to 3"""
        self.assertEqual(self.fizzbuzz.fizzbuzz(3), 'Fizz')

    def test_buzz(self):
        """==> fizzbuzz should return 'Buzz' when n set to 5"""
        self.assertEqual(self.fizzbuzz.fizzbuzz(5), 'Buzz')

    def test_fizzbuzz(self):
        """==> fizzbuzz should return 'FizzBuzz' when n set to 15"""
        self.assertEqual(self.fizzbuzz.fizzbuzz(15), 'FizzBuzz')

    #--------------------------------------------------

    def test_alt_invalid_type(self):
        """==> number should raise TypeError when set to invalid type"""
        with self.assertRaises(TypeError):
            self.fizzbuzz.fizzbuzz_alt('invalid_type')

    def test_alt_number_negative(self):
        """==> number should raise ValueError when set to negative value"""
        with self.assertRaises(ValueError):
            self.fizzbuzz.fizzbuzz_alt(-1)

    def test_alt_number_equals_zero(self):
        """==> number should raise ValueError when set to zero"""
        with self.assertRaises(ValueError):
            self.fizzbuzz.fizzbuzz_alt(0)

    def test_alt_fizz(self):
        """==> fizzbuzz should return 'Fizz' when n set to 3"""
        self.assertEqual(self.fizzbuzz.fizzbuzz_alt(3), 'Fizz')

    def test_alt_buzz(self):
        """==> fizzbuzz should return 'Buzz' when n set to 5"""
        self.assertEqual(self.fizzbuzz.fizzbuzz_alt(5), 'Buzz')

    def test_alt_fizzbuzz(self):
        """==> fizzbuzz should return 'FizzBuzz' when n set to 15"""
        self.assertEqual(self.fizzbuzz.fizzbuzz_alt(15), 'FizzBuzz')
