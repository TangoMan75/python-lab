#!/bin/python3
# -*- coding: utf-8 -*-

"""
 This file is part of the TangoMan Python Lab package.

 (c) "Matthias Morin" <mat@tangoman.io>

 For the full copyright and license information, please view the LICENSE
 file that was distributed with this source code.
"""

from typing import (List, Tuple, Optional)
from collections import Counter


class PokerHandStrengthCalculator:
    """
    PokerHandStrengthCalculator class to evaluate poker hand strength.
    """

    RANKS = {
        'A': 14,
        'K': 13,
        'Q': 12,
        'J': 11,
        'T': 10,
        '9': 9,
        '8': 8,
        '7': 7,
        '6': 6,
        '5': 5,
        '4': 4,
        '3': 3,
        '2': 2
    }

    SUITS = {
        'S': 4,
        'H': 3,
        'D': 2,
        'C': 1
    }

    HANDS = (
        'High card',
        'Pair',
        'Two pair',
        'Three of a kind',
        'Straight',
        'Flush',
        'Full House',
        'Four of a kind',
        'Straight flush',
        'Royal flush'
    )

    def __init__(self, community_cards: List[Tuple[str, str]], player_cards: List[Tuple[str, str]]):
        if not isinstance(community_cards, list):
            raise TypeError(f'{self.__init__.__qualname__}: expects parameter "community_cards" to be of type list: {type(community_cards)} given')

        if not isinstance(player_cards, list):
            raise TypeError(f'{self.__init__.__qualname__}: expects parameter "player_cards" to be of type list: {type(player_cards)} given')

        self.community_cards = community_cards
        self.player_cards = player_cards
        self.hand = None
        self.rank = None
        self.evaluate_hand()

    def evaluate_hand(self) -> None:
        """evaluate_hand"""
        cards = self.sort_cards(self.community_cards + self.player_cards)

        straight_flush = self.check_straight_flush(cards)
        if straight_flush and straight_flush[0][0] == 'A':
            self.rank = 9
            self.hand = straight_flush
            return

        if straight_flush:
            self.rank = 8
            self.hand = straight_flush
            return

        four_of_a_kind = self.check_four_of_a_kind(cards)
        if four_of_a_kind:
            self.rank = 7
            self.hand = four_of_a_kind
            return

        full_house = self.check_full_house(cards)
        if full_house:
            self.rank = 6
            self.hand = full_house
            return

        flush = self.check_flush(cards)
        if flush:
            self.rank = 5
            self.hand = flush
            return

        straight = self.check_straight(cards)
        if straight:
            self.rank = 4
            self.hand = straight
            return

        three_of_a_kind = self.check_three_of_a_kind(cards)
        if three_of_a_kind:
            self.rank = 3
            self.hand = three_of_a_kind
            return

        two_pair = self.check_two_pair(cards)
        if two_pair:
            self.rank = 2
            self.hand = two_pair
            return

        one_pair = self.check_one_pair(cards)
        if one_pair:
            self.rank = 1
            self.hand = one_pair
            return

        self.rank = 0
        self.hand = cards[0:5]

    def sort_cards(self, cards: List[str]) -> List[str]:
        """sort_cards"""
        # Sorts the given list of card tuples first by suit, then by rank, both in
        # descending order. This allows ranking hands where suits and ranks matter.
        cards = sorted(cards, key=lambda card: self.SUITS[card[1]], reverse=True)
        return sorted(cards, key=lambda card: self.RANKS[card[0]], reverse=True)

    def check_straight_flush(self, cards: List[Tuple[str, str]]) -> Optional[List[Tuple[str, str]]]:
        """check_straight_flush"""
        flush = self.get_flush(cards)
        if not flush:
            return None

        straight_flush = self.check_straight(flush)
        if not straight_flush:
            return None

        return straight_flush

    def check_four_of_a_kind(self, cards: List[Tuple[str, str]]) -> Optional[List[Tuple[str, str]]]:
        """check_four_of_a_kind"""
        rank_counts = Counter([card[0] for card in cards])
        for rank, count in rank_counts.items():
            if count == 4:
                kicker = [card for card in cards if rank not in card[0]]
                return [card for card in cards if rank in card[0]] + [kicker[0]]

        return None

    def check_full_house(self, cards: List[Tuple[str, str]]) -> Optional[List[Tuple[str, str]]]:
        """check_full_house"""
        rank_counts = Counter([card[0] for card in cards])
        three_of_a_kind = None
        pair = None

        for rank, count in rank_counts.items():
            if count == 3:
                three_of_a_kind = [card for card in cards if rank in card[0]]

            elif count == 2:
                pair = [card for card in cards if rank in card[0]]

        if not (three_of_a_kind and pair):
            return None

        return three_of_a_kind + pair

    def get_flush(self, cards: List[Tuple[str, str]]) -> Optional[List[Tuple[str, str]]]:
        """get_flush"""

        suit_counts = Counter([card[1] for card in cards])
        for suit, count in suit_counts.items():
            if count >= 5:
                return [card for card in cards if suit in card[1]]
        return None

    def check_flush(self, cards: List[Tuple[str, str]]) -> Optional[List[Tuple[str, str]]]:
        """check_flush"""
        flush = self.get_flush(cards)
        if flush:
            return flush[-5:]

        return None

    def check_straight(self, cards: List[Tuple[str, str]]) -> Optional[List[Tuple[str, str]]]:
        """check_straight"""
        # Checks if the given cards form a straight.
        # Iterates through all 5 card combinations, joins the ranks, and checks if
        # the straight pattern exists in the rank keys. Handles special case of
        # wheel straight. Returns the 5 card straight hand if found, else None.
        ranks = [card[0] for card in cards]
        for i in range(len(cards) - 4):
            if ''.join(ranks[i:i + 5]) in ''.join(self.RANKS):
                return cards[i:i + 5]

        if '5432' in ''.join(ranks) and cards[0][0] == 'A':
            hand = cards[-4:] + [cards[0]]
            return hand

        return None

    def check_three_of_a_kind(self, cards: List[Tuple[str, str]]) -> Optional[List[Tuple[str, str]]]:
        """check_three_of_a_kind"""
        rank_counts = Counter([card[0] for card in cards])
        for rank, count in rank_counts.items():
            if count == 3:
                three_of_a_kind = [card for card in cards if rank in card[0]]
                kicker = [card for card in cards if rank not in card[0]]
                return three_of_a_kind + kicker[:2]
        return None

    def check_two_pair(self, cards: List[Tuple[str, str]]) -> Optional[List[Tuple[str, str]]]:
        """check_two_pair"""
        rank_counts = Counter([card[0] for card in cards])
        pairs = [rank for rank, count in rank_counts.items() if count == 2]

        if len(pairs) < 2:
            return None

        pairs = sorted(pairs, key=lambda x: self.RANKS[x], reverse=True)
        high_pair = [card for card in cards if pairs[0] in card[0]]
        low_pair = [card for card in cards if pairs[1] in card[0]]
        kicker = [card for card in cards if pairs[0] not in card[0] and pairs[1] not in card[0]]

        return high_pair + low_pair + [kicker[0]]

    def check_one_pair(self, cards: List[Tuple[str, str]]) -> Optional[List[Tuple[str, str]]]:
        """check_one_pair"""
        rank_counts = Counter([card[0] for card in cards])
        for rank, count in rank_counts.items():
            if count == 2:
                pair = [card for card in cards if rank in card[0]]
                kicker = [card for card in cards if rank not in card[0]]
                return pair + kicker[:3]
        return None

    def get_rank(self):
        """get_rank"""
        return self.rank

    def get_hand(self):
        """get_hand"""
        return self.hand


def main():
    """main"""
    print('PokerHandStrengthCalculator')
    print('=' * 50 + '\n')

    # Royal flush
    community_cards = [('2', 'H'), ('3', 'H'), ('T', 'H'), ('J', 'H'), ('Q', 'H')]
    player_cards = [('A', 'H'), ('K', 'H')]
    hand_evaluator = PokerHandStrengthCalculator(community_cards, player_cards)
    print("Player's hand ranking:", hand_evaluator.HANDS[hand_evaluator.get_rank()], hand_evaluator.get_hand())

    # Straight flush
    community_cards = [('2', 'H'), ('3', 'H'), ('4', 'H'), ('5', 'H'), ('6', 'H')]
    player_cards = [('7', 'H'), ('8', 'H')]
    hand_evaluator = PokerHandStrengthCalculator(community_cards, player_cards)
    print("Player's hand ranking:", hand_evaluator.HANDS[hand_evaluator.get_rank()], hand_evaluator.get_hand())

    # Four of a kind
    community_cards = [('2', 'H'), ('2', 'D'), ('2', 'S'), ('3', 'C'), ('6', 'H')]
    player_cards = [('A', 'C'), ('2', 'C')]
    hand_evaluator = PokerHandStrengthCalculator(community_cards, player_cards)
    print("Player's hand ranking:", hand_evaluator.HANDS[hand_evaluator.get_rank()], hand_evaluator.get_hand())

    # Full House
    community_cards = [('2', 'H'), ('2', 'D'), ('3', 'S'), ('3', 'C'), ('3', 'H')]
    player_cards = [('7', 'H'), ('8', 'D')]
    hand_evaluator = PokerHandStrengthCalculator(community_cards, player_cards)
    print("Player's hand ranking:", hand_evaluator.HANDS[hand_evaluator.get_rank()], hand_evaluator.get_hand())

    # Flush
    community_cards = [('2', 'H'), ('4', 'H'), ('6', 'H'), ('8', 'C'), ('T', 'D')]
    player_cards = [('A', 'H'), ('8', 'H')]
    hand_evaluator = PokerHandStrengthCalculator(community_cards, player_cards)
    print("Player's hand ranking:", hand_evaluator.HANDS[hand_evaluator.get_rank()], hand_evaluator.get_hand())

    # Straight
    community_cards = [('2', 'H'), ('3', 'D'), ('4', 'H'), ('5', 'C'), ('6', 'H')]
    player_cards = [('7', 'S'), ('8', 'H')]
    hand_evaluator = PokerHandStrengthCalculator(community_cards, player_cards)
    print("Player's hand ranking:", hand_evaluator.HANDS[hand_evaluator.get_rank()], hand_evaluator.get_hand())

    # Three of a kind
    community_cards = [('2', 'H'), ('3', 'D'), ('3', 'H'), ('3', 'C'), ('6', 'H')]
    player_cards = [('7', 'S'), ('8', 'H')]
    hand_evaluator = PokerHandStrengthCalculator(community_cards, player_cards)
    print("Player's hand ranking:", hand_evaluator.HANDS[hand_evaluator.get_rank()], hand_evaluator.get_hand())

    # Two pair
    community_cards = [('2', 'H'), ('2', 'D'), ('3', 'H'), ('3', 'C'), ('6', 'H')]
    player_cards = [('7', 'S'), ('8', 'H')]
    hand_evaluator = PokerHandStrengthCalculator(community_cards, player_cards)
    print("Player's hand ranking:", hand_evaluator.HANDS[hand_evaluator.get_rank()], hand_evaluator.get_hand())

    # One pair
    community_cards = [('2', 'H'), ('3', 'D'), ('4', 'H'), ('4', 'C'), ('6', 'H')]
    player_cards = [('7', 'S'), ('8', 'H')]
    hand_evaluator = PokerHandStrengthCalculator(community_cards, player_cards)
    print("Player's hand ranking:", hand_evaluator.HANDS[hand_evaluator.get_rank()], hand_evaluator.get_hand())

    # High card
    community_cards = [('2', 'C'), ('4', 'D'), ('6', 'H'), ('8', 'C'), ('T', 'H')]
    player_cards = [('A', 'H'), ('K', 'H')]
    hand_evaluator = PokerHandStrengthCalculator(community_cards, player_cards)
    print("Player's hand ranking:", hand_evaluator.HANDS[hand_evaluator.get_rank()], hand_evaluator.get_hand())


if __name__ == '__main__':
    main()
