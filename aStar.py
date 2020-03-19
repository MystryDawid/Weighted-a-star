from random import random
import math
import time as _time
from BinaryTree import TreeNode

class Node:
    def __init__(self, parent=None, position=None):     # constructor of objects
        self.parent = parent

        self.position = position

        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):    # function for comparing objects
        return self.position == other.position

    def __hash__(self):         # function for hashing objects
        return hash(self.position)

    def __sub__(self, other):   # function for subtractions objects
        return self.position - other.position


def astar(size, difficulty, e):
    start_time = _time.time()   # starting timer
    grid = size
    diff = difficulty / 100
    e = e/100
    n = grid * 2.5

    # creating a maze size x size
    maze = [[1 if random() < diff else 0 for x in range(grid)] for y in range(grid)]

    # making sure that start and goal are not wall
    maze[0][0] = 0
    maze[grid - 1][grid - 1] = 0

    # setting start and end node
    start_node = Node(None, (0, 0))
    end = Node(None, (grid - 1, grid - 1))

    o = []
    closed_set = TreeNode()

    # adding start node to open set and o
    open_set = TreeNode(start_node)
    o.append(start_node.position)

    while open_set.value:

        current_node = open_set.value_min_node()    # looking in open set for the closest node to the end

        if current_node.position == end.position:     # if path is founded

            path = [current_node.position]      # adding the start node position

            while current_node.parent:
                current_node = current_node.parent      # adding node position to the path
                path.append(current_node.position)      # changing node to previous one

            time = _time.time() - start_time    # stopping timer
            # returning revers path, maze and position of every node that was in open set and time
            return path[::-1], maze, o, time

        open_set.del_note(current_node)         # deleting closest node from open set
        closed_set.add_node(current_node)     # and adding it to the close set

        d = closed_set.value_min_node().g  # calculating d (depth of search)
        w = (0.4 + e - e * (d / n))     # calculating w (dynamic weight)
        # looking in neighbors for new nodes
        for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]:

            # creating a new position close to current node position
            position = current_node.position[0] + new_position[0], current_node.position[1] + new_position[1]

            # checking if position is walkable if not we skip one loop
            if position[0] > (len(maze) - 1) or\
                    position[0] < 0 or\
                    position[1] > (len(maze[len(maze) - 1]) - 1) or\
                    position[1] < 0 or\
                    maze[position[0]][position[1]] != 0:
                continue

            new_node = Node(current_node, position)  # creating a new node

            # calculating h
            new_node.h = math.sqrt((new_node.position[0] - end.position[0]) ** 2
                                   + (new_node.position[1] - end.position[1]) ** 2)

            if open_set.search(new_node):     # checking if node is in open_set, if is we skip one loop
                continue

            if closed_set.search(new_node):  # checking if node is in closet_set, if is we skip one loop
                continue

            # calculating g
            new_node.g = current_node.g + math.sqrt((new_node.position[0] - current_node.position[0]) ** 2
                                                    + (new_node.position[1] - current_node.position[1]) ** 2)

            # calculating f using dynamic weight
            new_node.f = new_node.g + w * new_node.h

            open_set.add_node(new_node)       # adding new node to open_set
            o.append(new_node.position)     # adding new nodes position to o

    time = _time.time() - start_time    # stopping timer
    return False, maze, o, time  # if end wasn't found we return false, maze, o and time


print(astar(100, 0, 100)[3])
