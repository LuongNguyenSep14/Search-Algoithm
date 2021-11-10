"""Greedy best first search"""
from Utility import *


# BFS with no bonus
def bfs_no_bonus(start, end, matrix):
    v = []
    v.append([start])  # v_0
    # close = []
    k = 0
    path = []
    previous = init_pre(matrix)
    while len(v[k]) != 0 and end not in v[k]:
        v.append([])  # v_k+1
        for s in v[k]:
            ss = succs(matrix, s, v[k], [])
            for i in ss:
                if previous[i] is None:
                    previous[i] = s
                    v[k + 1].append(i)
        k = k + 1
    close = []
    for i in range(0, k):
        for j in v[i]:
            close.append(j)

    if len(v[k]) == 0:
        return None
    else:
        cur = end
        cost = None
        for j in range(k + 1):  # start + path + end
            path.append(cur)
            cur = previous[cur]
        path.reverse()
        cost = len(path) - 1
        visited = sub_list(close, path)
        return cost, path, visited
