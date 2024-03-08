#!/bin/python3
# -*- coding: utf-8 -*-

"""
 This file is part of the TangoMan Python Lab package.

 (c) "Matthias Morin" <mat@tangoman.io>

 For the full copyright and license information, please view the LICENSE
 file that was distributed with this source code.
"""


class HelloWorld:
    """
    Returns "Hello World!" string
    """

    def hello_world(self) -> str:
        """hello_world"""
        return 'Hello World!'


def main():
    """main"""
    hello_world = HelloWorld()

    print('HelloWorld')
    print('=' * 50 + '\n')

    for _ in range(0, 10):
        print(hello_world.hello_world())
    print('')


if __name__ == '__main__':
    main()
