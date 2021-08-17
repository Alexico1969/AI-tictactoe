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

# Step 5.
# 
#           - process user_input

def process_move(move):
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

    board[x_coord][y_coord] = 1
    
    return True


draw_board()



valid_move = False

while not(valid_move):
    pl_move = input("What's your move? ")
    if process_move(pl_move):
        valid_move = True

draw_board()

print("--- end of code ---")