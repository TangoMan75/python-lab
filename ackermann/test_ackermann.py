#!/bin/python3
# -*- coding: utf-8 -*-

"""
 This file is part of the TangoMan Python Lab package.

 (c) "Matthias Morin" <mat@tangoman.io>

 For the full copyright and license information, please view the LICENSE
 file that was distributed with this source code.
"""

from unittest import TestCase

from ackermann import Ackermann


class TestAckermann(TestCase):
    """TestAckermann"""

    def setUp(self):
        self.ackermann = Ackermann()
        self.fixture = (
            (1, 2, 3, 4, 5, 6),
            (2, 3, 4, 5, 6, 7),
            (3, 5, 7, 9, 11, 13),
            (5, 13, 29, 61, 125, 253)
        )

    def test_m_should_raise_typeerror_when_set_to_invalid_type(self):
        """==> m should raise TypeError when set to invalid type"""
        with self.assertRaises(TypeError):
            self.ackermann.ackermann('invalid_type', 0)

    def test_n_should_raise_typeerror_when_set_to_invalid_type(self):
        """==> n should raise TypeError when set to invalid type"""
        with self.assertRaises(TypeError):
            self.ackermann.ackermann(0, 'invalid_type')

    def test_m_should_raise_valueerror_when_set_to_negative_value(self):
        """==> m should raise ValueError when set to negative value"""
        with self.assertRaises(ValueError):
            self.ackermann.ackermann(-1, 3)

    def test_n_should_raise_valueerror_when_set_to_negative_value(self):
        """==> n should raise ValueError when set to negative value"""
        with self.assertRaises(ValueError):
            self.ackermann.ackermann(3, -1)

    def test_should_return_the_expected_sequence_for_ackermann(self):
        """==> should return the expected sequence for Ackermann"""
        for i in range(0, 4):
            for j in range(0, 6):
                self.assertEqual(self.ackermann.ackermann(i, j), self.fixture[i][j])

    def test_should_raise_the_expected_recursionerror(self):
        """==> should raise the expected RecursionError"""
        with self.assertRaises(RecursionError):
            for i in range(0, 5):
                for j in range(0, 6):
                    self.ackermann.ackermann(i, j)
