class Card:
    def __init__(self, suit, rank):

        self.suit = suit
        self.rank = rank

    def getsuit(self):
        return self.suit

    def getrank(self):
        return self.rank

class Deck:
    

card = Card("Club", "Ace")

print (card.getrank())
print (card.getsuit())
