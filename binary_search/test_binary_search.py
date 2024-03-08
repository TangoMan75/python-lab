#!/bin/python3
# -*- coding: utf-8 -*-

"""
 This file is part of the TangoMan Python Lab package.

 (c) "Matthias Morin" <mat@tangoman.io>

 For the full copyright and license information, please view the LICENSE
 file that was distributed with this source code.
"""

from unittest import TestCase
from binary_search import BinarySearch


class TestBinarySearch(TestCase):
    """TestBinarySearch"""
    def setUp(self):
        self.binary_search = BinarySearch()

    def test_should_raise_typeerror_when_array_is_set_to_invalid_type(self):
        """==> should raise TypeError when array is set to invalid type"""
        with self.assertRaises(TypeError):
            self.binary_search.binary_search('invalid_type', 'thing_to_find')

    def test_should_raise_valueerror_when_thing_to_find_is_empty(self):
        """==> should raise ValueError when thing_to_find is empty"""
        array = [1, 2, 3, 4, 5]
        with self.assertRaises(ValueError):
            self.binary_search.binary_search(array, None)

    def test_should_raise_typeerror_when_start_is_set_to_invalid_type(self):
        """==> should raise TypeError when start is set to invalid type"""
        array = [1, 2, 3, 4, 5]
        with self.assertRaises(TypeError):
            self.binary_search.binary_search(array, 'thing_to_find', 'invalid_type')

    def test_should_raise_valueerror_when_start_is_lower_than_zero(self):
        """==> should raise ValueError when start is lower than zero"""
        array = [1, 2, 3, 4, 5]
        with self.assertRaises(ValueError):
            self.binary_search.binary_search(array, 'thing_to_find', -1)

    def test_should_raise_typeerror_when_end_is_set_to_invalid_type(self):
        """==> should raise TypeError when end is set to invalid type"""
        array = [1, 2, 3, 4, 5]
        with self.assertRaises(TypeError):
            self.binary_search.binary_search(array, 'thing_to_find', 0, 'invalid_type')

    def test_should_return_true_if_value_is_found(self):
        """==> should return true if value is found"""
        array = [1, 2, 3, 4, 5]
        self.assertTrue(self.binary_search.binary_search(array, 3))

    def test_should_return_false_if_value_is_not_found(self):
        """==> should return false if value is not found"""
        array = [1, 2, 3, 4, 5]
        self.assertFalse(self.binary_search.binary_search(array, 0))

    def test_should_work_on_empty_array(self):
        """==> should work on empty array"""
        array = []
        self.assertFalse(self.binary_search.binary_search(array, 'thing_to_find'))

    def test_should_return_true_with_start_and_end_indices(self):
        """==> should return true with start and end indices"""
        array = [1, 2, 3, 4, 5]
        self.assertTrue(self.binary_search.binary_search(array, 4, 2, 4))
