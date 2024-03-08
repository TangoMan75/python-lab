#!/bin/python3
# -*- coding: utf-8 -*-

"""
 This file is part of the TangoMan Python Lab package.

 (c) "Matthias Morin" <mat@tangoman.io>

 For the full copyright and license information, please view the LICENSE
 file that was distributed with this source code.
"""

from unittest import TestCase
from jwt_encoder import JwtEncoder


class JwtEncoderTest(TestCase):
    """JwtEncoderTest"""

    SECRET = 'secret'

    EXPECTED_DICT = {
        'header': {
            'alg': 'HS256',
            'typ': 'JWT',
        },
        'claims': {'foo': 'bar'},
        'signature': 'a0189ad05a61dfd170416bf44d2ec38ac838a9ad1a15af2aa4c6980eb21766ab',
    }

    EXPECTED_STRING = 'eyJhbGciOiAiSFMyNTYiLCAidHlwIjogIkpXVCJ9.eyJmb28iOiAiYmFyIn0.a0189ad05a61dfd170416bf44d2ec38ac838a9ad1a15af2aa4c6980eb21766ab'

    def setUp(self):
        self.encoder = JwtEncoder(self.SECRET)

    def test_encode_should_return_expected_result(self):
        """==> encode should return expected result"""
        self.assertEqual(self.EXPECTED_STRING, self.encoder.encode({'foo': 'bar'}))

    def test_decode_should_return_expected_result(self):
        """==> decode should return expected result"""
        self.assertEqual(self.EXPECTED_DICT, self.encoder.decode(self.EXPECTED_STRING))

    def test_is_valid_should_return_expected_result(self):
        """==> is valid should return expected result"""
        self.assertTrue(self.encoder.is_valid(self.EXPECTED_STRING))
