import sys
import heapq
from collections import deque

# Usage of deque:
#   q = deque()   # declare new deque
#   q.append('A') # append A to the rear of the queue.
#   q.popleft()   # pop from the front of the queue.

'''
frontier = []
heapq.heappush(frontier,'A')
heapq.heappush(frontier,'B')
print(heapq.heappop(frontier))
'''

class Node:
    def __init__(self, x, y, state, parent):
        self.state = state
        self.parent = parent
<<<<<<< HEAD
        self.g = 0                                   # true cost
        self.h = 0                                   # estimated cost 
        self.f = self.g + self.h                     # f = g + h    
=======
        self.location = x, y                        # location tuple
        self.g = 0                                   # true cost
        self.h = 0                                   # estimated cost 
        self.fcost = 0                               # f = g + h
>>>>>>> c7dfc9e2c723ba6cd75627b2707cdd054e02a3c3


    # Nodes with the same state are viewed as equal
    def __eq__(self, other_node):
        return isinstance(other_node, Node) and self.state == other_node.state

    def __less_than__(self, other_node):
        return self.fcost < other_node.fcost         # fcost tells you which one to take off the queue 

    def __more_than__(self, other_node):
<<<<<<< HEAD
        return self.fcost > other_node.fcost
=======
        return self.fcost > othernode.fcost
>>>>>>> c7dfc9e2c723ba6cd75627b2707cdd054e02a3c3



    # Nodes with the same state hash to the same value
    # (e.g., when storing them in a set or dictionary)
    def __hash__(self):
        return hash(self.state)

    # Evaluates the number of blocks away from the goal
    def __moves_from_goal__ (self):
        # true_cost = (the absolute value of the x location of block - the x location 
        # of the goal) + (the absolute value of the y location of the block - the y location of the goal)
        return (abs(self.location[0] - locationG[0]) + abs(self.location[1] - locationG[1]))
<<<<<<< HEAD
=======


#TEST CODE
def up(state, location):
    if state is True:
        state = False
    return
def down(state, location):
    if state is True:
        state = False
    return
def left(state, location):
    if state is True:
        state = False
    return
def right(state, location):
    if state is True:
        state = False
    return
def goalCheck(state, location):
    if state is True and location is "G":
        return
def check_state(state):
    if state is True:
        standing = True
        return standing
    else:
        standing = False
        return standing
>>>>>>> c7dfc9e2c723ba6cd75627b2707cdd054e02a3c3

'''
frontier = []
heapq.heappush(frontier,'A')
heapq.heappush(frontier,'B')
print(heapq.heappop(frontier))
'''

#A* search
def aStar(start, goal):
    frontier = []
    explored = list()
<<<<<<< HEAD
    s = Node(start, None)
    heapq.heappush(frontier, s)
=======
    fn = gn + hn
    s = Node(locationS[0], locationS[1], fn, None)
    frontier.append(s)
>>>>>>> c7dfc9e2c723ba6cd75627b2707cdd054e02a3c3
    while frontier:
        parent = heapq.heappop(frontier)
        if (parent.state == goal):          #TEST: after first iteration, parent is a list and not a node
            return parent.state             #TEST: is state the solution? or is it just the node
        explored.append(parent.state)
        for i in range(3):                   #TEST: what is the range?
            for j in range(3):
                nextLocation = ([i],[j])
                child = Node(nextLocation, parent)
                if child.state not in explored and child not in frontier:
                    frontier.insert(0, frontier)        #how are we inserting into frontier?
                elif child.state in frontier and child.state > frontier[0]:
                    frontier.insert(0,child)                #is this correct?

    return None


    
#retrieves maze file from command line argument
mazeNum = sys.argv[1]

def main():
    fileCounter = 0
    movCounter = 0
    standing = True
    position = None
    locationS = None
    locationG = None
    x = list()
    y = list()
    print(mazeNum)
    maze = open(mazeNum + ".txt", "r")
    print(maze.read())                          #prints full map of maze
    maze = open(mazeNum + ".txt", "r")
    mazeLines = maze.readlines()                #creates 2D array of maze
    #print(mazeLines)
    maze = open(mazeNum + ".txt", "r")
    for i in range(len(mazeLines)):             #iterates through maze to find location of S and G
        for j in range(len(mazeLines)):
            fileCounter = fileCounter + 1
            if mazeLines[i][j] == "S":  
                locationS = i, j                  #start location storec as tuple
                print("S at: " + str(locationS))
            if mazeLines[i][j] == "G": 
                locationG = i, j                  #goal location stored as tuple
                print("G at: " + str(locationG))
<<<<<<< HEAD
            
        
    searching = aStar(locationS, locationG)
    
=======
    
    #TEST CODE
    print(mazeLines[0][0])                      #prints "S" for maze1
    print(mazeLines[6][6])                      #prints "G" for maze1
>>>>>>> c7dfc9e2c723ba6cd75627b2707cdd054e02a3c3

    #TEST EVALUATE
    #newNode = Node(0,0,None,None)
    #cost = newNode.moved_from_goal()

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
'''

'''
    if "S" in line:
        print("Check")
        if maze[i] == "S":
            start = i
            print(start)
            break
        '''

    


if __name__ == "__main__": 
    main()