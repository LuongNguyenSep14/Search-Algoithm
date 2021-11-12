# import package
import os
import matplotlib.pyplot as plt
import math


# support function
# 1. Visualize Function
def visualize_maze(matrix, bonus, start, end, route=None, visited=None):
    """
    Args:
      1. matrix: The matrix read from the input file,
      2. bonus: The array of bonus points,
      3. start, end: The starting and ending points,
      4. route: The route from the starting point to the ending one, defined by an array of (x, y), e.g. route = [(1, 2), (1, 3), (1, 4)]
    """
    # 1. Define walls and array of direction based on the route
    walls = [(i, j) for i in range(len(matrix)) for j in range(len(matrix[0])) if matrix[i][j] == 'x']

    if route:
        direction = []
        for i in range(1, len(route)):
            if route[i][0] - route[i - 1][0] > 0:
                direction.append('v')  # ^
            elif route[i][0] - route[i - 1][0] < 0:
                direction.append('^')  # v
            elif route[i][1] - route[i - 1][1] > 0:
                direction.append('>')
            else:
                direction.append('<')

        direction.pop(0)

    # 2. Drawing the map
    ax = plt.figure(dpi=100).add_subplot(111)

    for i in ['top', 'bottom', 'right', 'left']:
        ax.spines[i].set_visible(False)

    plt.scatter([i[1] for i in walls], [-i[0] for i in walls],
                marker='X', s=100, color='black')

    plt.scatter([i[1] for i in bonus], [-i[0] for i in bonus],
                marker='P', s=100, color='green')
    if visited:
        plt.scatter([i[1] for i in visited], [-i[0] for i in visited],
                    marker='.', s=100, color='pink')

    plt.scatter(start[1], -start[0], marker='*',
                s=100, color='gold')

    if route:
        for i in range(len(route) - 2):
            plt.scatter(route[i + 1][1], -route[i + 1][0],
                        marker=direction[i], color='red')

    plt.text(end[1], -end[0], 'EXIT', color='red',
             horizontalalignment='center',
             verticalalignment='center')
    plt.xticks([])
    plt.yticks([])
    plt.show()

    print(f'Starting point (x, y) = {start[0], start[1]}')
    print(f'Ending point (x, y) = {end[0], end[1]}')

    for _, point in enumerate(bonus):
        print(f'Bonus point at position (x, y) = {point[0], point[1]} with point {point[2]}')


# 2. Read File Function
def read_file(file_name):
    f = open(file_name, 'r')
    n_bonus_points = int(next(f)[:-1])
    bonus_points = []
    for i in range(n_bonus_points):
        x, y, reward = map(int, next(f)[:-1].split(' '))
        bonus_points.append((x, y, reward))

    text = f.read()
    matrix = [list(i) for i in text.splitlines()]
    f.close()

    return bonus_points, matrix


# 3. Extract Start, End point function
def extract_point(matrix):
    start = None
    end = None
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 'S':
                start = (i, j)

            elif matrix[i][j] == ' ':
                if (i == 0) or (i == len(matrix) - 1) or (j == 0) or (j == len(matrix[0]) - 1):
                    end = (i, j)

            else:
                pass
    return start, end


# 4. Generate Successor Function
def succs(matrix, point, open, close):
    dc = [0, 1, 0, -1]
    dr = [-1, 0, 1, 0]

    results = []
    for i in range(4):
        rr, cc = point[0] + dr[i], point[1] + dc[i]
        if matrix[rr][cc] == 'x':
            continue
        else:
            if (rr, cc) not in open and (rr, cc) not in close:
                results.append((rr, cc))
    return results


# 5. Initialize Back Track Function
def init_pre(matrix):
    dic = {}
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] != 'x':
                dic[(i, j)] = None
            else:
                pass
    return dic


# 6. Euclid Norm Function
def euclid_norm(X: tuple, Y: tuple):
    dx = X[0] - Y[0]
    dy = X[1] - Y[1]
    return math.sqrt(dx ** 2 + dy ** 2)


# 7. Manhattan Norm
def manhattan(X: tuple, Y: tuple):
    dx = X[0] - Y[0]
    dy = X[1] - Y[1]
    return abs(dx) + abs(dy)


# 8. Get point Function
def reward_bonus_point(point, bonus_points):
    for bonus_point in bonus_points:
        i, j, k = bonus_point
        if i == point[0] and j == point[1]:
            return k
    return 0


# 9. Initialize Weight Matrix Function
def init_weights(matrix, bonus_points):
    weights = {}
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == ' ':
                weights[(i, j)] = 1
            elif matrix[i][j] == 'S':
                weights[(i, j)] = 0
            elif matrix[i][j] == '+':
                weights[(i, j)] = reward_bonus_point((i, j), bonus_points)
            else:
                pass
    return weights


# 10. Subtract 2 list Function.
def sub_list(l1, l2):
    return list(set(l1) - set(l2))
