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

    SECRET = 'a-string-secret-at-least-256-bits-long'

    EXPECTED_DICT = {
        'header': {
            'alg': 'HS256',
            'typ': 'JWT',
        },
        'claims': {
            'sub': '1234567890',
            'name': 'John Doe',
            'admin': True,
            'iat': 1516239022,
        },
        'signature': 'KMUFsIDTnFmyG3nMiGM6H9FNFUROf3wh7SmqJp-QV30',
    }

    EXPECTED_STRING = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiYWRtaW4iOnRydWUsImlhdCI6MTUxNjIzOTAyMn0.KMUFsIDTnFmyG3nMiGM6H9FNFUROf3wh7SmqJp-QV30'

    EXPECTED_URL_SAFE_DICT = {
        'header': {
            'alg': 'HS256',
            'typ': 'JWT',
        },
        'claims': {
            'data': 'ÿî?>a',
        },
        'signature': '1uuDwYEx6-la-RAYd6JZGkuQDCYHv12s7PyBRBcZ4jE',
    }

    EXPECTED_URL_SAFE_STRING = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJkYXRhIjoiw7_Drj8-YSJ9.1uuDwYEx6-la-RAYd6JZGkuQDCYHv12s7PyBRBcZ4jE'

    def setUp(self):
        self.encoder = JwtEncoder(self.SECRET)

    def test_encode_should_return_expected_result(self):
        """==> encode should return expected result"""
        self.assertEqual(self.EXPECTED_STRING, self.encoder.encode(self.EXPECTED_DICT['claims']))

    def test_decode_should_return_expected_result(self):
        """==> decode should return expected result"""
        self.assertEqual(self.EXPECTED_DICT, self.encoder.decode(self.EXPECTED_STRING))

    def test_is_valid_should_return_expected_result(self):
        """==> is valid should return expected result"""
        self.assertTrue(self.encoder.is_valid(self.EXPECTED_STRING))

    def test_encode_produces_url_safe_token(self):
        """==> ensure the encoder always produces url-safe Base64"""
        self.assertEqual(self.EXPECTED_URL_SAFE_STRING, self.encoder.encode(self.EXPECTED_URL_SAFE_DICT['claims']))

    def test_decode_url_safe_token_should_return_expected_result(self):
        """==> decode url-safe token should return expected result"""
        self.assertEqual(self.EXPECTED_URL_SAFE_DICT, self.encoder.decode(self.EXPECTED_URL_SAFE_STRING))
