board = [[0,0,0],[0,0,0],[0,0,0]]
symbol = [".","X","O"]

# Step 2.   
# 
# - create function to draw the board:
# -  call the function 

def draw_board():
    print()
    for row in board:
        print("-------------")
        print('|', symbol[row[0]], '|', symbol[row[1]], '|', symbol[row[2]], "|")
    print("-------------")
    print()

draw_board()