from src.player import Player, Hand
from src.deck import Card, Suit
import pytest

class TestPlayer:
    
    def test_init(self):
        test_player = Player()
        assert True

    def test_judge_royal_flush(self):
        test_player = Player()
        test_player.cards = [Card(suit=Suit.CLUBS, value=1)] + [Card(suit=Suit.CLUBS, value=i) for i in range(10, 14)]
        
        assert test_player.judge_hand() == Hand.ROYAL_FLUSH

    def test_judge_straight_flush(self):

        test_player = Player()
        test_player.cards = [Card(suit=Suit.CLUBS, value=i) for i in range(2, 7)]
        
        assert test_player.judge_hand() == Hand.STRAIGHT_FLUSH
    
    def test_judge_four_of_a_kind(self):
        test_player = Player()
        test_player.cards = [Card(suit=suit, value=1) for suit in list(Suit)] + [Card(suit=Suit.CLUBS, value=4)]
        
        assert test_player.judge_hand() == Hand.FOUR_OF_A_KIND
    
    def test_judge_full_house(self):
        test_player = Player()
        test_player.cards = [
            Card(suit=Suit.HEARTS, value=4),
            Card(suit=Suit.DIAMONDS, value=4),
            Card(suit=Suit.SPADES, value=4),
            Card(suit=Suit.CLUBS, value=2),
            Card(suit=Suit.SPADES, value=2),
        ]
        
        assert test_player.judge_hand() == Hand.FULL_HOUSE

    def test_judge_flush(self):
        test_player = Player()
        test_player.cards = [
            Card(suit=Suit.HEARTS, value=4),
            Card(suit=Suit.HEARTS, value=5),
            Card(suit=Suit.HEARTS, value=6),
            Card(suit=Suit.HEARTS, value=1),
            Card(suit=Suit.HEARTS, value=2),
        ]
        
        assert test_player.judge_hand() == Hand.FLUSH

    def test_judge_straight(self):
        test_player = Player()
        test_player.cards = [
            Card(suit=Suit.SPADES, value=4),
            Card(suit=Suit.HEARTS, value=5),
            Card(suit=Suit.HEARTS, value=3),
            Card(suit=Suit.HEARTS, value=1),
            Card(suit=Suit.HEARTS, value=2),
        ]
        
        assert test_player.judge_hand() == Hand.STRAIGHT

    def test_judge_three_of_a_kind(self):
        test_player = Player()
        test_player.cards = [
            Card(suit=Suit.SPADES, value=4),
            Card(suit=Suit.HEARTS, value=4),
            Card(suit=Suit.CLUBS, value=4),
            Card(suit=Suit.HEARTS, value=1),
            Card(suit=Suit.HEARTS, value=2),
        ]
        
        assert test_player.judge_hand() == Hand.THREE_OF_A_KIND

    def test_judge_two_pair(self):
        test_player = Player()
        test_player.cards = [
            Card(suit=Suit.SPADES, value=4),
            Card(suit=Suit.HEARTS, value=4),
            Card(suit=Suit.CLUBS, value=2),
            Card(suit=Suit.HEARTS, value=1),
            Card(suit=Suit.HEARTS, value=2),
        ]
        
        assert test_player.judge_hand() == Hand.TWO_PAIR

    def test_judge_pair(self):
        test_player = Player()
        test_player.cards = [
            Card(suit=Suit.SPADES, value=4),
            Card(suit=Suit.HEARTS, value=4),
            Card(suit=Suit.CLUBS, value=6),
            Card(suit=Suit.HEARTS, value=1),
            Card(suit=Suit.HEARTS, value=2),
        ]

        assert test_player.judge_hand() == Hand.PAIR

    def test_flush(self):

        test_player = Player()
        test_player.cards = [Card(suit=Suit.CLUBS, value=1)] + [Card(suit=Suit.CLUBS, value=i) for i in range(10, 14)]
        assert test_player.is_flush()

    def test_royal_straight(self):
        test_player = Player()
        test_player.cards = [Card(suit=Suit.CLUBS, value=1)] + [Card(suit=Suit.CLUBS, value=i) for i in range(10, 14)]
        assert test_player.is_straight()
    
    def test_normal_straight(self):
        test_player = Player()
        test_player.cards = [Card(suit=Suit.CLUBS, value=i) for i in range(2, 7)]
        assert test_player.is_straight()


