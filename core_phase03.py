board = [[0,0,0],[0,0,0],[0,0,0]]
symbol = [".","X","O"]

# Step 3:
#
#           - expand the board (ABC and 123)

def draw_board():
    print()
    print("--A---B---C--")
    row_nr = 1
    for row in board:
        print("-------------")
        print('|', symbol[row_nr], '|', symbol[row_nr], '|', symbol[row_nr], "|", row_nr )
        row_nr += 1
    print("-------------")
    print()

draw_board()

