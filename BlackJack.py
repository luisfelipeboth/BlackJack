from os import system,name
import Chips
import Deck
import Hand

# Global variables
suits = ["Hearts","Clubs","Diamonds","Spades"]
ranks = ["Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten","Jack","Queen","King","Ace"]
values = {"Two":2,"Three":3,"Four":4,"Five":5,"Six":6,"Seven":7,
          "Eight":8,"Nine":9,"Ten":10,"Jack":10,"Queen":10,"King":10,"Ace":11}
playing = True

'''
    Functions to help in the game
'''
def clear_screen():
    if name == 'nt':
        _ = system("cls")
    else:
        _ = system("clear")

def take_bet(chips):
    while True:
        try:
            chips.bet = int(input("Please select your bet: "))
        except:
            print("Sorry, a bet must be an integer value!")
        else:
            if chips.bet > chips.total:
                print(f"Sorry, you bet can't exceed {chips.total}!")
            else:
                break

def hit(deck,hand):
    hand.add_card(deck.draw_one())
    hand.adjust_for_ace()

def hit_or_stand(deck, hand):
    global playing
    while True:
        x = input("Would you like to hit or stand? (H or S) ")
        if x[0].upper() == "H":
            hit(deck, hand)
        elif x[0].upper() == "S":
            print("Player stands. Dealer is playing.")
            playing = False
        else:
            print("Sorry, please try again!")
            continue
        break

def show_some(player, dealer):
    print("\nDealer's Hand:")
    print("<card hidden>")
    print(f"{dealer.hand_cards[1]}")
    print("\nPlayer's Hand:",*player.hand_cards, sep="\n")
    print(f"Player's Hand = {player.value}")

def show_all(player, dealer):
    print("\nDealer's Hand:",*dealer.hand_cards,sep="\n")
    print(f"Dealer's Hand = {dealer.value}")
    print("\nPlayer's Hand:",*player.hand_cards, sep="\n")
    print(f"Player's Hand = {player.value}")

def player_busts(player,dealer,chips):
    print("\nPlayer busts!")
    chips.lose_bet()

def player_wins(player,dealer,chips):
    print("\nPlayer wins!")
    chips.win_bet()

def dealer_busts(player,dealer,chips):
    print("\nDealer busts!")
    chips.win_bet()

def dealer_wins(player,dealer,chips):
    print("\nDealer wins!")
    chips.lose_bet()

def push(player,dealer):
    print("\nDealer and Player tie! It's a push.")

def main():
    clear_screen()
    global playing
    while True:
        # Print an opening statement
        print("Welcome to BlackJack! Get as close to 21 as you can without going over!\nDealer hits until she reaches 17. Aces count as 1 or 11.")
        # Create & shuffle the deck, deal two cards to each player
        new_deck = Deck.Deck(suits,ranks)
        new_deck.shuffle()
        player_hand = Hand.Hand(values)
        dealer_hand = Hand.Hand(values)
        player_hand.add_card(new_deck.draw_one())
        player_hand.add_card(new_deck.draw_one())
        dealer_hand.add_card(new_deck.draw_one())
        dealer_hand.add_card(new_deck.draw_one())

        # Set up the Player's chips
        player_chips = Chips.Chips()
        
        # Prompt the Player for their bet
        take_bet(player_chips)
        
        # Show cards (but keep one dealer card hidden)
        show_some(player_hand,dealer_hand)
        
        while playing:  # recall this variable from our hit_or_stand function
            
            # Prompt for Player to Hit or Stand
            hit_or_stand(new_deck,player_hand)
            
            # Show cards (but keep one dealer card hidden)
            show_some(player_hand,dealer_hand)
            
            # If player's hand exceeds 21, run player_busts() and break out of loop
            if player_hand.value > 21:
                player_busts(player_hand, dealer_hand, player_chips)
                break

        # If Player hasn't busted, play Dealer's hand until Dealer reaches 17
        if player_hand.value <= 21:
            while dealer_hand.value < 17:
                hit(new_deck,dealer_hand)
        
            # Show all cards
            show_all(player_hand,dealer_hand)

            # Run different winning scenarios
            if dealer_hand.value > 21:
                dealer_busts(player_hand,dealer_hand,player_chips)
            elif dealer_hand.value > player_hand.value:
                dealer_wins(player_hand,dealer_hand,player_chips)
            elif dealer_hand.value < player_hand.value:
                player_wins(player_hand,dealer_hand,player_chips)
            else:
                push(player_hand,dealer_hand)
                
        # Inform Player of their chips total 
        print(f"\nPlayer's winnings stand at {player_chips.total}")
        # Ask to play again
        new_game = input("Would you like to play another hand? (Y or N) ")
        if new_game[0].upper() == "Y":
            playing = True
            clear_screen()
            continue
        else:
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()