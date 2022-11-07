from src.deck import Deck
from src.player import Player

class Game:

    def __init__(self, no_players: int) -> None:

        self.no_players = int
        self.deck = Deck()
        self.players = [Player(name=f"Player {i}") for i in range(no_players)]

        self.deck.shuffle()

        for player in self.players:
            hand = self.deck.draw(5)
            player.cards = hand
    
    def start(self):

        for player in self.players:

            print(f"{player.name} - here are your cards")
            [print(f"{idx}: {card}\n") for idx, card in enumerate(player.cards)]
            card_indexes = input(f"{player.name}, what cards do you want to swap? ").split(",")
            [player.cards.pop(int(i)) for i in card_indexes]
            self.deck.put_back([player.cards[int(i)] for i in card_indexes])
            self.deck.shuffle()
            player.cards += self.deck.draw(len(card_indexes))
            player.hand = player.judge_hand()

        winner = min(self.players, key=lambda a: a.hand)

        print(f"The winner is: {winner.name} with a {winner.hand.name}!")
        print(f"Their cards were:", ", ".join([str(card) for card in winner.cards]))