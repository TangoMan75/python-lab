#!/bin/python3
# -*- coding: utf-8 -*-

"""
 This file is part of the TangoMan Python Lab package.

 (c) "Matthias Morin" <mat@tangoman.io>

 For the full copyright and license information, please view the LICENSE
 file that was distributed with this source code.
"""


class FizzBuzz:
    """
    This script is inspired by the following Tom Scott video :
    "FizzBuzz: One Simple Interview Question"
    https://www.youtube.com/watch?v=QPZ0pIK_wsc
    """

    def fizzbuzz(self, number: int) -> int:
        """fizzbuzz"""
        if not isinstance(number, int):
            raise TypeError(f'{self.fizzbuzz.__qualname__}: expects parameter "number" to be of type int: {type(number)} given')

        if number < 1:
            raise ValueError(f'{self.fizzbuzz.__qualname__}: expects parameter "number" to be a positive integer: {str(number)} given')

        string = ''

        if number % 3 == 0:
            string = 'Fizz'

        if number % 5 == 0:
            string += 'Buzz'

        if string == '':
            return str(number)

        return string

    def fizzbuzz_alt(self, number: int) -> int:
        """fizzbuzz_alt"""
        if not isinstance(number, int):
            raise TypeError(f'{self.fizzbuzz.__qualname__}: expects parameter "number" to be of type int: {type(number)} given')

        if number < 1:
            raise ValueError(f'{self.fizzbuzz.__qualname__}: expects parameter "number" to be a positive integer: {str(number)} given')

        if number % 15 == 0:
            return 'FizzBuzz'

        if number % 3 == 0:
            return 'Fizz'

        if number % 5 == 0:
            return 'Buzz'

        return str(number)


def main():
    """main"""
    fizzbuzz = FizzBuzz()

    print('FizzBuzz')
    print('=' * 50 + '\n')

    for i in range(1, 20):
        print(fizzbuzz.fizzbuzz(i))
    print('')


if __name__ == '__main__':
    main()
