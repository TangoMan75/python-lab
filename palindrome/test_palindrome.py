#!/bin/python3
# -*- coding: utf-8 -*-

"""
 This file is part of the TangoMan Python Lab package.

 (c) "Matthias Morin" <mat@tangoman.io>

 For the full copyright and license information, please view the LICENSE
 file that was distributed with this source code.
"""

from unittest import TestCase

from palindrome import Palindrome


class TestPalindrome(TestCase):
    """TestPalindrome"""

    def setUp(self):
        self.palindrome = Palindrome()

    def test_invalid_type(self):
        """==> string should raise TypeError when set to invalid type"""
        with self.assertRaises(TypeError):
            self.palindrome.is_palindrome(123)

    def test_true(self):
        """==> is_palindrome should return 'True' when string set to 'racecar'"""
        self.assertEqual(self.palindrome.is_palindrome('racecar'), True)

    def test_false(self):
        """==> is_palindrome should return 'False' when string set to 'cat'"""
        self.assertEqual(self.palindrome.is_palindrome('cat'), False)

    def test_recursive_invalid_type(self):
        """==> string should raise TypeError when set to invalid type"""
        with self.assertRaises(TypeError):
            self.palindrome.is_palindrome_recursive(123)

    def test_recursive_true(self):
        """==> is_palindrome_recursive should return 'True' when string set to 'racecar'"""
        self.assertEqual(self.palindrome.is_palindrome_recursive('racecar'), True)

    def test_recursive_false(self):
        """==> is_palindrome_recursive should return 'False' when string set to 'cat'"""
        self.assertEqual(self.palindrome.is_palindrome_recursive('cat'), False)
