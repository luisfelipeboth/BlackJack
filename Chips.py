class Chips:
    '''
        Definition of chips bank for each player
    '''
    def __init__(self, total=100):  # Define a default number if none is given
        self.total = total
        self.bet = 0
    
    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet