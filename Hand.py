class Hand:
    '''
        Definition of a hand of cards of the player
    '''
    def __init__(self, values):
        self.values = values
        self.hand_cards = []
        self.value = 0
        self.aces = 0

    def add_card(self, new_card):
        self.hand_cards.append(new_card)
        self.value += self.values[new_card.rank]

        # Keep traking the number of aces
        if new_card.rank == "Ace":
            self.aces += 1

    def adjust_for_ace(self):
        # If total value > 21 and still have an ace
        # Than change my ace value to 1 instead of 11
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1