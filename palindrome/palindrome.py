#!/bin/python3
# -*- coding: utf-8 -*-

"""
 This file is part of the TangoMan Python Lab package.

 (c) "Matthias Morin" <mat@tangoman.io>

 For the full copyright and license information, please view the LICENSE
 file that was distributed with this source code.
"""


class Palindrome:
    """
    A palindrome is a word, phrase, or number that reads the same backward as it does forward.
    """

    def is_palindrome(self, string: str) -> str:
        """is_palindrome"""
        if not isinstance(string, str):
            raise TypeError(f'{self.is_palindrome.__qualname__}: expects parameter "string" to be of type str: {type(string)} given')

        reverse = string[::-1]
        if string == reverse:
            return True

        return False

    def is_palindrome_recursive(self, string: str) -> str:
        """is_palindrome_recursive"""
        if not isinstance(string, str):
            raise TypeError(f'{self.is_palindrome_recursive.__qualname__}: expects parameter "string" to be of type str: {type(string)} given')

        if len(string) < 1:
            return True

        if string[0] == string[-1]:
            return self.is_palindrome_recursive(string[1:-1])

        return False


def main():
    """main"""
    palindrome = Palindrome()

    print('Palindrome')
    print('=' * 50 + '\n')

    print('Is "racecar" a palindrome ? ')
    print(palindrome.is_palindrome('racecar'))


if __name__ == '__main__':
    main()
