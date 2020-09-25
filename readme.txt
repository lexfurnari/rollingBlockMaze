// Project 1 (blockmaze.py) - readme.txt //  - Alexa Furnari, Tim Wu, Bridget Murphy

To run the program blockmaze.py, the command line argument should include the name of the maze file as well as a choice of heuristic. To use the trivial heuristic where h(n) = 0, the user should input “0” as the second command line argument. To use the Scaled Manhattan Distance heuristic, the user should input “1” as the second command line argument. 

For example, to use the Scaled Manhattan Distance heuristic on Maze 3, the user should input the following:
python3 blockmaze.py maze3 1

The program will print out a map of the maze, as well as the path that the block should take to reach the goal in the form of a list of coordinates. It will also print out the length of this path, the amount of nodes generated, and the amount of nodes visited. If there is no path from start to goal, the program will print a message saying so. 


