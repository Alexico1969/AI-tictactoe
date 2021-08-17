import random

board = [[0,0,0],[0,0,0],[0,0,0]]
symbol = [".","X","O"]

def draw_board():
    print()
    print("--A---B---C--")
    row_nr = 1
    for row in board:
        print("-------------")
        print('|', symbol[row[0]], '|', symbol[row[1]], '|', symbol[row[2]], "|", row_nr )
        row_nr += 1
    print("-------------")
    print()

def process_move(move,symb):
    move = move.upper()
    if not(len(move) == 2):
        print()
        print("*** Error: need 2 chars for input ***")
        return False

    move_y = move[0]
    move_x = move[1]

    if (not(move_y in 'ABC')):
        print("*** Error: unknown character 01 ***")
        return False

    if not(move_x in '123'):
        print("*** Error: unknown character 02 ***")
        return False

    if move_y == 'A':
        y_coord = 0
    elif move_y == 'B':
        y_coord = 1  
    elif move_y == 'C':
        y_coord = 2 

    x_coord = int(move_x) - 1

    cell_value = board[x_coord][y_coord]

    if not(cell_value == 0):
        print("*** Error: cell already taken ***")
        return False

    board[x_coord][y_coord] = symb
    
    return True

def player_make_move():
    valid_move = False

    while not(valid_move):
        pl_move = input("What's your move? ")
        if process_move(pl_move,1):
            valid_move = True



def computer_make_move():
    valid_move = False

    print("computer makes move")

    while not(valid_move):
        #string1 = "ABC"
        col = "ABC"[random.randint(0,2)]
        row = "123"[random.randint(0,2)]
        co_move = col + row
        if process_move(co_move,2):
            valid_move = True

# Step 8
#
#           Check if there is a winner
#           Adjust main game while loop

def check_win():
    win = False

    for i in range(3):
        if board[i][0] == board[i][1] and board[i][1] == board[i][2]:
            return board[i][0]
            break
    
    for i in range(3):
        if board[0][i] == board[1][i] and board[1][i] == board[2][i]:
            return board[0][i]
            break
   
    if board[0][0] == board[1][1] and board[1][1] == board[2][2]:
            return board[0][0]

    if board[2][0] == board[1][1] and board[1][1] == board[0][2]:
            return board[2][0]

    return 0

draw_board()

game_over = False

while not(game_over):
    player_make_move()
    computer_make_move()
    draw_board()
    result = check_win()
    if result != 0:
        print("*** THE WINNER IS : ", result)
        game_over = True
    




print("--- end of code ---")