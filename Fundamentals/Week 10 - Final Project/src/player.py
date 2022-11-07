from enum import IntEnum
from collections import Counter

class Hand(IntEnum):

    ROYAL_FLUSH = 1
    STRAIGHT_FLUSH = 2
    FOUR_OF_A_KIND = 3
    FULL_HOUSE = 4
    FLUSH = 5
    STRAIGHT = 6
    THREE_OF_A_KIND = 7
    TWO_PAIR = 8
    PAIR = 9
    HIGH_CARD = 10


class Player:
    
    def __init__(self, name: str = "") -> None:
        self.name = name
        self.cards = []
        self.hand = Hand.HIGH_CARD

    def judge_hand(self) -> Hand:

        if self.is_flush() and sorted([card.value for card in self.cards]) == sorted([1, 13, 12, 11, 10]):
            return Hand.ROYAL_FLUSH
        elif self.is_flush() and self.is_straight():
            return Hand.STRAIGHT_FLUSH
        elif self.value_counts() == [4, 1]:
            return Hand.FOUR_OF_A_KIND
        elif self.value_counts() == [3, 2]:
            return Hand.FULL_HOUSE
        elif self.is_flush():
            return Hand.FLUSH
        elif self.is_straight():
            return Hand.STRAIGHT
        elif self.value_counts() == [3, 1, 1]:
            return Hand.THREE_OF_A_KIND
        elif self.value_counts() == [2, 2, 1]:
            return Hand.TWO_PAIR
        elif self.value_counts() == [2, 1, 1, 1]:
            return Hand.PAIR
        else:
            return Hand.HIGH_CARD


    def is_flush(self):
        return all([self.cards[0].suit == card.suit for card in self.cards])

    def is_straight(self):
        values = [card.value for card in self.cards]
        royal = sorted(values) == [1, 10, 11, 12, 13] 
        main_case = sorted(values) == list(range(min(values), max(values) + 1))
        return royal or main_case

    def value_counts(self):
        value_counter = Counter([card.value for card in self.cards])
        return sorted(value_counter.values(), reverse=True)

