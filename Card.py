class Card:
    '''
        Definition of a card, each card has a suit, rank and value associated
    '''
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f"{self.rank} of {self.suit}"