#!/bin/python3
# -*- coding: utf-8 -*-

"""
 This file is part of the TangoMan Python Lab package.

 (c) "Matthias Morin" <mat@tangoman.io>

 For the full copyright and license information, please view the LICENSE
 file that was distributed with this source code.
"""

from functools import lru_cache


class Factorial:
    """
    In mathematics, the factorial of a non-negative integer is the product of all positive integers less than or equal to that integer.

    3! == 3x2x1 == 6
    2! == 2x1 == 2
    1! == 1 == 1
    0! == 1 (by convention)
    n < 0 == ValueError
    """

    @lru_cache(maxsize=1000)
    def factorial(self, number: int) -> int:
        """
        Compute factorial recursively

        @param n: number to compute factorial
        @return: factorial of n
        """

        if not isinstance(number, int):
            raise TypeError(f'{self.factorial.__qualname__}.factorial: expects parameter "number" to be of type int: {type(number)} given')

        if number < 0:
            raise ValueError(f'{self.factorial.__qualname__}.factorial: expects parameter "number" to be greater than "-1": {str(number)} given')

        if number == 0:
            return 1

        return number * self.factorial(number - 1)

    @lru_cache(maxsize=1000)
    def factorial_iterative(self, number: int) -> int:
        """
        Compute factorial iteratively

        @param n: number to compute factorial
        @return: factorial of n
        """

        if not isinstance(number, int):
            raise TypeError(f'{self.factorial.__qualname__}.factorialIterative: expects parameter "number" to be of type int: {type(number)} given')

        if number < 0:
            raise ValueError(f'{self.factorial.__qualname__}.factorialIterative: expects parameter "number" to be greater than "-1": {str(number)} given')

        result = 1

        for i in range(1, number + 1):
            result *= i

        return result


def main():
    """main"""
    factorial = Factorial()

    print('Factorial')
    print('=' * 50 + '\n')

    for i in range(1, 25):
        print(f'{i}: {factorial.factorial(i)}')
    print('')


if __name__ == '__main__':
    main()
