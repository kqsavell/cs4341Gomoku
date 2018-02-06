GomokuGuy Python Script

GROUP MEMBERS
Kyle Savell // Henry Wheeler-Mackta // Richard Valente

INSTRUCTIONS ON COMPILING / RUNNING
Assuming this is being run on a Windows machine...
It can be run like any other .py script:
	In the windows cmd, run the computer's python.exe's full path followed by the full path of the python script (gomokuguy.py)
	It'll look something like: C:\Python27\python.exe C:\Username\Desktop\gomokuguy.py

HEURISTICS / STRATEGIES
The program primarily uses a heuristic based on the presence of "windows" of 5 possible friendly / enemy stones. That is, it will check 
for whether-or-not there are 5 spaces where friendly stones could be placed such to score a win. It scores a given board state based on
how many of these windows exist and how many of them are already partially filled with friendly stones. Likewise, the heuristic will give
high score to moves that will block enemy windows. 

In addition, the program builds its decision tree dynamically rather than constructing it out of all possible moves / future results. Each 
node of the tree is built such that the newly added stone is within 5 places of the last placed stone. Like many grid-based games, gomoku games 
will often see their stone placements "fan out" from each previously placed node. Thus, it was assumed that the predictions will not need to consider
moves made that are far away from previously placed nodes

UTILITY FUNCTION
At a given terminal state, the utility function runs the primary heuristic and returns the heuristic score. The minimax algorithm 
will then use those heuristic scores for its values.


EVALUATION FUNCTION
At any given state, the evaluation function runs the primary heuristic and returns the heuristic score. 


RESULTS



JUSTIFICATION FOR EVALUATION FUNCTIONS / HEURISTICS