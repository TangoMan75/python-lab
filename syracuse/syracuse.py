#!/bin/python3
# -*- coding: utf-8 -*-

"""
 This file is part of the TangoMan Python Lab package.

 (c) "Matthias Morin" <mat@tangoman.io>

 For the full copyright and license information, please view the LICENSE
 file that was distributed with this source code.
"""


class Syracuse:
    """
    The Syracuse Conjecture, also known as the Collatz Conjecture, proposes that for any positive integer,
    if it is even, divide it by two, and if it is odd, multiply it by three and add one, and repeat this process.
    The conjecture suggests that no matter what number you start with, this sequence will eventually reach 1
    and then continue cycling between 1 and 4. It's an unsolved problem in mathematics.
    """

    def syracuse(self, number: int) -> int:
        """syracuse"""

        if not isinstance(number, int):
            raise TypeError(f'{self.syracuse.__qualname__}: expects parameter "number" to be of type int: {type(number)} given')

        if number < 1:
            raise ValueError(f'{self.syracuse.__qualname__}: expects parameter "number" to be a positive integer: {str(number)} given')

        if number == 1:
            return [number]

        if number % 2 == 0:
            return [number] + self.syracuse(number // 2)

        return [number] + self.syracuse((number * 3) + 1)


def main():
    """main"""
    syracuse = Syracuse()

    print('Syracuse')
    print('=' * 50 + '\n')

    for i in range(1, 25):
        print(f'{i}: {syracuse.syracuse(i)}')
    print('')


if __name__ == '__main__':
    main()
