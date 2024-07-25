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
        rank_values = {
        'A': 11, '2': 2, '3': 3, '4': 4, '5': 5,
        '6': 6, '7': 7, '8': 8, '9': 9, '10': 10,
        'J': 10, 'Q': 10, 'K': 10
    }
    return rank_values.get(self.rank, -1)

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


