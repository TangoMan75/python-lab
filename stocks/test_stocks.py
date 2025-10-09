#!/bin/python3
# -*- coding: utf-8 -*-

"""
 This file is part of the TangoMan Python Lab package.

 (c) "Matthias Morin" <mat@tangoman.io>

 For the full copyright and license information, please view the LICENSE
 file that was distributed with this source code.
"""

from unittest import TestCase

from stocks import Stocks


class TestStocks(TestCase):
    """TestStocks"""

    def setUp(self):
        self.stocks = Stocks()
        self.expected = ['NFLX', 'META', 'GOOGL']
        self.stocks_list = ['AMZN', 'GOOGL', 'META', 'NFLX']
        self.prices_list = [
            [10, 11, 12, 13, 14],
            [20, 21, 22, 23, 24],
            [30, 31, 32, 33, 34],
            [40, 41, 42, 43, 44],
        ]

    def test_stocks_invalid_type(self):
        """==> stocks should raise TypeError when set to invalid type"""
        with self.assertRaises(TypeError):
            self.stocks.get_top_three(1.0, [])

    def test_prices_invalid_type(self):
        """==> prices should raise TypeError when set to invalid type"""
        with self.assertRaises(TypeError):
            self.stocks.get_top_three([], 1.0)

    def test_different_list_length_size_should_raise_error(self):
        """==> get_top_three method should raise ValueError when lists have different size"""
        with self.assertRaises(ValueError):
            self.stocks.get_top_three(['foo', 'bar'], [[1]])

    def test_undersized_lists_should_raise_error(self):
        """==> get_top_three method should raise ValueError when lists are too short"""
        with self.assertRaises(ValueError):
            self.stocks.get_top_three(['foo', 'bar'], [[1], [2]])

    def test_get_top_three(self):
        """==> get_top_three method should return expected resut"""
        self.assertEqual(self.expected, self.stocks.get_top_three(self.stocks_list, self.prices_list))
