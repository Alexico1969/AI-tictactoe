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

draw_board()

# Step 4:
#
#           - ask for user input in while loop:

valid_move = False

while not(valid_move):
    pl_move = input("What's your move? ")