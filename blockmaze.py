import sys
from collections import deque

# Usage of deque:
#   q = deque()   # declare new deque
#   q.append('A') # append A to the rear of the queue.
#   q.popleft()   # pop from the front of the queue.

class Node:
    def __init__(self, state, parent):
        self.state = state
        self.parent = parent

    # Nodes with the same state are viewed as equal
    def __eq__(self, other_node):
        return isinstance(other_node, Node) and self.state == other_node.state

    # Nodes with the same state hash to the same value
    # (e.g., when storing them in a set or dictionary)
    def __hash__(self):
        return hash(self.state)


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
    if state == True and location == "G":
        return
        
def check_state(state):
    if state is True:
        standing = True
        return standing
    else:
        standing = False
        return False

mazeNum = sys.argv[1]

def main():
    movCounter = 0
    blockState = True
    position = None
    start = 0
    print(mazeNum)
    maze = open(mazeNum + ".txt", "r")
    print(maze.read())
    lineNum = (maze.read())
    line = list(lineNum)
    print(line)
    for i in range(len(lineNum)):
        if lineNum[i] == "S":
            start = i
            print(start)
            break

    
    



if __name__ == "__main__": 
    main()