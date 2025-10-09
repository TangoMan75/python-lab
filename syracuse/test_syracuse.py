#!/bin/python3
# -*- coding: utf-8 -*-

"""
 This file is part of the TangoMan Python Lab package.

 (c) "Matthias Morin" <mat@tangoman.io>

 For the full copyright and license information, please view the LICENSE
 file that was distributed with this source code.
"""

from unittest import TestCase

from syracuse import Syracuse


class TestSyracuse(TestCase):
    """TestSyracuse"""

    def setUp(self):
        self.syracuse = Syracuse()
        self.fixture = [
            [1],
            [2, 1],
            [3, 10, 5, 16, 8, 4, 2, 1],
            [4, 2, 1],
            [5, 16, 8, 4, 2, 1],
            [6, 3, 10, 5, 16, 8, 4, 2, 1],
            [7, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1],
            [8, 4, 2, 1],
            [9, 28, 14, 7, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1],
            [10, 5, 16, 8, 4, 2, 1],
            [11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1],
            [12, 6, 3, 10, 5, 16, 8, 4, 2, 1],
            [13, 40, 20, 10, 5, 16, 8, 4, 2, 1],
            [14, 7, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1],
            [15, 46, 23, 70, 35, 106, 53, 160, 80, 40, 20, 10, 5, 16, 8, 4, 2, 1],
            [16, 8, 4, 2, 1],
            [17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1],
            [18, 9, 28, 14, 7, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1],
            [19, 58, 29, 88, 44, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1],
            [20, 10, 5, 16, 8, 4, 2, 1],
            [21, 64, 32, 16, 8, 4, 2, 1],
            [22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1],
            [23, 70, 35, 106, 53, 160, 80, 40, 20, 10, 5, 16, 8, 4, 2, 1],
            [24, 12, 6, 3, 10, 5, 16, 8, 4, 2, 1],
        ]

    def test_invalid_type(self):
        """==> number should raise TypeError when set to invalid type"""
        with self.assertRaises(TypeError):
            self.syracuse.syracuse(1.0)

    def test_negative_number_should_raise_error(self):
        """==> number should raise ValueError when set to negative value"""
        with self.assertRaises(ValueError):
            self.syracuse.syracuse(-1)

    def test_zero_should_raise_error(self):
        """==> number should raise ValueError when set to zero"""
        with self.assertRaises(ValueError):
            self.syracuse.syracuse(0)

    def test_syracuse_sequence(self):
        """==> syracuse method should return expected sequence"""
        for i in range(1, 25):
            self.assertEqual(self.fixture[i - 1], self.syracuse.syracuse(i))
