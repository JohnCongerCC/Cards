print ("Welcome to the Text-Based Card Drawing Simulator")
import random

def main():
    deck = Deck()
    print (deck.Draw().getRank())
    print (deck.Draw().getSuit())

    deck.Shuffle()
    print (deck.Draw().getRank())
    print (deck.Draw().getSuit())

class Card:
    
    def __init__(self, suit, rank):

        self.suit = suit
        self.rank = rank

    def getSuit(self):

        return self.suit

    def getRank(self):

        return self.rank

class Deck:
    def __init__(self):
        self.cards = []
        suits = ["Clubs", "Diamonds", "Spades", "Hearts"]
        ranks = ["Ace", "King", "Queen", "Jack", "10","9","8","7","6","5","4","3","2"]
        for s in suits:
            for r in ranks:
                card = Card(s,r)
                self.cards.append(card)

    def Draw(self):
        return self.cards[0]

    def Shuffle(self):
           for i in range(len(self.cards) - 1, 0, -1):
                r = random.randint(0,i)
                self.cards[i], self.cards[r] = self.cards[r], self.cards[i]



main()
