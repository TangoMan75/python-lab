#!/bin/python3
# -*- coding: utf-8 -*-

"""
 This file is part of the TangoMan Python Lab package.

 (c) "Matthias Morin" <mat@tangoman.io>

 For the full copyright and license information, please view the LICENSE
 file that was distributed with this source code.
"""

from functools import lru_cache


class Fibonacci:
    """
    The Fibonacci sequence is a mathematical pattern where each number is the sum of the previous two numbers.
    """

    @lru_cache(maxsize=1000)
    def fib(self, number: int) -> int:
        """
        Fn+1 = Fn + Fn-1
        fib(1) == 1
        fib(2) == 1
        fib(3) == 1+1 == 2
        fib(4) == 2+1 == 3
        fib(5) == 3+2 == 5
        fib(6) == 5+3 == 8
        n < 1 == ValueError
        """

        if not isinstance(number, int):
            raise TypeError(f'{self.fib.__qualname__}: expects parameter "number" to be of type int: {type(number)} given')

        if number < 1:
            raise ValueError(f'{self.fib.__qualname__}: expects parameter "number" to be a positive integer: {str(number)} given')

        if number <= 2:
            return 1

        return self.fib(number - 1) + self.fib(number - 2)


def main():
    """main"""
    fibonacci = Fibonacci()

    print('Fibonacci')
    print('=' * 50 + '\n')

    for i in range(1, 25):
        print(f'{i}: {fibonacci.fib(i)}')
    print('')


if __name__ == '__main__':
    main()
