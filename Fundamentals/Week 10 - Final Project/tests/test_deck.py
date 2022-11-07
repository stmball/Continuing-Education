from src.deck import Card, Deck, Suit

import pytest

class TestCard:

    def test_init(self):
        test_card = Card(suit = Suit.CLUBS, value = 10)
        assert True

class TestDeck:

    def test_init(self):
        test_deck = Deck()
        assert Card(suit = Suit.CLUBS, value = 10) in test_deck.cards

    def test_number_of_cards(self):
        test_deck = Deck()
        assert len(test_deck.cards) == 52

    def test_draw_cards(self):
        test_deck = Deck()
        test_draw = test_deck.draw(5)

        assert len(test_draw) == 5
        assert len(test_deck.cards) == 47
        assert isinstance(test_draw[0], Card)

    def test_put_back(self):
        test_deck = Deck()
        test_draw = test_deck.draw(5)
        test_deck.put_back(test_draw)

        assert len(test_deck.cards) == 52
        assert Card(suit=Suit.HEARTS, value=13) in test_deck.cards