from enum import Enum
from dataclasses import dataclass
from random import shuffle

import typing as tp

class Suit(Enum):
    """
        Class for defining suits of cards.
    """
    SPADES = 1
    CLUBS = 2
    DIAMONDS = 3
    HEARTS = 4

@dataclass
class Card:
    """
        Card object for each card in deck.
    """
    suit: Suit
    value: int

    def __str__(self) -> str:
        return f"{self.value} of {self.suit.name}"

class Deck:
    """
        Object for a deck of cards
    """

    def __init__(self) -> None:
        
        self.cards = self.create_deck()

    def __repr__(self) -> str:
        return str(self.cards)

    def shuffle(self) -> None:
        """
            Shuffles the cards, reordering the cards in the deck
        """

        shuffle(self.cards)

    def draw(self, no_cards: int) -> tp.List[Card]:
        """
            Draw a number of cards from the deck.

            Arguments:

                no_cards (int): Number of cards to draw.

            Returns:

                List[Card]: Cards that have been drawn.
        """

        return [self.cards.pop() for _ in range(no_cards)]

    def put_back(self, cards: tp.List[Card]) -> bool:
        """
            Put back a number of cards to the deck.

            Arguments:

                cards (List[Card]): Cards to put back
        """

        self.cards += cards
        return True

    @staticmethod
    def create_deck() -> 'Deck':
        """
            Create a new full deck of cards
        """

        return [Card(suit, value) for suit in list(Suit) for value in range(1, 14)]



