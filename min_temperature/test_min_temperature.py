#!/bin/python3
# -*- coding: utf-8 -*-

"""
 This file is part of the TangoMan Python Lab package.

 (c) "Matthias Morin" <mat@tangoman.io>

 For the full copyright and license information, please view the LICENSE
 file that was distributed with this source code.
"""

from unittest import TestCase

from min_temperature import MinTemperature


class TestMinTemperature(TestCase):
    """TestMinTemperature"""

    def setUp(self):
        self.min_temperature = MinTemperature()

    def test_get_closest_to_zero_invalid_type(self):
        """==> temperature should raise TypeError when set to invalid type"""
        with self.assertRaises(TypeError):
            self.min_temperature.get_closest_to_zero('invalid_type')

    def test_get_closest_to_zero_no_temperature(self):
        """==> get_closest_to_zero method should raise ValueError when given empty list"""
        with self.assertRaises(ValueError):
            self.min_temperature.get_closest_to_zero([])

    def test_get_closest_to_zero_one_negative_temperature(self):
        """==> get_closest_to_zero method should return expected result"""
        self.assertEqual(-273, self.min_temperature.get_closest_to_zero([-273]))

    def test_get_closest_to_zero_two_negative_temperatures(self):
        """==> get_closest_to_zero method should return expected result"""
        self.assertEqual(-10, self.min_temperature.get_closest_to_zero([-10, -10]))

    def test_get_closest_to_zero_simple(self):
        """==> get_closest_to_zero method should return expected result"""
        self.assertEqual(1, self.min_temperature.get_closest_to_zero([1, -2, -8, 4, 5]))

    def test_get_closest_to_zero_complex(self):
        """==> get_closest_to_zero method should return expected result"""
        self.assertEqual(2, self.min_temperature.get_closest_to_zero([-5, -4, -2, 12, -40, 4, 2, 18, 11, 5]))

    # ==================================================

    def test_get_minimum_positive_temperature_invalid_type(self):
        """==> temperature should raise TypeError when set to invalid type"""
        with self.assertRaises(TypeError):
            self.min_temperature.get_minimum_positive_temperature('invalid_type')

    def test_get_minimum_positive_temperature_no_temperature(self):
        """==> get_minimum_positive_temperature method should raise ValueError when given empty list"""
        with self.assertRaises(ValueError):
            self.min_temperature.get_minimum_positive_temperature([])

    def test_get_minimum_positive_temperature_no_positive_values(self):
        """==> get_minimum_positive_temperature method should raise ValueError when given list without positive values"""
        with self.assertRaises(ValueError):
            self.min_temperature.get_minimum_positive_temperature([-273])

    def test_get_minimum_positive_temperature_simple(self):
        """==> get_minimum_positive_temperature method should return expected result"""
        self.assertEqual(1, self.min_temperature.get_minimum_positive_temperature([1, -2, -8, 4, 5]))

    def test_get_minimum_positive_temperature_complex(self):
        """==> get_minimum_positive_temperature method should return expected result"""
        self.assertEqual(2, self.min_temperature.get_minimum_positive_temperature([-5, -4, -2, 12, -40, 4, 2, 18, 11, 5]))
