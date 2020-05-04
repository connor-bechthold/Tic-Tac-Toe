
#Boolean value for the game status
game_still_going = True

#Current player
player_now = 'X'

#Variable for board
board = ['-', '-', '-',
         '-', '-', '-',
         '-', '-', '-']

#Boolean value for the winner of the game
winner = None

#Main playing game sequence
def play_game():

  display_board()
  
  while game_still_going:
    
    
    handle_turn(player_now)

    
    is_game_over()

    
    flip_turn()

  #Displays if there was a win or loss or tie
  if winner == 'X' or winner == 'O':
    print(winner + ' won.')
  elif winner == None:
    print('Tie')

#Function to display the board
def display_board():
  print(board[0] + ' | ' + board[1] + ' | ' + board[2] + '      1 | 2 | 3')
  print(board[3] + ' | ' + board[4] + ' | ' + board[5] + '      4 | 5 | 6')
  print(board[6] + ' | ' + board[7] + ' | ' + board[8] + '      7 | 8 | 9')

#Handles the turn of each player
def handle_turn(player):

  print('\n') 
  print(player + "'s turn")
  placement = input('Choose a number from 1 to 9: ')

  check = True
  while check:
    while placement not in ['1', '2', '3', '4', '5', '6', 
    '7', '8', '9']:
      placement = input('Choose a number from 1 to 9: ')

    placement = int(placement) - 1

    if board[placement] == '-':
      check = False
    else:
      print('This spot is unavailable.') 
  
      display_board()

  board[placement] = player

  display_board()

#Checks if the game is over
def is_game_over():
  check_if_win()
  check_if_tie()

#Checks if there is a win
def check_if_win():

  global winner 

  row_winner = check_rows()
  column_winner = check_columns()
  diagonal_winner = check_diagonals()

  if row_winner:
    winner = row_winner
  elif column_winner:
    winner = column_winner
  elif diagonal_winner:
    winner = diagonal_winner
  else:
    winner = None

#Checks each row of the board
def check_rows():

  global game_still_going

  row_1 = board[0] == board[1] == board[2] != "-"
  row_2 = board[3] == board[4] == board[5] != "-"
  row_3 = board[6] == board[7] == board[8] != "-"

  if row_1 or row_2 or row_3:
    game_still_going = False

  if row_1:
    return board[0]
  elif row_2:
    return board[3]
  elif row_3:
    return board[6]
  else:
    return None


#Checks each column of the board
def check_columns():

  global game_still_going

  column_1 = board[0] == board[3] == board[6] != "-"
  column_2 = board[1] == board[4] == board[7] != "-"
  column_3 = board[2] == board[5] == board[8] != "-"

  if column_1 or column_2 or column_3:
    game_still_going = False

  if column_1:
    return board[0]
  elif column_2:
    return board[1]
  elif column_3:
    return board[2]
  else:
    return None


#Checks each diagonal of the board
def check_diagonals():

  global game_still_going

  diagonal_1 = board[0] == board[4] == board[8] != "-"
  diagonal_2 = board[2] == board[4] == board[6] != "-"
  
  if diagonal_1 or diagonal_2:
    game_still_going = False

  if diagonal_1:
    return board[0]
  elif diagonal_2:
    return board[2]
  else:
    return None


#Checks if there is a tie
def check_if_tie():
  
  global game_still_going

  if '-' not in board:
    game_still_going = False
    return True
  else:
    return False

#Flips the turn of from 'X' to 'O'
def flip_turn():
  
  global player_now 
  
  if player_now == 'X':
    player_now = 'O'
  elif player_now == 'O':
    player_now = 'X'

#Initiates the game 
play_game()




