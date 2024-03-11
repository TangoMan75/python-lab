#!/bin/python3
# -*- coding: utf-8 -*-

"""
 This file is part of the TangoMan Python Lab package.

 (c) "Matthias Morin" <mat@tangoman.io>

 For the full copyright and license information, please view the LICENSE
 file that was distributed with this source code.
"""

from player import *


class Human(Player):
    """Human - Extends Player class"""

    def play(self, game):
        y = int(input('Enter line number (1 a ' + str(game.size) + ') : '))
        x = int(input('Enter column number (1 a ' + str(game.size) + ') : '))
        return (x - 1, y - 1)

