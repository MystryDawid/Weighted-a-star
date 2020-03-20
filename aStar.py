from random import random
import math
import time as _time



class Node:
    def __init__(self, parent=None, position=None):     # constructor of objects

        self.parent = parent
        self.position = position
        self.id = 0

        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):    # function for comparing objects
        return self.position == other.position

    def __sub__(self, other):   # function for subtractions objects
        return self.position - other.position


def smallest_f(dict):
    min_f = list(dict.values())[0]  # getting first element
    for x in dict:
        if min_f.f > dict[x].f:
            min_f = dict[x]
    return min_f    # retuning element with smallest f


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

    o = [start_node.position]

    open_set = {}   # adding start node to open set and o
    closed_set = {}      # creating closed set

    open_set[start_node.id] = start_node

    while open_set:

        current_node = smallest_f(open_set)  # getting node with smallest f

        if current_node.position == end.position:     # if path is founded

            path = [current_node.position]      # adding the start node position

            while current_node.parent:
                current_node = current_node.parent      # adding node position to the path
                path.append(current_node.position)      # changing node to previous one

            time = _time.time() - start_time    # stopping timer
            # returning revers path, maze and position of every node that was in open set and time
            return path[::-1], maze, o, time

        del open_set[current_node.id]       # deleting closest node from open set
        closed_set[current_node.id] = current_node    # and adding it to the close set

        d = current_node.g  # calculating d (depth of search)
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
            new_node.id = new_node.position[0] + (new_node.position[1] * grid)

            if new_node.id in closed_set:    # checking if node is in closet_set, if is we skip one loop
                continue

            if new_node.id in open_set:      # checking if node is in open_set, if is we skip one loop
                continue

            # calculating h
            new_node.h = math.sqrt((new_node.position[0] - end.position[0]) ** 2
                                   + (new_node.position[1] - end.position[1]) ** 2)

            # calculating g
            new_node.g = current_node.g + math.sqrt((new_node.position[0] - current_node.position[0]) ** 2
                                                    + (new_node.position[1] - current_node.position[1]) ** 2)

            # calculating f using dynamic weight
            new_node.f = new_node.g + w * new_node.h

            open_set[new_node.id] = new_node       # adding new node to open_set
            o.append(new_node.position)     # adding new nodes position to o

    time = _time.time() - start_time    # stopping timer
    return False, maze, o, time  # if end wasn't found we return false, maze, o and time

