#!/bin/python3
# -*- coding: utf-8 -*-

"""
 This file is part of the TangoMan Python Lab package.

 (c) "Matthias Morin" <mat@tangoman.io>

 For the full copyright and license information, please view the LICENSE
 file that was distributed with this source code.
"""

from unittest import TestCase

from perfect import Perfect


class TestPerfect(TestCase):
    """TestPerfect"""

    def setUp(self):
        self.perfect = Perfect()
        self.fixture = [
            (1, False),
            (2, False),
            (3, False),
            (4, False),
            (5, False),
            (6, True),
            (7, False),
            (8, False),
            (9, False),
            (10, False),
            (11, False),
            (12, False),
            (13, False),
            (14, False),
            (15, False),
            (16, False),
            (17, False),
            (18, False),
            (19, False),
            (20, False),
            (21, False),
            (22, False),
            (23, False),
            (24, False),
            (25, False),
            (26, False),
            (27, False),
            (28, True),
            (29, False),
        ]

    def test_invalid_type(self):
        """==> number should raise TypeError when set to invalid type"""
        with self.assertRaises(TypeError):
            self.perfect.is_perfect(1.0)

    def test_negative_number_should_raise_error(self):
        """==> number should raise ValueError when set to negative value"""
        with self.assertRaises(ValueError):
            self.perfect.is_perfect(-1)

    def test_is_perfect_sequence(self):
        """==> is_perfect method should return expected sequence"""
        for i in self.fixture:
            self.assertEqual(i[1], self.perfect.is_perfect(i[0]))
