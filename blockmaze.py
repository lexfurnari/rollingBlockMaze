import sys
import heapq

class Node:
    def __init__(self, block1, block2, parent, g, h, goal):
        self.state = (block1,block2)
        self.block1 = block1
        self.block2 = block2
        self.parent = parent
        self.h = 0
        self.g = g                                              # true cost
        if h == 1:
            self.h = manhattan_distance(self.block1, goal)      # estimated cost 
            self.f = self.g + self.h                            # f = g + h
        else:
            self.f = self.g


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
def manhattan_distance(current, goal):
    # true_cost = (the absolute value of the x location of block - the x location
    # of the goal) + (the absolute value of the y location of the block - the y location of the goal)
    return ((abs(current[0] - goal[0]) + (abs(current[1] - goal[1]))/(2)))


def legal_actions(current, mazeLines, xMax, yMax): #take in current state of the block, array of the maze, and the edges of the maze
    moves = []

    block1 = current.block1
    block2 = current.block2


    if current.block1 == current.block2:                                                                                #if block is standing
        if block1[0] > 1:    
            if ((mazeLines[block1[0]-1][block1[1]]) is not "*" and (mazeLines[block1[0]-2][block1[1]]) is not "*"):     #checks up
                moves.append((block1[0]-1, block1[1]))
                moves.append((block1[0]-2, block1[1]))

        if block1[1] < yMax-2:
            if ((mazeLines[block1[0]][block1[1]+1]) is not "*" and (mazeLines[block1[0]][block1[1]+2]) is not "*"):     #checks right
                moves.append((block1[0], block1[1]+1))
                moves.append((block1[0], block1[1]+2))

        if block1[0] < xMax-2:
            if ((mazeLines[block1[0]+1][block1[1]]) is not "*" and (mazeLines[block1[0]+2][block1[1]]) is not "*"):     #checks down
                moves.append((block1[0]+1, block1[1]))
                moves.append((block1[0]+2, block1[1]))

        if block1[1] > 1:
            if ((mazeLines[block1[0]][block1[1]-1]) is not "*" and (mazeLines[block1[0]][block1[1]-2]) is not "*"):     #checks left
                moves.append((block1[0], block1[1]-1))
                moves.append((block1[0], block1[1]-2))


    elif current.block1[0] == current.block2[0]:                                                                        #if laying horizontally (x's are the same)

        if block1[0] > 0 and block2[0] > 0:                                                                             #checks up
            if ((mazeLines[block1[0]-1][block1[1]]) is not "*" and (mazeLines[block2[0]-1][block2[1]]) is not "*"): 
                moves.append((block1[0]-1, block1[1]))
                moves.append((block2[0]-1, block2[1]))

        if block1[1] < yMax-1 and block2[1] < yMax-1:                                                                   #checks right
            if block1[1] > block2[1]:                                                                                   #checks for furthest right block
                if ((mazeLines[block1[0]][block1[1]+1]) is not "*"):
                    moves.append((block1[0], block1[1]+1))
                    moves.append((block1[0], block1[1]+1))
            elif block2[1] > block1[1]:
                if ((mazeLines[block2[0]][block2[1]+1]) is not "*"):                                                       
                    moves.append((block2[0], block2[1]+1))
                    moves.append((block2[0], block2[1]+1))


        if block1[0] < xMax-1 and block2[0] < xMax-1:
            if ((mazeLines[block1[0]+1][block1[1]]) is not "*" and (mazeLines[block2[0]+1][block2[1]]) is not "*"):     #checks down
                moves.append((block1[0]+1, block1[1]))
                moves.append((block2[0]+1, block2[1]))

        if block1[1] > 0 and block2[1] > 0:                                                                             #checks left
            if block1[1] < block2[1]:                                                                                   #checks for furthest left piece
                if ((mazeLines[block1[0]][block1[1]-1]) is not "*"):                    
                    moves.append((block1[0], block1[1]-1))
                    moves.append((block1[0], block1[1]-1))
            elif block2[1] < block1[1]:
                if ((mazeLines[block2[0]][block2[1]-1]) is not "*"): 
                    moves.append((block2[0], block2[1]-1))
                    moves.append((block2[0], block2[1]-1))
 
            
    elif current.block1[1] == current.block2[1]:                                                                        #if laying vertically (y's are the same)

        if block1[0] > 0 and block2[0] > 0:                                                                             #checks up
            if(block2[0] > block1[0]):                                                                                  #checks for highest block piece
                if ((mazeLines[block1[0]-1][block1[1]]) is not "*"):    
                    moves.append((block1[0]-1, block1[1]))
                    moves.append((block1[0]-1, block1[1]))
            elif(block1[0] > block2[0]):
                if ((mazeLines[block2[0]-1][block2[1]]) is not "*"):
                    moves.append((block2[0]-1, block2[1]))
                    moves.append((block2[0]-1, block2[1]))

        if block1[1] < yMax-1 and block2[1] < yMax-1:                                                                   #checks right
            if ((mazeLines[block1[0]][block1[1]+1]) is not "*" and (mazeLines[block2[0]][block2[1]+1]) is not "*"):    
                moves.append((block1[0], block1[1]+1))
                moves.append((block2[0], block2[1]+1))

        if block1[0] < xMax-1 and block2[0] < xMax-1:                                                                    #checks down
            if(block2[0] < block1[0]):                                                                                   #checks for lowest block piece
                if ((mazeLines[block2[0]+1][block2[1]]) is not "*"):   
                    moves.append((block2[0]+1, block2[1]))
                    moves.append((block2[0]+1, block2[1]))
            elif(block1[0] < block2[0]):
                if ((mazeLines[block1[0]+1][block1[1]]) is not "*"):
                    moves.append((block1[0]+1, block1[1]))
                    moves.append((block1[0]+1, block1[1]))
        
        if block1[1] > 0 and block2[1] > 0:                                                                             #checks left
            if ((mazeLines[block1[0]][block1[1]-1]) is not "*" and (mazeLines[block2[0]][block2[1]-1]) is not "*"): 
                moves.append((block1[0], block1[1]-1))
                moves.append((block2[0], block2[1]-1))

    return moves


#A* search
def aStar(start, goal, mazeLines, xMax, yMax, heur):
    frontier = list()
    explored = list()
    pathList = list()
    pathCount = 0
    nodeCount = 0
    nodeVisit = 0
    h = int(heur)
    s = Node(start, start, None, 0, h, goal)
    frontier.append(s)
    while frontier:
        heapq.heapify(frontier)
        parent = heapq.heappop(frontier) 
        nodeVisit = nodeVisit+1
        explored.append(parent.state)

        if (parent.state == (goal,goal)):
            print("Path Found!")
            while parent is not None:                           #while Node is not empty
                pathList.append(parent.state)                   #append to path list from bottom up
                parent = parent.parent                          #move current Node to parent Node
                pathCount = pathCount + 1
            pathList.reverse()                                  #reorder pathList to correct order
            print(pathList)
            print("Path length: " + str(pathCount))
            print("Nodes generated: " + str(nodeCount))
            print("Nodes visted: " + str(nodeVisit))
            return pathList

        moveList = legal_actions(parent, mazeLines, xMax, yMax)
        for i in (range(len(moveList))):
            if i%2 == 1:                                        #we want every other i because we send moveList[i] and moveList[i+1]
                continue
            child = Node(moveList[i], moveList[i+1], parent, parent.g+1, h, goal)

            if child not in frontier and child.state not in explored:
                heapq.heappush(frontier,child)
                nodeCount = nodeCount+1

            elif child in frontier:
                tempNode = frontier.pop()
                if(child.f < tempNode.f):
                    heapq.heapify(frontier)
                    heapq.heappush(frontier,child)
                else:
                    frontier.append(tempNode)

    return None

    
#retrieves maze file from command line argument
mazeNum = sys.argv[1]
heur = sys.argv[2]

def main():
    xMax = 0
    yMax = 0
    start = None
    goal = None
    print("Reading from file: " + str(mazeNum))
    maze = open(mazeNum + ".txt", "r")
    print(maze.read())                          #prints full map of maze
    maze = open(mazeNum + ".txt", "r")
    mazeLines = maze.readlines()                #creates 2D array of maze
    for i in range(len(mazeLines)):             #iterates through maze to find location of S and G
        xMax = xMax + 1
        for j in range(len(mazeLines)):
            yMax = yMax + 1
            if mazeLines[i][j] == "S":  
                start = (i, j)                   #start location storec as tuple
            elif mazeLines[i][j] == "G": 
                goal = (i, j)                    #goal location stored as tuple

    print("S at: " + str(start))
    print("G at: " + str(goal))
    yMax = yMax//xMax
    search = aStar(start, goal, mazeLines, xMax, yMax, heur)
    if (search == None):
        print("Sorry, path could not be found")
    
    maze.close

if __name__ == "__main__": 
    main()
