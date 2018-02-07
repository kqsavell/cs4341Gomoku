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
 - A "non-optimized" version that analyzes a sub-board surrounding placed stones on the board. Function declaration is at line #700.
 - An "optimized" version that only analyzes the board within a small radius around the last placed stone. Function declaration is at line #906.

In addition, the program builds its decision tree dynamically rather than constructing it out of all possible moves / future results. Each 
node of the tree is built such that the newly added stone is within 5 places of the last placed stone. Like many grid-based games, gomoku games 
will often see their stone placements "fan out" from each previously placed node. Thus, it was assumed that the predictions will not need to consider
moves made that are far away from previously placed nodes.

During decision tree generation, heuristics are applied to each node using either the "optimized" or "non-optimized" versions of the heuristic 
algorithm. Non-terminal leaves use the optimized versions whereas terminal leaves (leaves that are at depth 5), use the optimized-algorithm. 
Additionally, during decision tree generation, if the heuristic for a given node is close to 0, the tree will not generate any children for that given 
node. This is a sort of evaluation function for the given node, as children of a node with a heuristic close to 0 is extremely unlikely to be chosen. 
The check for this can be found at line #344.

There is an additional heuristic for detecting win conditions for either player such to take the appropriate action. For opponent plays, it analyzes the 
board for existing stone patterns that would lead to an enemy victory, and will bypass any heuristic checks such to place a stone that would block such
a victory. Likewise, if there are any friendly stone patterns that can be finished such to guarantee a friendly victory, the program will take that play
regardless of heuristic calculation. This winning_move function can be found at line #88.

UTILITY FUNCTION
At a given terminal state, the utility function runs the primary heuristic and returns the heuristic score. The minimax algorithm and non-terminal nodes for decision tree generation will then use those heuristic scores for its values. The minimax algorithm calls for the heuristic at line #426. 

EVALUATION FUNCTION
At any given state, the evaluation function runs the optimized heuristic and returns an estimated heuristic score. The decision tree generation calls for the heuristic at line #391, Which calls the function get_heuristic_optimized at line #906

TESTING
Many different methods were used for testing. We hard-coded in starting values to see how different games would play out. Specifically we tested starting positions near the edge of the board and near the middle, since the AI will replace the first stone if it is near the center, but otherwise play around the first stone if it is near the edge.

Additionally, we manually changed the move file so that we could play against the AI by manually inputting coordinates we wanted to place stones. Through this method we were able to test the AI to see if it blocked moves that we set up.

RESULTS
The AI plays very defensively. Unless there is a move that will guarantee a win, it will play around the enemy's stone placements. When it sees that the enemy has a winning move available, it will block it. One weakness is that the AI does not detect any "gotcha" scenarios where the enemy has set up multiple ways to win in their next move. Another negative is that it does not intentionally set up any of these types of winning moves unless the heuristic detects an optimal position in the right spot.

On the plus side, since the AI plays veyr defensively it will be impossible for the opponent to win unless one of these "gotcha" scenarios are set up by it. 

It was observed that the AI places stones in clusters (around surrounding stones) or in lines. This is likely due to how the heuristics are set up and how they but bigger value on lines of stones.


