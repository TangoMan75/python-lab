#!/bin/python3
# -*- coding: utf-8 -*-

"""
 This file is part of the TangoMan Python Lab package.

 (c) "Matthias Morin" <mat@tangoman.io>

 For the full copyright and license information, please view the LICENSE
 file that was distributed with this source code.
"""

from unittest import TestCase

from taxes import FrenchIncomeTaxCalculator


class TestFrenchIncomeTaxCalculator(TestCase):
    """
    A test class for the FrenchIncomeTaxCalculator class.
    """

    def test_zero_income(self):
        """
        Test calculation of tax for zero income.
        """
        calculator = FrenchIncomeTaxCalculator(0)
        self.assertEqual(calculator.calculate_tax(), 0)

    def test_bracket_1(self):
        """
        Test calculation of tax for an income falling into bracket 1.
        """
        calculator = FrenchIncomeTaxCalculator(10000)
        self.assertEqual(calculator.calculate_tax(), 0)

    def test_bracket_2(self):
        """
        Test calculation of tax for an income falling into bracket 2.
        """
        calculator = FrenchIncomeTaxCalculator(20000)
        self.assertEqual(calculator.calculate_tax(), 957.66)

    def test_bracket_3(self):
        """
        Test calculation of tax for an income falling into bracket 3.
        """
        calculator = FrenchIncomeTaxCalculator(50000)
        self.assertEqual(calculator.calculate_tax(), 8286.23)

    def test_bracket_4(self):
        """
        Test calculation of tax for an income falling into bracket 4.
        """
        calculator = FrenchIncomeTaxCalculator(100000)
        self.assertEqual(calculator.calculate_tax(), 25228.72)

    def test_bracket_5(self):
        """
        Test calculation of tax for an income falling into bracket 5.
        """
        calculator = FrenchIncomeTaxCalculator(200000)
        self.assertEqual(calculator.calculate_tax(), 67144.48)

    def test_large_income(self):
        """
        Test calculation of tax for a large income.
        """
        calculator = FrenchIncomeTaxCalculator(500000)
        self.assertEqual(calculator.calculate_tax(), 202144.48)

    def test_example_from_website(self):
        """
        Test calculation of the example from government website (bracket 3)
        """
        calculator = FrenchIncomeTaxCalculator(32000)
        self.assertEqual(calculator.calculate_tax(), 2886.23)

    def test_bracket_1_with_familly_quotient_equals_2(self):
        """
        Test calculation of tax for an income falling into bracket 1 with familly quotient = 2.
        """
        calculator = FrenchIncomeTaxCalculator(22588, 2)
        self.assertEqual(calculator.calculate_tax(), 0)

    def test_bracket_2_with_familly_quotient_equals_2(self):
        """
        Test calculation of tax for an income falling into bracket 2 with familly quotient = 2.
        """
        calculator = FrenchIncomeTaxCalculator(57594, 2)
        self.assertEqual(calculator.calculate_tax(), 1925.33)

    def test_bracket_3_with_familly_quotient_equals_2(self):
        """
        Test calculation of tax for an income falling into bracket 3 with familly quotient = 2.
        """
        calculator = FrenchIncomeTaxCalculator(164682, 2)
        self.assertEqual(calculator.calculate_tax(), 17988.53)
