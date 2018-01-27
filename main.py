# Intro to AI Project 1: Gomoku
# Kyle Savell, Richard Valente, Henry Wheeler-Mackta

# Sample Board:
# 0 = Blank
# 1 = Player One Bead (White)
# 2 = Player Two Bead (Black)
# #         A    B    C    D    E    F    G    H    I    J    K    L    M    N    P
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

#             A    B    C    D    E    F    G    H    I    J    K    L    M    N    P
cur_board = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",  # 1
             " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",  # 2
             " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",  # 3
             " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",  # 4
             " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",  # 5
             " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",  # 6
             " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",  # 7
             " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",  # 8
             " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",  # 9
             " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",  # 10
             " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",  # 11
             " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",  # 12
             " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",  # 13
             " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",  # 14
             " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "]  # 15


# Class for Game Node, holds a board state
class GameNode:
    def __init__(self, move, value, parent):
        """
        Game Nodes contain a potential board state
        :param move: the move to make as a string(B5, A10, etc.)
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

        def build_tree(self, data_list):
            """
            Builds the tree from a given data list
            :param data_list: a list of all data, not sure what we want this to look like
            :return:
            """
            self.root = GameNode(data_list.pop(0))  # pop off the root game node, that's our root
            for element in data_list:
                self.parse_subtree(element, self.root)  # parse the subtree and hook it up to the root

        def parse_subtree(self, data_list, parent):
            """
            Builds the subtree for a given parent node, recursive
            :param data_list: the list of all data, data = board states?
            :param parent: the root of this subtree
            :return:
            """

            # TODO: how do we want to store/build the tree?


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
        print "MiniMax: Utility Value of Root Node: " + str(best)

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

def main():  # Runs the main program
    print(cur_board)


main()
