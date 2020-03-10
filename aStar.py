from random import random
import math


class Node:
    def __init__(self, parent=None, position=None):     # initialization of objects
        self.parent = parent
        self.position = position

        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):                    # function for comparing objects
        return self.position == other.position

    def __hash__(self):                         # function for hashing objects
        return hash(self.position)

    def __sub__(self, other):                   # function for subtractions objects
        return (self.position - other.position, self.position[0] - other.position[0])


def astar(size, difficulty):
    grid = size
    diff = difficulty / 100

    maze = [[1 if random() < diff else 0 for x in range(grid)] for y in range(grid)]
    # creating a maze size x size

    maze[0][0] = 0
    maze[grid - 1][grid - 1] = 0    # making sure that start and goal are not wall

    start_node = Node(None, (0, 0))
    end = Node(None, (grid - 1, grid - 1))  # setting start and end node

    open_set = []
    closed_set = []
    o = []

    open_set.append(start_node)
    o.append(start_node.position)
    # adding start node to open set
    while open_set:

        current_node = open_set[0]
        current_index = 0

        for index, item in enumerate(open_set):     # looking in open set for the closest not to the end
            if item.f < current_node.f:
                current_node = item
                current_index = index

        open_set.pop(current_index)                 # deleting closest node from open set
        closed_set.append(current_node)             # and adding it to the close set

        if current_node == end:                     # if path is founded
            path = []
            while current_node.parent:                  # from latest node to the node after start
                path.append(current_node.position)      # adding nod position to the path table
                current_node = current_node.parent      # changing node to previous one
            path.append(current_node.position)          # adding the start node position
            return [path[::-1], maze, o]                # returning revers path,
                                                        # maze and position of every node that was in open set

        for new_position in [(-1, -1), (-1, 1), (1, -1), (1, 1), (0, -1), (0, 1), (-1, 0), (1, 0)]:

            position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])
            # creating a new position close to current node position

            if position[0] > (len(maze) - 1) or\
                    position[0] < 0 or\
                    position[1] > (len(maze[len(maze) - 1]) - 1) or\
                    position[1] < 0 or\
                    maze[position[0]][position[1]] != 0:    # checking if position is not walkable,
                continue                                    # if if not we skip one loop

            new_node = Node(current_node, position)     # if so creating a new node

            if new_node in closed_set:  # checking if node is in closet_set, if is we skip one loop
                continue

            if new_node in open_set:    # checking if node is in open_set, if is we skip one loop
                continue

            new_node.g = current_node.g + math.sqrt(((new_node.position[0] - current_node.position[0]) ** 2)
                                                    + ((new_node.position[1] - current_node.position[1]) ** 2))
            # calculating the g

            new_node.h = math.sqrt(((new_node.position[0] - end.position[0]) ** 2) + (
                    (new_node.position[1] - end.position[1]) ** 2))

            # calculating the h

            new_node.f = new_node.g + new_node.h    # calculating the f

            open_set.append(new_node)    # adding new node to open_set
            o.append(new_node.position)   # adding new nodes position to o

    return False, maze, o   # if end wasn't found we return false, maze and o





