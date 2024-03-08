#!/bin/python3
# -*- coding: utf-8 -*-

"""
 This file is part of the TangoMan Python Lab package.

 (c) "Matthias Morin" <mat@tangoman.io>

 For the full copyright and license information, please view the LICENSE
 file that was distributed with this source code.
"""

from unittest import TestCase

from poker import PokerHandStrengthCalculator


class TestPokerHandStrengthCalculator(TestCase):
    """TestPokerHandStrengthCalculator"""

    def test_community_cards_invalid_type(self):
        """==> community_cards should raise TypeError when set to invalid type"""
        with self.assertRaises(TypeError):
            PokerHandStrengthCalculator('invalid_type', [])

    def test_player_cards_invalid_type(self):
        """==> player_cards should raise TypeError when set to invalid type"""
        with self.assertRaises(TypeError):
            PokerHandStrengthCalculator([], 'invalid_type')

    def test_royal_flush(self):
        """==> royal flush should return expected result """
        community_cards = [('2', 'H'), ('3', 'H'), ('T', 'H'), ('J', 'H'), ('Q', 'H')]
        player_cards = [('A', 'H'), ('K', 'H')]

        expected_rank = 9
        expected_hand = [('A', 'H'), ('K', 'H'), ('Q', 'H'), ('J', 'H'), ('T', 'H')]

        hand_evaluator = PokerHandStrengthCalculator(community_cards, player_cards)
        self.assertEqual(hand_evaluator.get_rank(), expected_rank)
        self.assertEqual(hand_evaluator.get_hand(), expected_hand)

    def test_royal_flush_edge_case(self):
        """==> edge case royal flush should return expected result """
        community_cards = [('A', 'C'), ('A', 'S'), ('T', 'H'), ('J', 'H'), ('Q', 'H')]
        player_cards = [('A', 'H'), ('K', 'H')]

        expected_rank = 9
        expected_hand = [('A', 'H'), ('K', 'H'), ('Q', 'H'), ('J', 'H'), ('T', 'H')]

        hand_evaluator = PokerHandStrengthCalculator(community_cards, player_cards)
        self.assertEqual(hand_evaluator.get_rank(), expected_rank)
        self.assertEqual(hand_evaluator.get_hand(), expected_hand)

    def test_straight_flush(self):
        """==> check_straight_flush method should return expected result """
        community_cards = [('2', 'H'), ('3', 'H'), ('4', 'H'), ('5', 'H'), ('6', 'H')]
        player_cards = [('7', 'H'), ('8', 'H')]

        expected_rank = 8
        expected_hand = [('8', 'H'), ('7', 'H'), ('6', 'H'), ('5', 'H'), ('4', 'H')]

        hand_evaluator = PokerHandStrengthCalculator(community_cards, player_cards)
        self.assertEqual(hand_evaluator.get_rank(), expected_rank)
        self.assertEqual(hand_evaluator.get_hand(), expected_hand)

    def test_wheel_flush(self):
        """==> wheel check_straight_flush method should return expected result """
        community_cards = [('2', 'H'), ('3', 'H'), ('4', 'H'), ('5', 'C'), ('6', 'C')]
        player_cards = [('A', 'H'), ('5', 'H')]

        expected_rank = 8
        expected_hand = [('5', 'H'), ('4', 'H'), ('3', 'H'), ('2', 'H'), ('A', 'H')]

        hand_evaluator = PokerHandStrengthCalculator(community_cards, player_cards)
        self.assertEqual(hand_evaluator.get_rank(), expected_rank)
        self.assertEqual(hand_evaluator.get_hand(), expected_hand)

    def test_wheel_flush_edge_case(self):
        """==> edge case wheel check_straight_flush method should return expected result """
        community_cards = [('2', 'H'), ('3', 'H'), ('4', 'H'), ('5', 'H'), ('T', 'C')]
        player_cards = [('A', 'C'), ('A', 'H')]

        expected_rank = 8
        expected_hand = [('5', 'H'), ('4', 'H'), ('3', 'H'), ('2', 'H'), ('A', 'H')]

        hand_evaluator = PokerHandStrengthCalculator(community_cards, player_cards)
        self.assertEqual(hand_evaluator.get_rank(), expected_rank)
        self.assertEqual(hand_evaluator.get_hand(), expected_hand)

    def test_four_of_a_kind(self):
        """==> check_four_of_a_kind method should return expected result """
        community_cards = [('2', 'H'), ('2', 'D'), ('2', 'S'), ('3', 'C'), ('6', 'H')]
        player_cards = [('A', 'C'), ('2', 'C')]

        expected_rank = 7
        expected_hand = [('2', 'S'), ('2', 'H'), ('2', 'D'), ('2', 'C'), ('A', 'C')]

        hand_evaluator = PokerHandStrengthCalculator(community_cards, player_cards)
        self.assertEqual(hand_evaluator.get_rank(), expected_rank)
        self.assertEqual(hand_evaluator.get_hand(), expected_hand)

    def test_full_house(self):
        """==> check_full_house method should return expected result """
        community_cards = [('2', 'H'), ('2', 'D'), ('3', 'S'), ('3', 'C'), ('3', 'H')]
        player_cards = [('7', 'H'), ('8', 'D')]

        expected_rank = 6
        expected_hand = [('3', 'S'), ('3', 'H'), ('3', 'C'), ('2', 'H'), ('2', 'D')]

        hand_evaluator = PokerHandStrengthCalculator(community_cards, player_cards)
        self.assertEqual(hand_evaluator.get_rank(), expected_rank)
        self.assertEqual(hand_evaluator.get_hand(), expected_hand)

    def test_flush(self):
        """==> check_flush method should return expected result """
        community_cards = [('2', 'H'), ('4', 'H'), ('6', 'H'), ('8', 'C'), ('T', 'D')]
        player_cards = [('A', 'H'), ('8', 'H')]

        expected_rank = 5
        expected_hand = [('A', 'H'), ('8', 'H'), ('6', 'H'), ('4', 'H'), ('2', 'H')]

        hand_evaluator = PokerHandStrengthCalculator(community_cards, player_cards)
        self.assertEqual(hand_evaluator.get_rank(), expected_rank)
        self.assertEqual(hand_evaluator.get_hand(), expected_hand)

    def test_straight(self):
        """==> check_straight method should return expected result """
        community_cards = [('2', 'H'), ('3', 'D'), ('4', 'H'), ('5', 'C'), ('6', 'H')]
        player_cards = [('7', 'S'), ('8', 'H')]

        expected_rank = 4
        expected_hand = [('8', 'H'), ('7', 'S'), ('6', 'H'), ('5', 'C'), ('4', 'H')]

        hand_evaluator = PokerHandStrengthCalculator(community_cards, player_cards)
        self.assertEqual(hand_evaluator.get_rank(), expected_rank)
        self.assertEqual(hand_evaluator.get_hand(), expected_hand)

    def test_wheel(self):
        """==> wheel check_straight method should return expected result """
        community_cards = [('2', 'H'), ('3', 'C'), ('4', 'H'), ('T', 'C'), ('Q', 'C')]
        player_cards = [('A', 'H'), ('5', 'C')]

        expected_rank = 4
        expected_hand = [('5', 'C'), ('4', 'H'), ('3', 'C'), ('2', 'H'), ('A', 'H')]

        hand_evaluator = PokerHandStrengthCalculator(community_cards, player_cards)
        self.assertEqual(hand_evaluator.get_rank(), expected_rank)
        self.assertEqual(hand_evaluator.get_hand(), expected_hand)

    def test_wheel_edge_case(self):
        """==> edge case wheel check_straight method should return expected result """
        community_cards = [('2', 'H'), ('3', 'C'), ('4', 'H'), ('5', 'C'), ('Q', 'C')]
        player_cards = [('A', 'H'), ('6', 'C')]

        expected_rank = 4
        expected_hand = [('6', 'C'), ('5', 'C'), ('4', 'H'), ('3', 'C'), ('2', 'H')]

        hand_evaluator = PokerHandStrengthCalculator(community_cards, player_cards)
        self.assertEqual(hand_evaluator.get_rank(), expected_rank)
        self.assertEqual(hand_evaluator.get_hand(), expected_hand)

    def test_three_of_a_kind(self):
        """==> check_three_of_a_kind method should return expected result """
        community_cards = [('2', 'H'), ('3', 'D'), ('3', 'H'), ('3', 'C'), ('6', 'H')]
        player_cards = [('7', 'S'), ('8', 'H')]

        expected_rank = 3
        expected_hand = [('3', 'H'), ('3', 'D'), ('3', 'C'), ('8', 'H'), ('7', 'S')]

        hand_evaluator = PokerHandStrengthCalculator(community_cards, player_cards)
        self.assertEqual(hand_evaluator.get_rank(), expected_rank)
        self.assertEqual(hand_evaluator.get_hand(), expected_hand)

    def test_two_pair(self):
        """==> check_two_pair method should return expected result """
        community_cards = [('2', 'H'), ('2', 'D'), ('3', 'H'), ('3', 'C'), ('6', 'H')]
        player_cards = [('7', 'S'), ('8', 'H')]

        expected_rank = 2
        expected_hand = [('3', 'H'), ('3', 'C'), ('2', 'H'), ('2', 'D'), ('8', 'H')]

        hand_evaluator = PokerHandStrengthCalculator(community_cards, player_cards)
        self.assertEqual(hand_evaluator.get_rank(), expected_rank)
        self.assertEqual(hand_evaluator.get_hand(), expected_hand)

    def test_one_pair(self):
        """==> check_one_pair method should return expected result """
        community_cards = [('2', 'H'), ('3', 'D'), ('4', 'H'), ('4', 'C'), ('6', 'H')]
        player_cards = [('7', 'S'), ('8', 'H')]

        expected_rank = 1
        expected_hand = [('4', 'H'), ('4', 'C'), ('8', 'H'), ('7', 'S'), ('6', 'H')]

        hand_evaluator = PokerHandStrengthCalculator(community_cards, player_cards)
        self.assertEqual(hand_evaluator.get_rank(), expected_rank)
        self.assertEqual(hand_evaluator.get_hand(), expected_hand)

    def test_high_card(self):
        """==> check_high_card method should return expected result """
        community_cards = [('2', 'C'), ('4', 'D'), ('6', 'H'), ('8', 'C'), ('T', 'H')]
        player_cards = [('A', 'H'), ('K', 'H')]

        expected_rank = 0
        expected_hand = [('A', 'H'), ('K', 'H'), ('T', 'H'), ('8', 'C'), ('6', 'H')]

        hand_evaluator = PokerHandStrengthCalculator(community_cards, player_cards)
        self.assertEqual(hand_evaluator.get_rank(), expected_rank)
        self.assertEqual(hand_evaluator.get_hand(), expected_hand)
