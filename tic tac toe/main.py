import os
from random import randint


def displayBoard(board):
  os.system('cls' if os.name=='nt' else 'clear')
  print(f'{board[7]}|{board[8]}|{board[9]}')
  print('-----')
  print(f'{board[4]}|{board[5]}|{board[6]}')
  print('-----')
  print(f'{board[1]}|{board[2]}|{board[3]}')


def playerInput():
  marker = ''
  while not (marker == 'X' or marker == 'O'):
    marker = input('player 1, choose X or O: ').upper()
  return ('X', 'O') if marker == 'X' else ('O', 'X')


def placeMarker(board, marker, position):
  board[position] = marker.upper()


def winCheck(board, mark):
  return (
    (board[7] == board[8] == board[9] == mark.upper()) or
    (board[4] == board[5] == board[6] == mark.upper()) or
    (board[1] == board[2] == board[3] == mark.upper()) or
    (board[7] == board[4] == board[1] == mark.upper()) or
    (board[8] == board[5] == board[2] == mark.upper()) or
    (board[9] == board[6] == board[3] == mark.upper()) or
    (board[7] == board[5] == board[3] == mark.upper()) or
    (board[1] == board[5] == board[9] == mark.upper())
  )


def chooseFirst():
  flip = randint(0, 1)
  return 'player 1' if flip == 0 else 'player 2'


def spaceCheck(board, position):
  return board[position] == ' '


def fullBoardCheck(board):
  for i in range(1, 10):
    if spaceCheck(board, i):
      return False
  return True


def playerChoice(board):
  position = 0
  if position not in [1,2,3,4,5,6,7,8,9] or spaceCheck(board, position):
    position = int(input('choose a position (1-9): '))
  return position


def replay():
  choice = input('play again, Yes or No? ').title()
  return choice == 'Yes' or choice =='Y'


print('welcome to Tic Tac Toe')

while True:
  board = [' '] * 10
  player1, player2 = playerInput()
  turn = chooseFirst()
  print(turn + ' will go 1st')
  play = ''
  while play != 'y':
    play = input('ready to play, y or n? ').lower()

  if play == 'y' or play =='yes':
    game_on = True
  else:
    game_on = False

  while game_on:
    if turn == 'player 1':
      displayBoard(board)
      position = playerChoice(board)
      placeMarker(board, player1, position)

      if winCheck(board, player1):
        displayBoard(board)
        print('player 1 WON!')
        game_on = False
      else:
        if fullBoardCheck(board):
          displayBoard(board)
          print('TIE')
          game_on = False
        else:
          turn = 'player 2'
    else:
      displayBoard(board)
      position = playerChoice(board)
      placeMarker(board, player2, position)

      if winCheck(board, player2):
        displayBoard(board)
        print('player 2 WON!')
        game_on = False
      else:
        if fullBoardCheck(board):
          displayBoard(board)
          print('TIE')
          game_on = False
        else:
          turn = 'player 1'

  if not replay():
    break