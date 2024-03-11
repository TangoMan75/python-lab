#!/bin/python3
# -*- coding: utf-8 -*-

"""
 This file is part of the TangoMan Python Lab package.

 (c) "Matthias Morin" <mat@tangoman.io>

 For the full copyright and license information, please view the LICENSE
 file that was distributed with this source code.
"""


from game import *
from player import *
from human import *
from bot import *

print('1 - Player vs player\n2 - Player vs bot\n3 - Bot vs player\n4 - Bot vs bot\n')

option = 0
while option < 1 or option > 4:
    option = int(input('Select game type : '))

if option == 1:
    Game(3, Human('X'), Human('O')).start()
elif option == 2:
    Game(3, Human('X'), Bot('O')).start()
elif option == 3:
    Game(3, Bot('X'), Human('O')).start()
else:
    Game(3, Bot('X'), Bot('O')).start()

