"""Dfs algorithm"""
from Utility import *

def dfs_no_bonus(start, end, matrix):
    close = []
    path = [start]
    visited = None
    while len(path) != 0 and path[-1] != end:
        top = path[-1]
        s = succs(matrix, top, path, close)
        if len(s) == 0:
            t = path.pop()
            close.append(t)
        else:
            path.append(s.pop())
    if len(path) == 0:
        return None
    else:
        visited = sub_list(close, path)
        return len(path) - 1, path, visited
