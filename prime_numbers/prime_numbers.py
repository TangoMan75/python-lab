#!/bin/python3
# -*- coding: utf-8 -*-

"""
 This file is part of the TangoMan Python Lab package.

 (c) "Matthias Morin" <mat@tangoman.io>

 For the full copyright and license information, please view the LICENSE
 file that was distributed with this source code.
"""


import math

class PrimeNumbers:
    """
    A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself.
    Examples include 2, 3, 5, and 7.
    """

    def is_prime(self, number):
        """is_prime"""
        if number < 1:
            raise ValueError(f'{self.is_prime.__qualname__} expects parameter "number" to be a positive integer: "{number}" given')

        for i in range(2, math.isqrt(number) + 1):
            if number % i == 0:
                return False

        return number > 1



def main():
    """main"""
    prime_numbers = PrimeNumbers()

    print('PrimeNumbers')
    print('=' * 50 + '\n')

    for i in range(1, 30):
        print(f'{i}: {prime_numbers.is_prime(i)}')
    print('')


if __name__ == '__main__':
    main()
