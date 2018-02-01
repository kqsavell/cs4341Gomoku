# Intro to AI Project 1: Gomoku
# Kyle Savell, Richard Valente, Henry Wheeler-Mackta
# AI Name: Gomokuguy

import copy
import os.path
from time import sleep

# 0 = Blank
# 1 = Player One Bead (White)
# 2 = Player Two Bead (Black)
#             A  B  C  D  E  F  G  H  I  J  K  L  M  N  O
cur_board = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 1
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
X = 0  # 0th element of x-y array
Y = 1  # 1st element of x-y array
MAX_DEPTH = 4  # Build and search depth of decision tree


# Class for Game Node, holds a board state
class GameNode:
    def __init__(self, move, value, parent):
        """
        Game Nodes contain a potential board state
        :param move: the move to make as row-column coords (1, 2)
        :param value: the board state, same structure as the cur_board
        :param parent: the parent game node
        """
        self.move = move  # the move to make
        self.value = value  # the minimax value
        self.parent = parent  # reference to the parent GameNode
        self.children = []  # a list of all children GameNodes

    def add_child_node(self, childNode):
        """
        Add a child node to the GameNode
        :param childNode: the child to add
        :return:
        """
        self.children.append(childNode)


# Class for the Decision Tree, where each node is a board state
class DecisionTree:
        def __init__(self):
            self.root = None  # by default, no root
            self.board = []  # Starting board is the current board
            self.last_depth = 0  # Depth of last created node, used for backtracking
            self.lvtwo_dup = []  # Holds unique nodes for depth 2
            self.lvthree_dup = []  # Holds unique nodes for depth 3

        def build_tree(self):
            """
            Builds the tree from a given board state
            :return: the root of the tree
            """
            self.root = GameNode(None, None, None)  # Starting node is empty
            for row in cur_board:  # copy cur board configuration
                self.board.append(copy.copy(row))
            data_list = self.list_moves(self.board)
            for element in data_list:
                self.parse_subtree(element, self.root, 2, self.board)  # parse the subtree and hook it up to the root
            return self.root

        def list_moves(self, board):
            """
            Gets list of possible first-order moves from current node
            :return: data list of possible moves
            """
            stone_pos = []  # List of positions taken up by stones
            move_list = []  # List of possible move positions given stone positions
            i, j = 0, 0

            # Generate list of stone positions
            for row in board:
                for element in row:
                    if element is not 0:  # If stone is there, add position to list
                        stone_pos.append([i, j])  # in row-column format
                    j += 1
                i += 1
                j = 0

            # Generate list of moves from current stone positions
            for pos in stone_pos:
                # Vertical positions
                x, y = 0, -4
                while y <= 4:  # B to T
                    new_move = [pos[0] + y, pos[1]]
                    if new_move not in move_list and new_move not in stone_pos:
                        if 0 <= new_move[0] <= 14 and 0 <= new_move[1] <= 14:
                            move_list.append(new_move)
                    y += 1

                # Horizontal positions
                x, y = -4, 0
                while x <= 4:  # L to R
                    new_move = [pos[0], pos[1] + x]
                    if new_move not in move_list and new_move not in stone_pos:
                        if 0 <= new_move[0] <= 14 and 0 <= new_move[1] <= 14:
                            move_list.append(new_move)
                    x += 1

                # Diagonal positions
                x, y = -4, -4
                while x <= 4:  # BL to UR
                    new_move = [pos[0] + y, pos[1] + x]
                    if new_move not in move_list and new_move not in stone_pos:
                        if 0 <= new_move[0] <= 14 and 0 <= new_move[1] <= 14:
                            move_list.append(new_move)
                    y += 1
                    x += 1
                x, y = -4, 4
                while x <= 4:  # UL to BR
                    new_move = [pos[0] + y, pos[1] + x]
                    if new_move not in move_list and new_move not in stone_pos:
                        if 0 <= new_move[0] <= 14 and 0 <= new_move[1] <= 14:
                            move_list.append(new_move)
                    y -= 1
                    x += 1

            return move_list

        def parse_subtree(self, pos, parent, cur_depth, board):
            """
            Builds the subtree for a given parent node, recursive
            :param pos: the last move of the parent node
            :param parent: the root of this subtree
            :param cur_depth: the tree depth this current iteration is on
            :param board: The current playing board configuration for the node
            :return: 0 once recursion on a branch has ended
            """
            # If backtracking, reset duplicate list
            if self.last_depth > cur_depth:
                if cur_depth is 3:
                    self.lvthree_dup = []
            self.last_depth = cur_depth

            # Root = depth 1, so starting at depth = 2:
            new_board = []
            for row in board:
                new_board.append(copy.copy(row))

            # Create and hookup new node
            new_node = GameNode(pos, 0, parent)
            parent.children.append(new_node)  # Append node to parent's children

            # Look at correct duplicate node list
            if cur_depth is 2:
                dup_list = self.lvtwo_dup
            else:
                dup_list = self.lvthree_dup

            # Recursively create children
            if cur_depth <= MAX_DEPTH and [pos, cur_depth] not in dup_list:
                dup_list.append([pos, cur_depth])  # Add entry to dup list
                if cur_depth % 2 == 0:  # If even, is our future move
                    new_board[pos[0]][pos[1]] = 1
                else:  # Otherwise, is opponent's future move
                    new_board[pos[0]][pos[1]] = 2
                new_data_list = self.list_moves(new_board)
                for element in new_data_list:
                    print("Making child node of " + str(pos[0])+", " + str(pos[1]) +
                          " at depth " + str(cur_depth) + ": " + str(element[0]) + ", " + str(element[1]))
                    self.parse_subtree(element, new_node, cur_depth+1, new_board)
            else:
                return 0  # Reached lowest depth


# Class for minimax
class MiniMax:
    def __init__(self, game_tree):
        """
        MiniMax takes a game tree (defined above)
        :param game_tree: the game tree to run the algorithm on
        """
        self.game_tree = game_tree
        self.root = game_tree.root  # the root of the tree
        self.currentNode = None  # we are not currently looking at any node
        self.successors = []  # an empty array of the game nodes that succeed the current node
        return

    def get_successors(self, node):
        """
        Return the successors of a node
        :param node: the node to get the successors of
        :return: the successors
        """
        return node.children

    def isTerminal(self, node):
        """
        Returns whether-or-not the node is a terminal node (has no chilren)
        :param node: the node
        :return: is it terminal?
        """
        if len(node.children) == 0:
            return True
        return False

    def getUtility(self, node):
        """
        Returns the value of the utility function for the given node
        TODO: Make this not just return the value
        :param node: the node
        :return: the utility value
        """
        return node.value

    def run_minimax(self, node):
        """
        Runs the minimax algorithm
        :param node: the root node
        :return: the best move
        """
        # set the current best val to the max value of the root node
        best = self.max_value(node)

        # which node has that max value?
        successors = self.get_sucessors(node)  # get a list of the successors to the current root
        print("MiniMax: Utility Value of Root Node: " + str(best))

        # find the node that has this best move
        best_move = None
        for element in successors:
            if element.value == best:
                best_move = element  # this element has the best value, therefore its the best one
                break

        return best_move

    def max_value(self, node):
        """
        Returns the max value from a given node
        :param node: the node to run this on
        :return: the max value
        """
        if self.isTerminal(node):  # if this is a terminal node...
            return self.getUtility(node)  # return the utility value of the node

        max_value = -float('inf')  # default the max value to negative infinity (we can only go up)
        the_successors = self.get_successors(node)  # get successors of this node
        for successor in the_successors:
            max_value = max(max_value, self.min_value(successor))
        return max_value

    def min_value(self, node):
        """
        Returns the min value from a given node
        :param node: the node to run this on
        :return: the min value
        """
        if self.isTerminal(node):  # if this is a terminal node...
            return self.getUtility(node)  # return the utility value of the node

        min_value = float('inf')  # default the min value to infinity (we can only go down
        the_successors = self.get_successors(node)  # get successors of this node
        for successor in the_successors:
            min_value = min(min_value, self.max_value(successor))
        return min_value


# Class for File I/O, also calculates first move
class FileIO:
    def __init__(self):
        self.is_end = False  # Not end of game by default
        self.our_turn = False  # Not our turn by default

    def parse_column(self, column):
        """
        Maps column letter to number, column number to letter
        :param column: the column letter or number to map
        :return: the corresponding number or letter
        """
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

    def check_files(self):
        """
        Reads move_file if our turn, checks for end of game
        :return: -1 = Not our turn nor end of game, 0 = our turn and not end of game, 1 = end of game
        """
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
            if new_play[0] is not "":  # Case where it is our turn first
                if new_play[0] == "gomokuguy":  # Case where other ai is still doing turn
                    return -1  # Not our turn
                cur_board[int(new_play[2]) - 1][self.parse_column(new_play[1])] = 2
            return 0  # Success
        return -1  # Not our turn

    def check_first(self):
        """
        Checks if it our first move, find initial placement if it is
        :return: array of position to place stone at, 0 if it is not our first move
        """
        is_empty = True
        num_stones = 0
        enemy_pos = [0, 0]
        i, j = 0, 0

        for row in cur_board:  # Check if board is empty or has only one stone
            for element in row:
                if element is not 0:
                    is_empty = False
                    num_stones += 1
                    enemy_pos[0], enemy_pos[1] = j, i  # Used if only one stone on the board
                j += 1
            i += 1
            j = 0

        if is_empty:  # It is our turn first
            return [3, 3]  # Return array of stone position
        elif not is_empty and num_stones is 1:  # It is our first move, enemy had first turn
            our_x, our_y = 0, 0

            # For enemy placement in corners, place our stone diagonally across from theirs
            print(enemy_pos)
            if enemy_pos[X] <= 3 and enemy_pos[Y] <= 3:  # Enemy placement in UL corner
                our_x, our_y = enemy_pos[X] + 1, enemy_pos[Y] + 1
            elif enemy_pos[X] >= 11 and enemy_pos[Y] <= 3:  # Enemy placement in UR corner
                our_x, our_y = enemy_pos[X] - 1, enemy_pos[Y] + 1
            elif enemy_pos[X] <= 3 and enemy_pos[Y] >= 11:  # Enemy placement in LL corner
                our_x, our_y = enemy_pos[X] + 1, enemy_pos[Y] - 1
            elif enemy_pos[X] >= 11 and enemy_pos[Y] >= 11:  # Enemy placement in LR corner
                our_x, our_y = enemy_pos[X] + 1, enemy_pos[Y] + 1

            # For enemy placement near a side, place our stone horizontally/vertically across from theirs
            elif enemy_pos[X] <= 3 and enemy_pos[Y] > 3 and enemy_pos[Y] < 11:  # Enemy placement on Left
                our_x, our_y = enemy_pos[X] + 1, enemy_pos[Y]
            elif enemy_pos[X] >= 11 and enemy_pos[Y] > 3 and enemy_pos[Y] < 11:  # Enemy placement on Right
                our_x, our_y = enemy_pos[X] - 1, enemy_pos[Y]
            elif enemy_pos[X] > 3 and enemy_pos[X] < 11 and enemy_pos[Y] <= 3:  # Enemy placement on Top
                our_x, our_y = enemy_pos[X], enemy_pos[Y] + 1
            elif enemy_pos[X] > 3 and enemy_pos[X] < 11 and enemy_pos[Y] >= 11:  # Enemy placement on Bottom
                our_x, our_y = enemy_pos[X], enemy_pos[Y] - 1

            else: # Otherwise, replace enemy stone
                our_x, our_y = enemy_pos[X], enemy_pos[Y]
            return [our_x, our_y]  # Return array of stone position
        else:
            return 0  # It is not the first turn

        # TODO: This logic is very basic right now, maybe incorporate the heuristics in later

    def write_turn(self, column, row):
        """
        Updates move file with our move
        :param column: the column index of our move
        :param row: the row index of our move
        :return: 0 if executed successfully
        """
        cur_board[row][column] = 1  # Put our move on our board

        # Write to move_file
        f = open("move_file.txt", "w")
        f.write("gomokuguy " + self.parse_column(column) + " " + str(row + 1))
        f.close()
        return 0  # Executed successfully

    def print_board(self):
        """
        Prints out board array in readable format
        :return: 0 if executed successfully
        """
        for row in cur_board:
            print(row)
        return 0  # Printed successfully


# Runs the main program
def main():
    is_end = False
    our_turn = False
    move_x, move_y = 0, 0
    io = FileIO()  # File input/output object
    dt = DecisionTree()  # Decision tree object

    while not is_end:
        print("Waiting for our turn...")
        while not our_turn:  # Wait for our turn
            file_output = io.check_files()
            if file_output == -1:
                sleep(0.1)  # (in seconds)
            if file_output == 0:
                our_turn = True
            if file_output == 1:
                is_end = True

        # Calculations for turn go here
        if not is_end:
            first_move = io.check_first()
            if first_move is not 0:
                move_x, move_y = first_move[X], first_move[Y]
            # If not the first move, build tree and use minimax algorithm
            # else:
            dt.build_tree()

        if not is_end:
            io.write_turn(move_x, move_y)
            io.print_board()

        is_end = True  # Temp


# Receives:
    # Board of any Size
    # Value(Side 1 or 2) to find the heuristic value of
# Returns:
    # Heuristic Value
def get_heuristic(board, value):
    heuristic_value = get_horizontal_heuristic(board,value) + get_vertical_heuristic(board, value) + \
                      get_lr_diagonal_heuristic(board, value) + get_rl_diagonal_heuristic(board, value)
    return heuristic_value;


# Helper Function of get_heuristic
def get_horizontal_heuristic(board, value):
    heuristic_value = 0
    for row in board:
        for start in range(0, len(row)- 5):
            friendly_count = 0
            enemy_count = 0
            for i in range(5):
                if row[start + i] == value:
                    friendly_count += 1
                else:
                    enemy_count += 1
            if friendly_count > enemy_count:
                heuristic_value += 1
            else:
                heuristic_value -= 1
    return heuristic_value


# Helper Function of get_heuristic
def get_vertical_heuristic(board, value):
    heuristic_value = 0
    rows = len(board)
    columns = len(board[0])
    for x in range(columns - 5):
        for y in range(rows):
            friendly_count = 0
            enemy_count = 0
            for i in range(5):
                if board[y + i][x] == value:
                    friendly_count += 1
                else:
                    enemy_count += 1
            if friendly_count > enemy_count:
                heuristic_value += 1
            else:
                heuristic_value -= 1
    return heuristic_value


# Helper Function of get_heuristic
def get_lr_diagonal_heuristic(board, value):
    heuristic_value = 0
    rows = len(board)
    columns = len(board[0])

    for y in range(columns - 4):
        x = 0
        diagonal_length = columns - y
        for i in range(diagonal_length - 5):
            friendly_count = 0
            enemy_count = 0
            for j in range(5):
                if board[y + i + j][x + i + j] == value:
                    friendly_count += 1
                else:
                    enemy_count += 1
            if friendly_count > enemy_count:
                heuristic_value += 1
            else:
                heuristic_value -= 1

    for x in range(columns - 4 - 1):
        x += 1
        y = 0
        diagonal_length = rows - x
        for i in range(diagonal_length - 5):
            friendly_count = 0
            enemy_count = 0
            for j in range(5):
                if board[y + i + j][x + i + j] == value:
                    friendly_count += 1
                else:
                    enemy_count += 1
            if friendly_count > enemy_count:
                heuristic_value += 1
            else:
                heuristic_value -= 1

    return heuristic_value


# Helper Function of get_heuristic
def get_rl_diagonal_heuristic(board, value):
    heuristic_value = 0
    rows = len(board)
    columns = len(board[0])

    for y in range(columns - 4):
        x = rows - 1
        diagonal_length = columns - y
        for i in range(diagonal_length - 5):
            friendly_count = 0
            enemy_count = 0
            for j in range(5):
                if board[y - i - j][x - i - j] == value:
                    friendly_count += 1
                else:
                    enemy_count += 1
            if friendly_count > enemy_count:
                heuristic_value += 1
            else:
                heuristic_value -= 1

    for x in range(columns - 4 - 1):
        x -= 1
        y = columns - 1
        diagonal_length = rows - x
        for i in range(diagonal_length - 5):
            friendly_count = 0
            enemy_count = 0
            for j in range(5):
                if board[y + i + j][x + i + j] == value:
                    friendly_count += 1
                else:
                    enemy_count += 1
            if friendly_count > enemy_count:
                heuristic_value += 1
            else:
                heuristic_value -= 1

    return heuristic_value


# Receives:
    # Board of any Size
    # Board from Previous Move of Same Size
# Only performs heuristic calculations on possibly affected areas
# Returns:
    # Heuristic Value
def get_heuristic_optimized(board, value, previous_board):
    #Not implemented

    return 0

#Turn
# - Check if Turn can be Won (Net sum of 5 area is 4) (Friendly)
# - Check if Oppenent can Win/Block (Net sum of 5 area is 4) (Oppenent)
# - Mini-max of Heuristic

main()

