import random


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f"{self.rank} of {self.suit}"


class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.score = 0

    def play_card(self, card):
        self.hand.remove(card)
        return card

    def add_card(self, card):
        self.hand.append(card)

    def add_score(self, points):
        self.score += points

    def __str__(self):
        return f"{self.name}: {self.score} points"


class Deck:
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']

    def __init__(self):
        self.cards = [Card(suit, rank) for suit in self.suits for rank in self.ranks]
        random.shuffle(self.cards)

    def deal(self, num_cards):
        return [self.cards.pop() for _ in range(num_cards)]


class BasraGame:
    def __init__(self):
        self.deck = Deck()
        self.players = [Player("Player 1"), Player("Player 2")]
        self.table = []

    def deal_initial_cards(self):
        for player in self.players:
            player.hand = self.deck.deal(4)
        self.table = self.deck.deal(4)

    def check_basra(self, card, table_card):
        return card.rank == table_card.rank

    def play_round(self):
        for player in self.players:
            print(f"{player.name}'s turn")
            print("Hand:", [str(card) for card in player.hand])
            card = player.play_card(player.hand[0])  
            print(f"{player.name} played {card}")

            captured = []
            for table_card in self.table:
                if self.check_basra(card, table_card):
                    captured.append(table_card)
                    player.add_score(10)  

            if captured:
                self.table = [c for c in self.table if c not in captured]
                print(f"Basra! {player.name} captured {captured}")
            else:
                self.table.append(card)

            print(f"Table: {[str(c) for c in self.table]}")
            print()

    def play_game(self):
        self.deal_initial_cards()
        for _ in range(4):  
            self.play_round()
        winner = max(self.players, key=lambda p: p.score)
        print(f"Game over! Winner: {winner}")


game = BasraGame()
game.play_game()