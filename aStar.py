from random import random
import math


class Node:
    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.position == other.position

    def __hash__(self):
        return hash(self.position)

    def __sub__(self, other):
        return (self.position[1] - other.position[1], self.position[0] - other.position[0])


def astar(size, difficulty):
    grid = size
    diff = difficulty / 100
    print(grid)
    maze = [[1 if random() < diff else 0 for x in range(grid)] for y in range(grid)]

    maze[0][0] = 0
    maze[grid - 1][grid - 1] = 0

    start_node = Node(None, (0, 0))
    end = Node(None, (grid - 1, grid - 1))

    open_set = []
    closed_set = []
    o = []

    open_set.append(start_node)
    o.append(start_node.position)
    while open_set:

        current_node = open_set[0]
        current_index = 0

        for index, item in enumerate(open_set):
            if item.f < current_node.f:
                current_node = item
                current_index = index

        open_set.pop(current_index)
        closed_set.append(current_node)

        if current_node == end:
            path = []
            while current_node.parent:
                path.append(current_node.position)
                current_node = current_node.parent
            path.append(current_node.position)
            return [path[::-1], maze, o]

        for new_position in [(-1, -1), (-1, 1), (1, -1), (1, 1), (0, -1), (0, 1), (-1, 0), (1, 0)]:

            position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])

            if position[0] > (len(maze) - 1) or\
                    position[0] < 0 or\
                    position[1] > (len(maze[len(maze) - 1]) - 1) or\
                    position[1] < 0:
                continue

            if maze[position[0]][position[1]] != 0:
                continue

            new_node = Node(current_node, position)

            if new_node in closed_set:
                continue

            new_node.g = current_node.g\
                         + math.sqrt(((new_node.position[0] - current_node.position[0]) ** 2)
                         + ((new_node.position[1] - current_node.position[1]) ** 2))

            new_node.h = math.sqrt(((new_node.position[0] - end.position[0]) ** 2) + (
                    (new_node.position[1] - end.position[1]) ** 2))

            new_node.f = new_node.g + new_node.h

            if new_node in open_set:
                continue

            open_set.append(new_node)
            o.append([new_node.position, new_node.g])

    return False, maze, o





