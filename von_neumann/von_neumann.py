#!/bin/python3
# -*- coding: utf-8 -*-

"""
 This file is part of the TangoMan Python Lab package.

 (c) "Matthias Morin" <mat@tangoman.io>

 For the full copyright and license information, please view the LICENSE
 file that was distributed with this source code.
"""


class VonNeumann:
    """
    Von Neumann's method, also called the middle-square method, generates pseudorandom numbers by squaring a seed value and
    extracting the middle digits as the next number. This process repeats using the generated number as the new seed. While
    simple, it has limitations like potential patterns and periodicity.
    """

    def pseudo_random(self, seed: int) -> int:
        """pseudo_random"""
        if not isinstance(seed, int):
            raise TypeError(f'{self.pseudo_random.__qualname__}: expects parameter "seed" to be of type int: {type(seed)} given')

        if seed < 1:
            raise ValueError(f'{self.pseudo_random.__qualname__}: expects parameter "seed" to be a positive integer: {str(seed)} given')

        squared = str(seed ** 2)
        middle_digits = squared[len(squared) // 2 - 2:len(squared) // 2 + 2]
        seed = int(middle_digits)
        return seed


def main():
    """main"""
    von_neumann = VonNeumann()

    print('VonNeumann')
    print('=' * 50 + '\n')

    seed = 1234
    for _ in range(20):
        seed = von_neumann.pseudo_random(seed)
        print(seed)
    print('')


if __name__ == '__main__':
    main()
