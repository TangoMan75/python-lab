#!/bin/python3
# -*- coding: utf-8 -*-

"""
 This file is part of the TangoMan Python Lab package.

 (c) "Matthias Morin" <mat@tangoman.io>

 For the full copyright and license information, please view the LICENSE
 file that was distributed with this source code.
"""

from unittest import TestCase

from player import Player


class PlayerTest(TestCase):
    """
    PlayerTest
    """

    def test_player_init(self):
        """test_player_init"""
        player = Player('X')
        assert player.sign == 'X', 'Player sign should be initialized correctly'

    def test_player_play(self):
        """test_player_play"""
        player = Player('X')
        game = None
        assert player.play(game) == (0, 0), 'Player play method should return (0, 0)'

