#!/bin/python3
# -*- coding: utf-8 -*-

"""
 This file is part of the TangoMan Python Lab package.

 (c) "Matthias Morin" <mat@tangoman.io>

 For the full copyright and license information, please view the LICENSE
 file that was distributed with this source code.
"""

from unittest import TestCase

from hyper_log_log import HyperLogLog


class TestHyperLogLog(TestCase):
    """TestHyperLogLog"""

    def setUp(self):
        self.hyper_log_log = HyperLogLog(precision=14)

    def test_add_element(self):
        """==> add element should append elements to processing list"""
        elements = ['apple', 'banana', 'orange', 'apple', 'grape', 'banana', 'kiwi']
        for element in elements:
            self.hyper_log_log.add_element(element)

        # Check that the registers have been updated
        self.assertNotEqual(self.hyper_log_log.registers, [0] * self.hyper_log_log.register_size)

    def test_estimate_cardinality(self):
        """==> estimate cardinality should return a positive integer"""
        elements = ['apple', 'banana', 'orange', 'apple', 'grape', 'banana', 'kiwi']
        for element in elements:
            self.hyper_log_log.add_element(element)

        estimated_cardinality = self.hyper_log_log.estimate_cardinality()
        self.assertIsInstance(estimated_cardinality, int)
        self.assertGreaterEqual(estimated_cardinality, 0)

    def test_empty_hyperloglog(self):
        """==> test empty hyperloglog should have an estimated cardinality of 0"""
        empty_hll = HyperLogLog(precision=14)
        estimated_cardinality = empty_hll.estimate_cardinality()
        self.assertEqual(estimated_cardinality, 0)
