# Intro to AI Project 1: Gomoku
# Kyle Savell, Richard Valente, Henry Wheeler-Mackta

import os.path
from time import sleep

# Sample Board:
# #         A    B    C    D    E    F    G    H    I    J    K    L    M    N    O
# board = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",  # 1
#          " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",  # 2
#          " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",  # 3
#          " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",  # 4
#          " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",  # 5
#          " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",  # 6
#          " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",  # 7
#          " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",  # 8
#          " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",  # 9
#          " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",  # 10
#          " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",  # 11
#          " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",  # 12
#          " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",  # 13
#          " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",  # 14
#          " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "]  # 15

# Opponent = X
# We = O

#              A    B    C    D    E    F    G    H    I    J    K    L    M    N    O
cur_board = [[" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],  # 1
             [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],  # 2
             [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],  # 3
             [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],  # 4
             [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],  # 5
             [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],  # 6
             [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],  # 7
             [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],  # 8
             [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],  # 9
             [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],  # 10
             [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],  # 11
             [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],  # 12
             [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],  # 13
             [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],  # 14
             [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "]]  # 15

#                  A  B  C  D  E  F  G  H  I  J  K  L  M  N  O
cur_hueristics = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 1
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 2
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 3
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 4
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 5
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 6
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 7
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 8
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 9
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 10
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 11
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 12
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 13
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 14
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]  # 15


# Maps a column letter to an int
def parse_column(column):
    if column == "A":
        return 0
    elif column == "B":
        return 1
    elif column == "C":
        return 2
    elif column == "D":
        return 3
    elif column == "E":
        return 4
    elif column == "F":
        return 5
    elif column == "G":
        return 6
    elif column == "H":
        return 7
    elif column == "I":
        return 8
    elif column == "J":
        return 9
    elif column == "K":
        return 10
    elif column == "L":
        return 11
    elif column == "M":
        return 12
    elif column == "N":
        return 13
    elif column == "O":
        return 14
    elif column == 0:
        return "A"
    elif column == 1:
        return "B"
    elif column == 2:
        return "C"
    elif column == 3:
        return "D"
    elif column == 4:
        return "E"
    elif column == 5:
        return "F"
    elif column == 6:
        return "G"
    elif column == 7:
        return "H"
    elif column == 8:
        return "I"
    elif column == 9:
        return "J"
    elif column == 10:
        return "K"
    elif column == 11:
        return "L"
    elif column == 12:
        return "M"
    elif column == 13:
        return "N"
    elif column == 14:
        return "O"
    else:  # Unknown input
        return "error"


# Check files and parse move_file
def check_files():
    is_end = (os.path.isfile("end_game") or os.path.isfile("end_game.txt"))  # Check for turn
    our_turn = (os.path.isfile("gomokuguy.go") or os.path.isfile("gomokuguy.go.txt"))  # Check for turn

    if is_end:
        return 1  # End of game
    if our_turn:  # Place new enemy placement on board
        f = open("move_file.txt", "r")
        f_line = f.read()
        f.close()
        new_play = f_line.split(" ")
        print(new_play)
        cur_board[int(new_play[2])-1][parse_column(new_play[1])] = "X"
        return 0  # Success
    return -1  # Failure


# Writes turn to move_file
def write_turn(column, row):

    cur_board[row][column] = "O"  # Put our move on our board

    # Write to move_file
    f = open("move_file.txt", "w")
    f.write("gomokuguy "+parse_column(column)+" "+str(row+1))
    f.close()


# Prints the current playing board
def print_board():
    for row in cur_board:
        print(row)


# Runs the main program
def main():
    is_end = False
    our_turn = False

    while not is_end:
        print("Waiting for our turn...")
        while not our_turn:  # Wait for our turn
            file_output = check_files()
            if file_output == -1:
                sleep(0.1)  # (in seconds)
            if file_output == 0:
                our_turn = True
            if file_output == 1:
                is_end = True

        # Calculations for turn go here

        write_turn(2, 3)
        print_board()

        is_end = True  # Temp

main()
