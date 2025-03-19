from random import shuffle


suits = 'hearts', 'diamonds', 'spades', 'clubs'
ranks = 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'jack', 'queen', 'king', 'ace'
values = {
  'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9, 'ten': 10, 'jack': 11, 'queen': 12, 'king': 13, 'ace': 14,
  2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9, 10: 10
}


class Card:
  def __init__(self, suit, rank):
    self.suit = suit
    self.rank = rank
    self.value = values[rank]

  def __str__(self):
    return f'{self.rank} of {self.suit}'


class Deck:
  def __init__(self):
    self.all_cards = [Card(suit, rank) for rank in ranks for suit in suits]

  def shuffle(self):
    shuffle(self.all_cards)

  def dealOne(self):
    return self.all_cards.pop()


class Player:
  def __init__(self, name):
    self.name = name
    self.all_cards = []

  def removeOne(self):
    return self.all_cards.pop(0)

  def addCards(self, new_cards):
    if type(new_cards) == type([]):
      self.all_cards.extend(new_cards)
    else:
      self.all_cards.append(new_cards)

  def __str__(self):
    return f'player {self.name} has {len(self.all_cards)} cards'


player1 = Player('ONE')
player2 = Player('TWO')
new_deck = Deck()
new_deck.shuffle()

for _ in range(26):
  player1.addCards(new_deck.dealOne())
  player2.addCards(new_deck.dealOne())

game_on = True
round_num = 0

while game_on:
  round_num += 1
  print(f'round {round_num}')

  if len(player1.all_cards) == 0:
    print('ONE is out of cards, TWO WINS!')
    game_on = False
    break

  if len(player2.all_cards) == 0:
    print('TWO is out of cards, ONE WINS!')
    game_on = False
    break

  player1_cards = []
  player2_cards = []
  player1_cards.append(player1.removeOne())
  player2_cards.append(player2.removeOne())
  at_war = True

  while at_war:
    if player1_cards[-1].value > player2_cards[-1].value:
      player1.addCards(player1_cards)
      player1.addCards(player2_cards)
      at_war = False
    elif player1_cards[-1].value < player2_cards[-1].value:
      player2.addCards(player1_cards)
      player2.addCards(player2_cards)
      at_war = False
    else:
      print('WAR!')

      if len(player1.all_cards) < 3:
        print('player ONE unable to declare war')
        print('player TWO WINS')
        game_on = False
        break
      elif len(player2.all_cards) < 3:
        print('player TWO unable to declare war')
        print('player ONE WINS')
        game_on = False
        break
      else:
        for _ in range(3):
          player1_cards.append(player1.removeOne())
          player2_cards.append(player2.removeOne())