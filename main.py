# Iterative Floyd Warshall algorithm:

import sys
import itertools

NO_PATH = sys.maxsize
graph = [[0, 7, NO_PATH, 8],
         [NO_PATH, 0, 5, NO_PATH],
         [NO_PATH, NO_PATH, 0, 2],
         [NO_PATH, NO_PATH, NO_PATH, 0]]
MAX_LENGTH = len(graph[0])


def floyd(distance):
    for intermediate, start_node, end_node in itertools.product\
                (range(MAX_LENGTH), range(MAX_LENGTH), range(MAX_LENGTH)):

        # Assume that if start_node and end_node are the same
        # then the distance would be zero
        if start_node == end_node:
            distance[start_node][end_node] = 0
            continue

        # return all possible paths and find the minimum
        distance[start_node][end_node] = min(distance[start_node][end_node],
                                             distance[start_node][intermediate] + distance[intermediate][end_node])

    # Any value that have sys.maxsize has no path
    print(distance)


floyd(graph)

# Recursive Floyd Warshall Algorithm:

NO_PATH = sys.maxsize
graph = [[0, 7, NO_PATH, 8],
         [NO_PATH, 0, 5, NO_PATH],
         [NO_PATH, NO_PATH, 0, 2],
         [NO_PATH, NO_PATH, NO_PATH, 0]]
max_length = len(graph[0])


def shortest_path(i, j, k, w):
    if k == 0:
        if i == j:
            return 0
        return w[i][j]
    else:
        return min(shortest_path(i, j, k - 1, w),
                   shortest_path(i, k, k - 1, w) + shortest_path(k, j, k - 1, w))


def floyd_warshall(distance):
    for k in range(max_length):
        for i in range(max_length):
            for j in range(max_length):
                distance[i][j] = shortest_path(i, j, k, distance)
    return distance


print(floyd_warshall(graph))
