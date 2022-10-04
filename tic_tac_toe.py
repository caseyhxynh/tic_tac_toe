MAX_ROUNDS = 9
NUM_ROWS = 3
NUM_COLS = 3
NUM_POSITIONS = 9
ROW_POS = 0
COL_POS = 1

def display_board(board):

   print("     0 1 2 ")

   for row in range(0, NUM_ROWS):
       print("  {}  ".format(row), end="")
       for col in range(0, NUM_COLS):
           if col == 0:
               print(board[(row, col)], end="")
           else:
               print("|{}".format(board[(row, col)]), end="")

       print(" ")

       if row < NUM_ROWS - 1:
           print("    --+-+--")
   print()


def reset_board(board):
   for key in board.keys():
       board[key] = ' '

def get_current_player(round):
   if round % 2 == 0:
    return 'X'
   elif round % 2 != 0:
    return 'O'
def get_position_choice(board, player_mark):
   print(player_mark + ',')
   inputs_valid = False
   position_valid = False
   while not inputs_valid:
       user_row = int(input("Choose your row: "))
       while user_row not in range(0, NUM_ROWS):
           user_row = int(input("Choose your row: "))
       user_col = int(input("Choose your column: "))
       while user_col not in range(0, NUM_COLS):
           user_col = int(input("Choose your column: "))
       print('')
       inputs_valid = True
       position_to_check = (user_row, user_col)
       if position_valid is False:
           for key in board.keys():
               if key == position_to_check:
                   if board[key] != ' ':
                       inputs_valid = False
                   else:
                       position_valid = True
   return (user_row, user_col)

def update_board(board, player_mark, position):
   for key in board.keys():
       if key == position:
           board[key] = player_mark

def display_outcome(round):
   if (round % 2 == 0) and (round < MAX_ROUNDS):
       print("X wins!\n")
   elif (round % 2 != 0) and (round < MAX_ROUNDS):
       print('O wins!\n')
   elif round == MAX_ROUNDS:
       print("It's a draw!\n")
   else:
       print("It's a draw!\n")

def check_positions(pos1_value, pos2_value, pos3_value):
   if pos1_value == 'X' and pos2_value == 'X' and pos3_value == 'X':
       return True
   elif pos1_value == 'O' and pos2_value == 'O' and pos3_value == 'O':
       return True
   else:
       return False

def is_game_complete(board):
   if check_positions(board[(0, 0)], board[(0, 1)], board[0, 2]):
       return True
   elif check_positions(board[(1, 0)], board[(1, 1)], board[1, 2]):
       return True
   elif check_positions(board[(1, 0)], board[(1, 1)], board[1, 2]):
       return True
   elif check_positions(board[(2, 0)], board[(2, 1)], board[2, 2]):
       return True
   elif check_positions(board[(0, 0)], board[(1, 0)], board[2, 0]):
       return True
   elif check_positions(board[(0, 1)], board[(1, 1)], board[2, 1]):
       return True
   elif check_positions(board[(0, 2)], board[(1, 2)], board[2, 2]):
       return True
   elif check_positions(board[(0, 0)], board[(1, 1)], board[2, 2]):
       return True
   elif check_positions(board[(0, 2)], board[(1, 1)], board[2, 0]):
       return True
   else:
       return False

def play_tic_tac_toe(board):
  print("Let's Play Tic-tac-toe!\n")
  round = 0
  play_game = 1
  display_board(board)
  while play_game == 1:
      while round < MAX_ROUNDS and not is_game_complete(board):
          player = get_current_player(round)
          position = get_position_choice(board, player)
          update_board(board, player, position)
          display_board(board)
          if is_game_complete(board):
              display_outcome(round)
              if is_program_finished():
                  print("Goodbye.")
                  play_game = 0
              else:
                  round = -1
                  reset_board(board)
          elif (round == MAX_ROUNDS - 1):
              round = MAX_ROUNDS
              display_outcome(round)
              if is_program_finished():
                  print("Goodbye.")
                  play_game = 0
              else:
                  round = -1
                  reset_board(board)
          round += 1

def is_program_finished():
   user_input = None
   while user_input != 'Y' or user_input != 'y' or user_input != 'N' or user_input != 'n':
       user_input = input("Play again (Y/N)? ")
       if user_input == 'Y' or user_input == 'y':
           print('')
           return False
       elif user_input == 'N' or user_input == 'n':
           print('')
           return True



def main():


   board = {
       (0,0): ' ', (0,1): ' ', (0,2): ' ',
       (1,0): ' ', (1,1): ' ', (1,2): ' ',
       (2,0): ' ', (2,1): ' ', (2,2): ' '
   }


   play_tic_tac_toe(board)

main()
