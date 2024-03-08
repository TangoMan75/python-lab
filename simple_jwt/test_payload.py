#!/bin/python3
# -*- coding: utf-8 -*-

"""
 This file is part of the TangoMan Python Lab package.

 (c) "Matthias Morin" <mat@tangoman.io>

 For the full copyright and license information, please view the LICENSE
 file that was distributed with this source code.
"""

from unittest import TestCase

from payload import Payload

class PayloadTest(TestCase):
    """
    PayloadTest
    """

    FIXTURE_1 = {
        'id': 1,
        'login': 'TangoMan75',
        'firstname': 'Matthias',
        'lastname': 'Morin',
        'email': 'mat@tangoman.io',
    }

    EXPECTED_1 = {
        'jti': '24a440a1ca9b90d72200192b',
        'iat': 1000000000,
        'id': 1,
        'login': 'TangoMan75',
        'firstname': 'Matthias',
        'lastname': 'Morin',
        'email': 'mat@tangoman.io',
    }

    EXPECTED_LIST_1 = [
        ('jti', '24a440a1ca9b90d72200192b'),
        ('iat', 1000000000),
        ('id', 1),
        ('login', 'TangoMan75'),
        ('firstname', 'Matthias'),
        ('lastname', 'Morin'),
        ('email', 'mat@tangoman.io')
    ]

    EXPECTED_STRING_1 = '{"jti": "24a440a1ca9b90d72200192b", "iat": 1000000000, "id": 1, "login": "TangoMan75", "firstname": "Matthias", "lastname": "Morin", "email": "mat@tangoman.io"}'

    FIXTURE_2 = {
        'payload': [
            {
                'id': 1,
                'name': 'tangoman',
                'email': 'mat@tangoman.io',
            },
            {
                'id': 2,
                'name': 'foobar',
                'email': 'foobar@example.com',
            }
        ]
    }

    EXPECTED_2 = {
        'jti': '24a440a1ca9b90d72200192b',
        'iat': 1000000000,
        'payload': [
            {
                'id': 1,
                'name': 'tangoman',
                'email': 'mat@tangoman.io',
            },
            {
                'id': 2,
                'name': 'foobar',
                'email': 'foobar@example.com',
            }
        ]
    }

    EXPECTED_LIST_2 = [
        ('jti', '24a440a1ca9b90d72200192b'),
        ('iat', 1000000000),
        ('payload', [
            {'id': 1, 'name': 'tangoman', 'email': 'mat@tangoman.io'},
            {'id': 2, 'name': 'foobar', 'email': 'foobar@example.com'}
        ])
    ]

    def test_constructor_typeerror(self):
        """==> Payload.__init__ should raise TypeError"""
        with self.assertRaises(TypeError):
            Payload('invalid_type')

    def test_properties(self):
        """==> Payload.__properties__ should return expected list"""
        payload = Payload(self.FIXTURE_1)
        self.assertEqual(payload.__properties__, list(self.EXPECTED_1.keys()))

        payload = Payload(self.FIXTURE_2)
        self.assertEqual(payload.__properties__, list(self.EXPECTED_2.keys()))

    def test_dict(self):
        """==> dict(Payload) should return expected dictionary"""
        payload = Payload(self.EXPECTED_1)
        self.assertEqual(dict(payload), self.EXPECTED_1)

        payload = Payload(self.EXPECTED_2)
        self.assertEqual(dict(payload), self.EXPECTED_2)

    def test_eq(self):
        """==> Payload == Payload should return expected boolean"""
        payload = Payload(self.EXPECTED_1)
        # self.assertEqual(payload, Payload(self.EXPECTED_1))
        self.assertTrue(payload == Payload(self.EXPECTED_1))
        self.assertFalse(payload == Payload({'foo': 'pong'}))

    def test_hash(self):
        """==> hash(Payload) should return expected hash"""
        payload = Payload(self.EXPECTED_1)
        self.assertIsInstance(hash(payload), int)
        self.assertEqual(hash(payload), hash(Payload(self.EXPECTED_1)))
        self.assertFalse(hash(payload) == hash(Payload({'foo': 'bar'})))

    def test_iter(self):
        """==> Payload.__iter__ should return expected values"""
        payload = Payload(self.EXPECTED_1)
        for item in payload:
            # self.assertTrue(item.name in ['tangoman', 'foobar'])
            self.assertEqual(item[1], self.EXPECTED_1[item[0]])

        payload = Payload(self.EXPECTED_2)
        for item in payload:
            # self.assertTrue(item.name in ['tangoman', 'foobar'])
            self.assertEqual(item[1], self.EXPECTED_2[item[0]])

    def test_list(self):
        """==> list(Payload) should return expected list"""
        payload = Payload(self.EXPECTED_1)
        self.assertEqual(list(payload), self.EXPECTED_LIST_1)

        payload = Payload(self.EXPECTED_2)
        self.assertEqual(list(payload), self.EXPECTED_LIST_2)

    def test_len(self):
        """==> len(object_) should return item count"""
        payload = Payload(self.FIXTURE_1)
        self.assertEqual(len(payload), 7)

        payload = Payload(self.FIXTURE_2)
        self.assertEqual(len(payload), 3)

    def test_str(self):
        """==> str(object_) should return expected value"""
        payload = Payload(self.EXPECTED_1)
        self.assertIsInstance(str(payload), str)
        self.assertEqual(str(payload), self.EXPECTED_STRING_1)
