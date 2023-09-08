import Card
import random

class Deck:
    '''
        Definition of a deck of cards, a list containing all the cards objects
    '''
    def __init__(self, suits, ranks):
        self.all_cards = []
        for suit in suits:
            for rank in ranks:
                self.all_cards.append(Card.Card(suit, rank))

    def __str__(self):
        deck_comp = ""
        for card in self.all_cards:
            deck_comp += "\n" + card.__str__()
        return "The deck has: " + deck_comp
    
    def shuffle(self):
        # Shuffles the deck
        random.shuffle(self.all_cards)

    def draw_one(self):
        return self.all_cards.pop()