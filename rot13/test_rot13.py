#!/bin/python3
# -*- coding: utf-8 -*-

"""
 This file is part of the TangoMan Python Lab package.

 (c) "Matthias Morin" <mat@tangoman.io>

 For the full copyright and license information, please view the LICENSE
 file that was distributed with this source code.
"""

from unittest import TestCase

from rot13 import Rot13


class TestRot13(TestCase):
    """TestRot13"""

    def setUp(self):
        self.rot13 = Rot13()

    def test_invalid_type(self):
        """==> text should raise TypeError when set to invalid type"""
        with self.assertRaises(TypeError):
            self.rot13.rot13(1.0)
        with self.assertRaises(TypeError):
            self.rot13.rot13(0)

    def test_rot13_encryption(self):
        """==> rot13 encryption should return expected result"""
        self.assertEqual(self.rot13.rot13('Hello, World!'), 'Uryyb, Jbeyq!')

    def test_rot13_decryption(self):
        """==> rot13 decryption should return expected result"""
        self.assertEqual(self.rot13.rot13('Uryyb, Jbeyq!'), 'Hello, World!')

    def test_rot13_edge_cases(self):
        """==> edge cases should return expected results"""
        self.assertEqual(self.rot13.rot13(''), '')
        self.assertEqual(self.rot13.rot13('123'), '123')
        self.assertEqual(self.rot13.rot13('+-*/'), '+-*/')
