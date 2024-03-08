#!/bin/python3
# -*- coding: utf-8 -*-

"""
 This file is part of the TangoMan Python Lab package.

 (c) "Matthias Morin" <mat@tangoman.io>

 For the full copyright and license information, please view the LICENSE
 file that was distributed with this source code.
"""

import base64
import hashlib
import hmac
import json
from payload import Payload


class JwtEncoder:
    """JwtEncoder"""

    VALID_ALGOS = {
        'HS256': 'sha256',
        'HS384': 'sha384',
        'HS512': 'sha512',
    }

    DEFAULT_HEADER = {
        'alg': 'HS256',
        'typ': 'JWT',
    }

    def __init__(self, secret: str):
        self.secret = secret

    def encode(self, payload: dict, header=None) -> str:
        """encode"""
        if not isinstance(payload, dict):
            raise TypeError(f'{self.encode.__qualname__}: expects parameter "payload" to be of type dict: {type(payload)} given')

        header = header or self.DEFAULT_HEADER.copy()

        encoded_header = base64.urlsafe_b64encode(json.dumps(header).encode()).rstrip(b'=').decode()
        encoded_payload = base64.urlsafe_b64encode(json.dumps(payload).encode()).rstrip(b'=').decode()
        signature = self.sign(header['alg'], encoded_header, encoded_payload)

        return f'{encoded_header}.{encoded_payload}.{signature}'

    def decode(self, token: str) -> dict:
        """decode"""
        if not isinstance(token, str):
            raise TypeError(f'{self.decode.__qualname__}: expects parameter "token" to be of type str: {type(token)} given')

        encoded_header, encoded_payload, signature = token.split('.', 2)

        return {
            'header': json.loads(base64.urlsafe_b64decode(encoded_header + '==').decode()),
            'claims': json.loads(base64.urlsafe_b64decode(encoded_payload + '==').decode()),
            'signature': signature,
        }

    def is_valid(self, token: str) -> bool:
        """is_valid"""
        if not isinstance(token, str):
            raise TypeError(f'{self.decode.__qualname__}: expects parameter "token" to be of type str: {type(token)} given')

        decoded = self.decode(token)
        encoded_header, encoded_payload, _ = token.split('.', 2)
        signature = self.sign(decoded['header']['alg'] if 'header' in decoded else '', encoded_header, encoded_payload)

        return hmac.compare_digest(decoded['signature'], signature)

    def sign(self, hash_algorithm: str, encoded_header: str, encoded_payload: str):
        """sign"""
        if not isinstance(hash_algorithm, str):
            raise TypeError(f'{self.decode.__qualname__}: expects parameter "hash_algorithm" to be of type str: {type(hash_algorithm)} given')

        if not isinstance(encoded_header, str):
            raise TypeError(f'{self.decode.__qualname__}: expects parameter "encoded_header" to be of type str: {type(encoded_header)} given')

        if not isinstance(encoded_payload, str):
            raise TypeError(f'{self.decode.__qualname__}: expects parameter "encoded_payload" to be of type str: {type(encoded_payload)} given')

        if hash_algorithm not in self.VALID_ALGOS:
            raise ValueError(f'{self.decode.__qualname__}: argument "hash_algorithm" is invalid: {str(hash_algorithm)} given')

        message = f'{encoded_header}.{encoded_payload}'.encode('utf-8')
        secret_key = self.secret.encode('utf-8')
        return hmac.new(secret_key, message, getattr(hashlib, self.VALID_ALGOS[hash_algorithm])).hexdigest()


def main():
    """main"""
    print('JwtEncoder')
    print('=' * 50 + '\n')

    jwt_encoder = JwtEncoder('secret')

    payload = {'foo': 'bar'}
    token = jwt_encoder.encode(payload)
    print(token)
    print('')

    decoded_token = jwt_encoder.decode(token)
    print(decoded_token)
    print('')

    print(jwt_encoder.is_valid(token))
    print('')

    print('-' * 50 + '\n')

    payload = Payload(    {
        'iss': 'tangoman.io',
        'user': {
            'firstname': 'Matthias',
            'lastname': 'Morin',
            'mail': 'mat@tangoman.io',
        }
    })
    token = jwt_encoder.encode(dict(payload))
    print(token)
    print('')

    decoded_token = jwt_encoder.decode(token)
    print(decoded_token)
    print('')

    print(jwt_encoder.is_valid(token))
    print('')


if __name__ == '__main__':
    main()
