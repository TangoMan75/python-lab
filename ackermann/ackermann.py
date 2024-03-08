#!/bin/python3
# -*- coding: utf-8 -*-

"""
 This file is part of the TangoMan Python Lab package.

 (c) "Matthias Morin" <mat@tangoman.io>

 For the full copyright and license information, please view the LICENSE
 file that was distributed with this source code.
"""

from functools import lru_cache


class Ackermann:
    """
    The Ackermann function is a classic example of a recursive function that rows very quickly in value, as does the size of its call tree.
    This script was inspired by the following Computerfile video :
    https://www.youtube.com/embed/i7sm9dzFtEI
    """

    @lru_cache(maxsize=1000)
    def ackermann(self, m: int, n: int) -> int:
        """
        ackermann
        @param m: (int) The first parameter
        @param n: (int) The second parameter
        @return int: The result of the Ackermann function
        """

        if not isinstance(m, int):
            raise TypeError(f'{self.ackermann.__qualname__}: expects parameter "m" to be of type int: {type(m)} given')

        if m < 0:
            raise ValueError(f'{self.ackermann.__qualname__}: expects parameter "m" to be greater than "-1": {str(m)} given')

        if not isinstance(n, int):
            raise TypeError(f'{self.ackermann.__qualname__}: expects parameter "n" to be of type int: {type(n)} given')

        if n < 0:
            raise ValueError(f'{self.ackermann.__qualname__}: expects parameter "n" to be greater than "-1": {str(n)} given')

        if m == 0:
            return n + 1

        if n == 0:
            return self.ackermann(m - 1, 1)

        return self.ackermann(m - 1, self.ackermann(m, n - 1))


def main():
    """main"""
    ackermann = Ackermann()

    print('Ackermann')
    print('=' * 50 + '\n')

    for i in range(0, 6):
        for j in range(0, 6):
            print(f'ackermann ({i}, {j}) is : {ackermann.ackermann(i, j)}')
    print('')


if __name__ == '__main__':
    main()
