GomokuGuy Python Script

GROUP MEMBERS
Kyle Savell // Henry Wheeler-Mackta // Richard Valente

INSTRUCTIONS ON COMPILING / RUNNING
Assuming this is being run on a Windows machine...
It can be run like any other .py script, by double-clicking on the gomokuguy.py file on any computer w/ Python 2.7 installed.
NOTE: If the script is run from the command line, it can run into a crash related to file reading. This does not happen when the script
is run by double-clicking.

HEURISTICS / STRATEGIES
The program primarily uses a heuristic based on the presence of "windows" of 5 possible friendly / enemy stones. That is, it will check 
for whether-or-not there are 5 spaces where friendly stones could be placed such to score a win. It scores a given board state based on
how many of these windows exist and how many of them are already partially filled with friendly stones. Likewise, the heuristic will give
high score to moves that will block enemy windows. There are two versions of the heuristic calculation: 
 - A "non-optimized" version that analyzes every single location on the board. Function declaration is at [LINE NUMBER]
 - An "optimzed" version that only analyzes the board within a small radius around the last placed stone. Function declaration is at [LINE NUMBER]

In addition, the program builds its decision tree dynamically rather than constructing it out of all possible moves / future results. Each 
node of the tree is built such that the newly added stone is within 5 places of the last placed stone. Like many grid-based games, gomoku games 
will often see their stone placements "fan out" from each previously placed node. Thus, it was assumed that the predictions will not need to consider
moves made that are far away from previously placed nodes.

During decision tree generation, heuristics are applied to each node using either the "optimized" or "non-optimized" versions of the heuristic 
algorithm. Non-terminal leaves use the optimized versions whereas terminal leaves (leaves that are at depth 5), use the optimized-algorithm. 
Additionally, during decision tree generation, if the heuristic for a given node is close to 0, the tree will not generate any children for that given 
node. This is a sort of evaluation function for the given node, as children of a node with a heuristic close to 0 is extremely unlikely to be chosen. 
The check for this can be found at [LINE NUMBER].

There is an additional heuristic for detecting win conditions for either player such to take the appropriate action. For opponent plays, it analyzes the 
board for existing stone patterns that would lead to an enemy victory, and will bypass any heuristic checks such to place a stone that would block such
a victory. Likewise, if there are any friendly stone patterns that can be finished such to guarantee a friendly victory, the program will take that play
regardless of heuristic calculation. This winning_move function cna be found at [LINE NUMBER].

UTILITY FUNCTION
At a given terminal state, the utility function runs the primary heuristic and returns the heuristic score. The minimax algorithm 
will then use those heuristic scores for its values. The minimax algorithm calls for the heuristic at [LINE NUMBER]. 


EVALUATION FUNCTION
At any given state, the evaluation function runs the primary heuristic and returns the heuristic score. The decision tree generation calls for the 
heuristic at [LINE NUMBER]. 


RESULTS


