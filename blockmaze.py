import sys
import heapq

class Node:
    def __init__(self, block1, block2, parent, g, h):
        self.state = (block1,block2)
        self.block1 = block1
        self.block2 = block2
        self.parent = parent
        self.g = 0                                   # true cost
        self.h = 0                                   # estimated cost 
        self.f = self.g + self.h                     # f = g + h    


    # Nodes with the same state are viewed as equal
    def __eq__(self, other_node):
        return isinstance(other_node, Node) and self.state == other_node.state

    def __lt__(self, other_node):
        return self.f < other_node.f         # fcost tells you which one to take off the queue 

    def __more_than__(self, other_node):
        return self.f > other_node.fcost



    # Nodes with the same state hash to the same value
    # (e.g., when storing them in a set or dictionary)
    def __hash__(self):
        return hash(self.state)

    # Evaluates the number of blocks away from the goal
    def __moves_from_goal__ (self):
        # true_cost = (the absolute value of the x location of block - the x location 
        # of the goal) + (the absolute value of the y location of the block - the y location of the goal)
        return (abs(self.state[0] - goal[0]) + abs(self.state[1] - goal[1]))


def legal_actions(current, mazeLines, xMax, yMax): #take in current state of the block
    moves = []
    
    block1 = current.block1
    block2 = current.block2

    if current.block1 == current.block2:                                                                            #if block is standing

        if block1[0] > 2:    
            if (((mazeLines[block1[0]-1][block1[1]]) is ".") and ((mazeLines[block1[0]-2][block1[1]]) is ".")):     #checks up
                moves.append((block1[0]-1, block1[1]))
                moves.append((block1[0]-2, block1[1]))

        if block1[1] < yMax-2:
            if (((mazeLines[block1[0]][block1[1]+1]) is ".") and ((mazeLines[block1[0]][block1[1]+2]) is ".")):   #checks right
                moves.append((block1[0], block1[1]+1))
                moves.append((block1[0], block1[1]+2))

        if block1[0] < xMax-2:
            if (((mazeLines[block1[0]+1][block1[1]]) is ".") and ((mazeLines[block1[0]+2][block1[1]]) is '.')):     #checks down
                moves.append((block1[0]+1, block1[1]))
                moves.append((block1[0]+2, block1[1]))

        if block1[1] > 2:
            if (((mazeLines[block1[0]][block1[1]-1]) is ".") and ((mazeLines[block1[0]][block1[1]-2]) is ".")):     #checks left
                moves.append((block1[0], block1[1]-1))
                moves.append((block1[0], block1[1]-2))

    elif current.block1[0] == current.block2[0]:                                                                    #if laying horizontally (x's are the same)

        if block2[1] > 0:
            if (((mazeLines[block1[0]-1][block1[1]]) is ".") and ((mazeLines[block2[0]-1][block2[1]]) is ".")):     #checks up
                moves.append((block1[0]-1, block1[1]))
                moves.append((block2[0]-1, block2[1]))

        if block2[0] < xMax-1:
            if (((mazeLines[block2[0]][block2[1]+1]) is "G") or ((mazeLines[block2[0]][block2[1]+1]) is ".")):      #checks right
                moves.append((block2[0], block2[1]+1))
                moves.append((block2[0], block2[1]+1))

        if block2[1] < yMax-1:
            if (((mazeLines[block1[0]+1][block1[1]]) is ".") and ((mazeLines[block2[0]][block2[1]+1]) is ".")):     #checks down
                moves.append((block1[0]+1, block1[1]))
                moves.append((block2[0]+1, block2[1]))

        if block1[0] > 0:
            if (((mazeLines[block1[0]][block1[1]-1]) is "G") or ((mazeLines[block1[0]][block1[1]-1]) is ".")):      #checks left
                moves.append((block1[0], block1[1]-1))
                moves.append((block1[0], block1[1]-1))
    
            
    elif current.block1[1] == current.block2[1]:                                                                    #if laying vertically (y's are the same)

        if block1[0] > 0:
            if (((mazeLines[block1[0]-1][block1[1]]) is "G") or ((mazeLines[block1[0]-1][block1[1]]) is ".")):      #checks up
                moves.append((block1[0]-1, block1[1]))
                moves.append((block1[0]-1, block1[1]))

        if block2[1] < yMax-1:
            if (((mazeLines[block1[0]][block1[1]+1]) is ".") and ((mazeLines[block2[0]][block2[1]+1]) is ".")):     #checks right
                moves.append((block1[0], block1[1]+1))
                moves.append((block2[0], block2[1]+1))

        if block2[0] < xMax-1:
            if (((mazeLines[block2[0]+1][block2[1]]) is "G") or ((mazeLines[block2[0]+1][block2[1]]) is ".")):      #checks down
                moves.append((block2[0]+1, block2[1]))
                moves.append((block2[0]+1, block2[1]))
        
        if block1[1] > 0:
            if (((mazeLines[block1[0]][block1[1]-1]) is ".") and ((mazeLines[block2[0]][block2[1]-1]) is ".")):     #checks left
                moves.append((block1[0], block1[1]-1))
                moves.append((block2[0], block2[1]-1))

    return moves




#A* search
def aStar(start, goal, mazeLines, xMax, yMax):
    frontier = list()
    explored = list()
    g = 0
    s = Node(start, start, None, g, 0)
    frontier.append(s)
    while frontier is not None:
        heapq.heapify(frontier)
        parent = heapq.heappop(frontier) 
        explored.append(parent.state)
        if (parent.state == (goal,goal)):
            print("GOAL")
            return parent.state                         #TEST: We want a path once the solution is found
        #print(parent.state)
        moveList = legal_actions(parent, mazeLines, xMax, yMax)
        for i in (range(len(moveList))):
            #if i%2 == 1:
            #    continue
            print(moveList)
            child = Node(moveList[0], moveList[1], parent, g+1, 0) # h is zero for now, make heuristic later
            #print(child.state)
            if child not in frontier and child.state not in explored:
                #frontier.append(child)
                heapq.heappush(frontier,child)            # use heappush instead of insert push maintaince heap in variant. 
            #elif child in frontier:
            #elif child.state in frontier and child.state > frontier[0]:
            else:
                heapq.heapreplace(frontier,child)
                #frontier.insert(0,child)               #is this correct?
                #frontier.append(child)

    return None


    
#retrieves maze file from command line argument
mazeNum = sys.argv[1]

def main():
    fileCounter = 0
    start = None
    goal = None
    xMax = 0
    yMax = 0
    print(mazeNum)
    maze = open(mazeNum + ".txt", "r")
    print(maze.read())                          #prints full map of maze
    maze = open(mazeNum + ".txt", "r")
    mazeLines = maze.readlines()                #creates 2D array of maze
    #print(mazeLines)
    maze = open(mazeNum + ".txt", "r")
    for i in range(len(mazeLines)):             #iterates through maze to find location of S and G
        xMax = xMax+1
        for j in range(len(mazeLines)):
            yMax = yMax + 1
            fileCounter = fileCounter + 1
            if mazeLines[i][j] == "S":  
                start = i, j                  #start location storec as tuple
                print("S at: " + str(start))
            if mazeLines[i][j] == "G": 
                goal = i, j                  #goal location stored as tuple
                print("G at: " + str(goal))

    yMax = yMax//xMax

    aStar(start, goal, mazeLines, xMax, yMax)

    '''
    #block1 = n.loc1
    if (mazeLines[1][0] == ".") and (mazeLines[2][0] == '.'):
        mazeLines[1][0].insert(1,"1")
        mazeLines[2][0].insert(2,"1")
    #maze = open(mazeNum + ".txt", "w")
    print(mazeLines)  
    #standing(n)       
    '''

    maze.close

'''
what to store in node
   present
   cost to goal
   h-cost
   f-cost
If wanna use list class, must use >, < for node class
to find fn of child, take gn of parent plus hn of child
for an admissible heuristic, hn =< h*n
   where h*n = true cost to goal
Use sm similar to manhattan distance
keep in mind oreintation of block
use of tuples?
Use two sets of coordinates to determine if standing or laying down
Go through all the actions and make a child
    g cost is number of moves, so g = g+1
    Or to optimize, lie down as least often as possible
#1 Goal: make action for function
    put it instead of for i in range; for j in range
    need function that returns all possible moves
    need function: if standing, change coordinates; else ...
#2 Goal: once action is working, then A*
#3 Goal: then work with heuristics
    first use 0 for heuristic to check if it works, then try more

Test: build a new smaller maze to test
'''

if __name__ == "__main__": 
    main()
