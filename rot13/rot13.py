#!/bin/python3
# -*- coding: utf-8 -*-

"""
 This file is part of the TangoMan Python Lab package.

 (c) "Matthias Morin" <mat@tangoman.io>

 For the full copyright and license information, please view the LICENSE
 file that was distributed with this source code.
"""


class Rot13:
    """
    ROT13 is a simple letter substitution cipher that shifts each letter 13 positions forward in the alphabet. It's a weak
    encryption method commonly used for obfuscation and hiding spoilers. Applying ROT13 twice reverses the encryption.
    """

    def rot13(self, text: str) -> str:
        """rot13"""
        if not isinstance(text, str):
            raise TypeError(f'{self.rot13.__qualname__}: expects parameter "text" to be of type str: {type(text)} given')

        result = ''
        for char in text:
            if char.isalpha():
                ascii_offset = 65 if char.isupper() else 97
                rotated = (ord(char) - ascii_offset + 13) % 26 + ascii_offset
                result += chr(rotated)
            else:
                result += char

        return result


def main():
    """main"""
    rot13 = Rot13()

    print('Rot13')
    print('=' * 50 + '\n')

    print(rot13.rot13('EBG13 vf n fvzcyr yrggre fhofgvghgvba pvcure gung fuvsgf rnpu yrggre 13 cbfvgvbaf sbejneq va gur nycunorg.'))
    print(rot13.rot13('ROT13 is a simple letter substitution cipher that shifts each letter 13 positions forward in the alphabet.'))


if __name__ == '__main__':
    main()
