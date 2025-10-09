#!/bin/python3
# -*- coding: utf-8 -*-

"""
 This file is part of the TangoMan Python Lab package.

 (c) "Matthias Morin" <mat@tangoman.io>

 For the full copyright and license information, please view the LICENSE
 file that was distributed with this source code.
"""

from unittest import TestCase

from hello_world import HelloWorld


class TestHelloWorld(TestCase):
    """TestHelloWorld"""

    def setUp(self):
        self.hello_world = HelloWorld()

    def test_hello_world(self):
        """==> test hello world"""
        self.assertEqual(self.hello_world.hello_world(), 'Hello World!')
