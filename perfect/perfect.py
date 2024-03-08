#!/bin/python3
# -*- coding: utf-8 -*-

"""
 This file is part of the TangoMan Python Lab package.

 (c) "Matthias Morin" <mat@tangoman.io>

 For the full copyright and license information, please view the LICENSE
 file that was distributed with this source code.
"""


class Perfect:
    """
    A perfect number is a positive integer that is equal to the sum of its proper divisors,
    which are the positive integers that divide the number without leaving a remainder
    and are less than the number itself.
    """

    def is_perfect(self, number: int) -> bool:
        """is_perfect"""
        if not isinstance(number, int):
            raise TypeError(f'{self.is_perfect.__qualname__}: expects parameter "number" to be of type int: {type(number)} given')

        if number < 0:
            raise ValueError(f'{self.is_perfect.__qualname__}: expects parameter "number" to be greater than "-1": {str(number)} given')

        # Find the sum of the proper divisors of number
        divisor_sum = 0
        for i in range(1, number):
            if number % i == 0:
                divisor_sum += i

        # Check if the sum of the proper divisors is equal to number
        return divisor_sum == number


def main():
    """main"""
    perfect = Perfect()

    print('Perfect')
    print('=' * 50 + '\n')

    for i in range(1, 30):
        print(f'{i}: {perfect.is_perfect(i)}')
    print('')


if __name__ == '__main__':
    main()
