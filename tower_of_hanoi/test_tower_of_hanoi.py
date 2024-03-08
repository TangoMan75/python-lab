#!/bin/python3
# -*- coding: utf-8 -*-

"""
 This file is part of the TangoMan Python Lab package.

 (c) "Matthias Morin" <mat@tangoman.io>

 For the full copyright and license information, please view the LICENSE
 file that was distributed with this source code.
"""

from unittest import TestCase

from tower_of_hanoi import TowerOfHanoi


class TestTowerOfHanoi(TestCase):
    """TestTowerOfHanoi"""

    def setUp(self):
        self.tower_of_hanoi = TowerOfHanoi()
        self.fixtures = [
            (1, 'A', 'C', 'B'),
            [
                (1, 'A', 'C')
            ],
            (2, 'A', 'C', 'B'),
            [
                (1, 'A', 'B'),
                (2, 'A', 'C'),
                (1, 'B', 'C')
            ],
            (3, 'A', 'C', 'B'),
            [
                (1, 'A', 'C'),
                (2, 'A', 'B'),
                (1, 'C', 'B'),
                (3, 'A', 'C'),
                (1, 'B', 'A'),
                (2, 'B', 'C'),
                (1, 'A', 'C')
            ],
            (4, 'A', 'C', 'B'),
            [
                (1, 'A', 'B'),
                (2, 'A', 'C'),
                (1, 'B', 'C'),
                (3, 'A', 'B'),
                (1, 'C', 'A'),
                (2, 'C', 'B'),
                (1, 'A', 'B'),
                (4, 'A', 'C'),
                (1, 'B', 'C'),
                (2, 'B', 'A'),
                (1, 'C', 'A'),
                (3, 'B', 'C'),
                (1, 'A', 'B'),
                (2, 'A', 'C'),
                (1, 'B', 'C')
            ]
        ]

    def test_height_invalid_type(self):
        """==> num_disks should raise TypeError when set to invalid type"""
        with self.assertRaises(TypeError):
            self.tower_of_hanoi.tower_of_hanoi(1.0, 'A', 'B', 'C')

    def test_negative_num_disks(self):
        """==> num_disks should raise ValueError when set to negative value"""
        with self.assertRaises(ValueError):
            self.tower_of_hanoi.tower_of_hanoi(-1, 'A', 'B', 'C')

    def test_null_num_disks(self):
        """==> num_disks should raise ValueError when set to zero"""
        with self.assertRaises(ValueError):
            self.tower_of_hanoi.tower_of_hanoi(0, 'A', 'B', 'C')

    def test_poles_invalid_type(self):
        """==> pole should raise TypeError when set to invalid type"""
        with self.assertRaises(TypeError):
            self.tower_of_hanoi.tower_of_hanoi(1, 1, 'B', 'C')
            self.tower_of_hanoi.tower_of_hanoi(1, 'A', 1, 'C')
            self.tower_of_hanoi.tower_of_hanoi(1, 'A', 'B', 1)

    def test_poles_invalid_value(self):
        """==> pole should raise ValueError when set to incorrect value"""
        with self.assertRaises(ValueError):
            self.tower_of_hanoi.tower_of_hanoi(1, 'X', 'B', 'C')
            self.tower_of_hanoi.tower_of_hanoi(1, 'A', 'X', 'C')
            self.tower_of_hanoi.tower_of_hanoi(1, 'A', 'B', 'X')

    def test_tower_of_hanoi_sequence(self):
        """==> tower_of_hanoi method should return expected sequence of moves"""
        for i in range(0, 7, 2):
            self.assertEqual(self.fixtures[i+1], self.tower_of_hanoi.tower_of_hanoi(self.fixtures[i][0], self.fixtures[i][1], self.fixtures[i][2], self.fixtures[i][3]))
