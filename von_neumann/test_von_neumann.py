#!/bin/python3
# -*- coding: utf-8 -*-

"""
 This file is part of the TangoMan Python Lab package.

 (c) "Matthias Morin" <mat@tangoman.io>

 For the full copyright and license information, please view the LICENSE
 file that was distributed with this source code.
"""

from unittest import TestCase

from von_neumann import VonNeumann


class TestVonNeumann(TestCase):
    """TestVonNeumann"""

    def setUp(self):
        self.von_neumann = VonNeumann()
        self.fixture = (1234, 5227, 3215, 3362, 3030, 1809, 2724, 4201, 6484, 422, 7808)

    def test_invalid_type(self):
        """==> number should raise TypeError when set to invalid type"""
        with self.assertRaises(TypeError):
            self.von_neumann.pseudo_random(1.0)

    def test_negative_number_should_raise_error(self):
        """==> number should raise ValueError when set to negative value"""
        with self.assertRaises(ValueError):
            self.von_neumann.pseudo_random(-1)

    def test_pseudo_random(self):
        """==> pseudo_random method should return expected type"""
        self.assertIsInstance(self.von_neumann.pseudo_random(696664536), int)

    def test_pseudo_random_alt(self):
        """==> pseudo_random method should return expected resut"""
        for i in range(0, 10):
            self.assertEqual(self.fixture[i + 1], self.von_neumann.pseudo_random(self.fixture[i]))
