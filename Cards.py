import random

class Deck(object):
    deck = []
    ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    suits = ['club', 'spade', 'diamond', 'heart']

    def __init__(self):
        for rank in self.ranks:
            for suit in self.suits:
                self.deck.append(Card(rank, suit))
        random.shuffle(self.deck)

class Card:
    
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        self.colour = self.getColour()
        self.value = self.getValue()
        
    def getValue(self):
        # values for blackjack
        if self.rank == 'A':
            return 11
        elif self.rank == '2':
            return 2
        elif self.rank == '3':
            return 3
        elif self.rank == '4':
            return 4
        elif self.rank == '5':
            return 5
        elif self.rank == '6':
            return 6
        elif self.rank == '7':
            return 7
        elif self.rank == '8':
            return 8
        elif self.rank == '9':
            return 11
        elif self.rank == '10':
            return 10
        elif self.rank == 'J':
            return 10
        elif self.rank == 'Q':
            return 10
        elif self.rank == 'K':
            return 10
        else:
            return -1   #rank error

    def getColour(self):
        if self.suit == "club" or self.suit == "spade":
            return "black"
        elif self.suit == "heart" or self.suit == "diamond":
            return "red"
        else:
            return "COLOUR ERROR"
    
    def __str__(self):
        return f"{self.rank} of {self.suit}s"


if __name__ == "__main__":
    a = Deck()
    for item in a.deck:
        print(item)


