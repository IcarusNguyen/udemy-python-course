from random import shuffle

suits = 'hearts', 'diamonds', 'spades', 'clubs'
ranks = 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'jack', 'queen', 'king', 'ace'
values = {
  'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9, 'ten': 10, 'jack': 10, 'queen': 10, 'king': 10, 'ace': 11,
  2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9, 10: 10
}
playing = True

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f'{self.rank} of {self.suit}'
  
class Deck:
    def __init__(self):
        self.deck = [Card(suit, rank) for rank in ranks for suit in suits]

    def __str__(self):
        deck_comp = ''
        for card in self.deck:
            deck_comp += '\n' + card.__str__()
        return 'the deck has:' + deck_comp
    
    def shuffle(self):
        shuffle(self.deck)

    def deal(self):
        return self.deck.pop()

class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def addCard(self, card):
        self.cards.append(card)
        self.value += values[card.rank]
        if card.rank == 'ace':
            self.aces += 1

    def adjustForAce(self):
        while self.value > 21 and self.aces:
            self.value -= 10
        self.aces -= 1

class Chips:
    def __init__(self):
        self.total = 100
        self.bet = 0

    def winBet(self):
        self.total += self.bet

    def loseBet(self):
        self.total -= self.bet

def takeBet(chips):
    while True:
        try:
            chips.bet = int(input('how many chips would you like to bet? '))
        except:
            print('sr pls input an integer')
        else:
            if chips.bet > chips.total:
                print(f"sr, you don't have enough chips! you have: {chips.total}")
            else:
                break

def hit(deck, hand):
    single_card = deck.deal()
    hand.addCard(single_card)
    hand.adjustForAce()

def hitOrStand(deck, hand):
    global playing

    while True:
        x = input('hit or stand? ').lower()

        if x[0] == 'h':
            hit(deck, hand)
        elif x[0] == 's':
            print("player stands, dealer's turn")
            playing = False
        else:
            print("sr, pls enter 'hit' or 'stand' only!")
            continue

        break

def showSome(player, dealer):
    # show only 1 of the dealer's cards
    print("\ndealer's cards:")
    print("1st card's hidden")
    print(dealer.cards[1])
    # show all (2 cards) of player's cards/hand
    print("\nplayer's cards:", *player.cards, sep='\n')

def showAll(player, dealer):
    # calculate & display value (J+K==20)
    # show all of the dealer's cards
    print("\ndealer's cards:", *dealer.cards, sep='\n')
    print(f"value of dealer's hand is: {dealer.value}")
    # show all of player's cards/hand
    print("\nplayer's cards:", *player.cards, sep='\n')
    print(f"value of player's hand is: {player.value}")

def playerBusts(player, dealer, chips):
    print('player BUSTS!')
    chips.loseBet()

def playerWins(player, dealer, chips):
    print('player WINS!')
    chips.winBet()

def dealerBusts(player, dealer, chips):
    print('player WINS! dealer BUSTS!')
    chips.winBet()

def dealerWins(player, dealer, chips):
    print('dealer WINS!')
    chips.loseBet()

def push(player, dealer):
    print('dealer & player TIE! PUSH')

while True:
    print('welcome to blackjack')
    # create & shuffle the deck, deal 2 cards to player & dealer
    deck = Deck()
    deck.shuffle()
    player_hand = Hand()
    player_hand.addCard(deck.deal())
    player_hand.addCard(deck.deal())
    dealer_hand = Hand()
    dealer_hand.addCard(deck.deal())
    dealer_hand.addCard(deck.deal())
    player_chips = Chips()
    takeBet(player_chips) # prompt the player to bet
    showSome(player_hand, dealer_hand) # show cards, but keep 1 dealer card hidden

    while playing:
        hitOrStand(deck, player_hand) # prompt player to hit or stand
        showSome(player_hand, dealer_hand) # show cards, but keep 1 dealer card hidden

        # if player's hand exceeds 21, run playerBusts & break out of the loop
        if player_hand.value > 21:
            playerBusts(player_hand, dealer_hand, player_chips)
            break

        # if player hasn't busted, play dealer's hand until 17
        if player_hand.value < 21:
            while dealer_hand.value < 17:
                hit(deck, dealer_hand)
            showAll(player_hand, dealer_hand)

            # run different winning scenarios
            if dealer_hand.value > 21:
                dealerBusts(player_hand, dealer_hand, player_chips)
            elif dealer_hand.value > player_hand.value:
                dealerWins(player_hand, dealer_hand, player_chips)
            elif player_hand.value > dealer_hand.value:
                playerWins(player_hand, dealer_hand, player_chips)
            else:
                push(player_hand, dealer_hand)

        print(f"\nplayer's total chips: {player_chips.total}") # inform player of their total chips
        new_game = input('wanna play again, y/n: ').lower() # ask to play again

        if new_game[0] == 'y':
            playing = True
            continue
        else:
            print('tks for playing!')
            break

    break