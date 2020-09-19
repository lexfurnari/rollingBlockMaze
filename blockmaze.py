import sys
from collections import deque

# Usage of deque:
#   q = deque()   # declare new deque
#   q.append('A') # append A to the rear of the queue.
#   q.popleft()   # pop from the front of the queue.

class Node:
    def __init__(self, x, y, state, parent):
        self.state = state
        self.parent = parent
        self.location = (x,y)                        #location tuple
        self.g = 0
        self.h = 0
        self.f = 0


    # Nodes with the same state are viewed as equal
    def __eq__(self, other_node):
        return isinstance(other_node, Node) and self.state == other_node.state

    # Nodes with the same state hash to the same value
    # (e.g., when storing them in a set or dictionary)
    def __hash__(self):
        return hash(self.state)

    # Evaluate true cost from block to the goal
    def __evaluateTrueCost__ (self):
        # true_cost = (the absolute value of the x location of block - the x location 
        # of the goal) + (the absolute value of the y location of the block - the y location of the goal)
        return #(abs((self.location[0] - ) + abs(self.location[1] - )


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


#A* search
def aStar(gn, hn, start, goal):
    frontier =  list()
    explored = list()
    fn = gn + hn
    s = Node(fn, None)
    frontier.append(s)
    while frontier:
        frontier.sort()
        x = frontier.pop(0)
        if (x.state is goal):
            return x.state
        explored.append(x.state)
        for i in range(hn):
            child = Node(fn,x)
            if child.state not in explored and child not in frontier:
                frontier.append(child)
            elif child in frontier:
                frontier.append(child)


    
#retrieves maze file from command line argument
mazeNum = sys.argv[1]

def main():
    fileCounter = 0
    movCounter = 0
    blockState = True
    position = None
    start = 0
    x = list()
    y = list()
    print(mazeNum)
    maze = open(mazeNum + ".txt", "r")
    print(maze.read())                          #prints full map of maze
    maze = open(mazeNum + ".txt", "r")
    mazeLines = maze.readlines()                #creates 2D array of maze
    print(mazeLines)
    maze = open(mazeNum + ".txt", "r")
    for i in maze.read():                       #locates start position "S"
        fileCounter = fileCounter + 1
        if "S" in i:                            
            print(fileCounter)
    
    #TEST CODE
    print(mazeLines[0][0])                      #prints "S" for maze1
    print(mazeLines[6][6])                      #prints "G" for maze2

    #TEST EVALUATE
    #newNode = Node(0,0,None,None)
    #cost = newNode.evaluateTrueCost()

    maze.close

    

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