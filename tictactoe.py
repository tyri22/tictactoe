""" tic tac toe game

- make a board
- think about user input
- user can enter 1-9 to place on board or x to exit
- check for valid inputs, prompt user to try again if not valid
- add piece to board : check rows, cols, diagonals
- check if winning move
- print board after each input
- have to switch between two users
- have to end game if x entered or game won
   
"""

board = [
    ['-','-','-'],
    ['-','-','-'],
    ['-','-','-'],
]
game_playing = True

def board_status(board):
    #prints out board
    for row in board:
        for space in row:
            print(space, end='')
        print()

def user_exit(user_input):
    if user_input.lower() == 'x':
        print('Thanks for playing!')
        game_playing = False
        return True
    else:
        return False

def check_num(user_input):
    if user_input.isnumeric():
        return True
    else: 
        return False

def valid_num(user_input):
    if check_num(user_input):
        if int(user_input) > 9 or int(user_input) < 1:
            print("Not a valid number, try again.")
            return False
        else:
            return True

def coordinates(user_input):
    act_num = int(user_input) - 1
    row = act_num / 3
    col = act_num
    if col > 2:
        col = col % 3
    return row, col

def add_to_board(curr_user, user_input, board):
    coords =  coordinates(user_input)
    row = int(coords[0])
    col = int(coords[1])
    if board[row][col] != '-':
        print('Oops! That space is taken, try again.')
    else:
        board[row][col] = curr_user

def check_rows(curr_user, board):
    complete_row = 0
    for row in board:
        for space in row:
            if space == curr_user:
                complete_row += 1
                if complete_row == 3:
                    return True
                    break
            else:
                complete_row = 0
    return False

def check_cols(curr_user, board):
    if board[0][0] == board[1][0] == board[2][0] == curr_user:
        return True
    elif board[0][1] == board[1][1] == board[2][1] == curr_user:
        return True
    elif board[0][2] == board[1][2] == board[2][2] == curr_user:
        return True
    else:
        return False

def check_diags(curr_user, board):
    if board[0][0] == board[1][1] == board[2][2] == curr_user:
        return True
    elif board[0][2] == board[1][1] == board[2][0] == curr_user:
        return True
    else:
        return False

def is_win(curr_user):
    if check_rows(curr_user, board) or check_cols(curr_user, board) or check_diags(curr_user, board):
        game_playing = False
        print(f'Player {curr_user} won!')
    
while game_playing:
    board_status(board)
    curr_user = 'X'

    user_toggle = lambda x: 'O' if x == 'X' else 'X'

    user_input = input('Choose a number 1-9 or X to exit: ')
    if user_exit(user_input):
        break
    valid_num(user_input)
    add_to_board(curr_user, user_input, board)
    if is_win(curr_user):
        break
    user_toggle(curr_user)


# board_status(board)
# user_input = input("choose a space or x to exit: ")
# user_exit(user_input)
# check_num(user_input)
# valid_num(user_input)
# coordinates(user_input)
# add_to_board(curr_user, user_input, board)
# board_status(board)
# is_win(curr_user, board)
