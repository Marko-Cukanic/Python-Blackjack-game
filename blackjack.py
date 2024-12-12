
import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}


playing = True

class Card: 
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.rank + ' of ' + self.suit
    
class Deck:
    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank))

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        return self.deck.pop()

class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        
    def add_card(self,card):
        self.cards.append(card) 
        self.value += card.value
        if card.value == 11 and self.value >= 21:
            self.value -= 11

class Chips:
    def __init__(self):
        self.total = 100
        self.bet = 0
        
    def __str__(self):
        return str(self.total) 

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet
    
# Game
## Game
game_on = True
chips = Chips() 
print("Welcome to blackjack")
while game_on:

    print(f"You currently have {chips.total} chips, choose how much you would like to bet on this game")
    
    try: 
        bet = int(input())
        if bet > chips.total or bet <=0:
            print("invalid bet amount. Try again")
            continue
    except ValueError:
        print("please enter a valid interger")
        continue
    chips.bet = bet  
    print(f"You have bet {chips.bet} chips.")

    print("bets are in lets begin by dealing")
    deck = Deck()
    deck.shuffle()
    
    myhand = Hand()
    dealershand = Hand()
    
    # Deal one card at a time and add it to the hand
    for _ in range(2):  # Deal two cards
        dealt_card = deck.deal()
        print(f"Dealt card: {dealt_card}")
        myhand.add_card(dealt_card)
    
    # Check the hand
    print(f"Your hand has {len(myhand.cards)} cards.")
    print(f"Total hand value: {myhand.value}")
    for card in myhand.cards:
        print(card)
    
    for _ in range(2):  # Deal two cards
        dealt_card = deck.deal()
        dealershand.add_card(dealt_card)
    print(f"The dealer has 2 cards with one of them being {dealt_card}")
    hitting = True
    while hitting:
        hitorstand = input("would you like to hit(1) or stand(2)")
        if hitorstand == '1':
            dealt_card = deck.deal()
            print(f"Dealt card: {dealt_card}")
            myhand.add_card(dealt_card)
            print(f"your hand value is {myhand.value}")
            if myhand.value > 21:
                print("You have busted the dealer has won")
                chips.lose_bet()
                hitting = False
                
        if hitorstand == '2':
            print("Now the dealer will go")
            dealerhitting = True
            while dealerhitting:
                if dealershand.value <= 17:
                    dealt_card = deck.deal()
                    dealershand.add_card(dealt_card)
                    print(f"The dealers hand value is {dealershand.value}")
                else:
                    print(f"The dealers hand value is {dealershand.value}")
                    dealerhitting = False
               
            if dealershand.value > 21:
                print("dealer busts you win")
                chips.win_bet()
            elif dealershand.value > myhand.value:
                print("Dealer wins!")
                chips.lose_bet()
            elif dealershand.value < myhand.value:
                print("You win!")
                chips.win_bet()
            else: 
                print("it was a tie so the house wins haha loser")
                chips.lose_bet()

            hitting = False 
    yn = input("would you like to keep playing y/n")
    if yn == "y":
        game_on = True
    elif yn == "n":
        game_on = False
  