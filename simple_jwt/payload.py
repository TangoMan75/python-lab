#!/bin/python3
# -*- coding: utf-8 -*-

"""
 This file is part of the TangoMan Python Lab package.

 (c) "Matthias Morin" <mat@tangoman.io>

 For the full copyright and license information, please view the LICENSE
 file that was distributed with this source code.
"""

from json import dumps
from time import time
from typing import Any
import secrets


class Payload:
    """
    Payload
    ======

    Payload features:

    Dunders
    -------
    - __eq__:   Implement equal operator
    - __hash__: Implement hash(self) method
    - __iter__: Allow object iteration, dict(self) and list(self) methods
    - __len__:  Return property count
    - __repr__: Return object as json string
    - __str__: Return object as json string

    Special attribute
    -----------------
    - __properties__: Return claims properties
    """

    ISSUER = 'iss'  # (Issuer) Claim
    SUBJECT = 'sub'  # (Subject) Claim
    AUDIENCE = 'aud'  # (Audience) Claim
    EXPIRATION_TIME = 'exp'  # (Expiration Time) Claim
    NOT_BEFORE = 'nbf'  # (Not Before) Claim
    ISSUED_AT = 'iat'  # (Issued At) Claim
    JWT_ID = 'jti'  # (JWT ID) Claim

    JWT_ID_LENGTH = 12

    def __init__(self, claims: dict = None) -> None:
        """Hydrate claims with given dictionary"""
        if claims is None:
            claims = {}

        if not isinstance(claims, dict):
            raise TypeError(f'{self.__init__.__qualname__}: expects parameter "claims" to be of type dict: {type(claims)} given')

        default = {
            self.JWT_ID: secrets.token_hex(self.JWT_ID_LENGTH),
            self.ISSUED_AT: int(time()),
        }
        self._claims = {**default, **claims}

    @property
    def __properties__(self) -> list:
        """Return claims keys"""
        return list(self._claims.keys())

    def __eq__(self, other: Any) -> bool:
        """Implement equal operator
        https://docs.python.org/3/reference/datamodel.html#object.__eq__
        """
        if not isinstance(other, type(self)):
            return False
        for key in list(self._claims.keys()):
            if self._claims[key] != dict(other)[key]:
                return False
        return True

    def __hash__(self) -> int:
        """Return object hash
        https://docs.python.org/3/reference/datamodel.html#object.__hash__
        """
        return hash(tuple(self._claims.values()))

    def __iter__(self) -> Any:
        """Allow object iteration
        https://docs.python.org/3/reference/datamodel.html#object.__iter__
        """
        for key, value in self._claims.items():
            yield key, value

    def __len__(self) -> int:
        """Return claims count
        https://docs.python.org/3/reference/datamodel.html#object.__len__
        """
        return len(self._claims.items())

    def __repr__(self) -> str:
        """Return object as json string
        https://docs.python.org/3/reference/datamodel.html#object.__repr__
        """
        return dumps(dict(self._claims))

    def __str__(self) -> str:
        """Return object as json string
        https://docs.python.org/3/reference/datamodel.html#object.__str__
        """
        return dumps(self._claims)


def main():
    """main"""
    payload = Payload({
        'id': 1,
        'login': 'TangoMan75',
        'firstname': 'Matthias',
        'lastname': 'Morin',
        'email': 'mat@tangoman.io',
    })

    print('Payload')
    print('=' * 50 + '\n')

    print('hash(payload)')
    print(hash(payload))
    print('')

    print('payload == payload(...)')
    print(payload == Payload({
        'id': 1,
        'login': 'TangoMan75',
        'firstname': 'Matthias',
        'lastname': 'Morin',
        'email': 'mat@tangoman.io',
    }))
    print('')

    print('payload.__properties__')
    print(payload.__properties__)
    print('')

    print('payload')
    print(payload)
    print('')

    print('list(payload)')
    print(list(payload))
    print('')

    print('dict(payload)')
    print(dict(payload))
    print('')

    print('len(payload)')
    print(len(payload))
    print('')

    for claim in payload:
        print(claim)


if __name__ == '__main__':
    main()
