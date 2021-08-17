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

draw_board()

game_over = False

while not(game_over):
    player_make_move()
    computer_make_move()
    draw_board()

print("--- end of code ---")