"""Greedy best first search"""
from Utility import *


def gbfs_no_bonus(start: tuple, end: tuple, matrix, heuristic):
  pq = [[start, 0]]
  close = []
  previous = init_pre(matrix)
  while len(pq) != 0 and pq[0][0] != end:
    s = pq.pop(0)
    close.append(s[0])
    open = [i[0] for i in pq]
    ss = succs(matrix, s[0], open, close)
    for i in ss:
      d = heuristic(i, end)
      if previous[i] is None:
        previous[i] = s[0]
        pq.append([i, d])
    pq.sort(key=lambda i:i[1])

  if len(pq) == 0:
    return None
  else:
    cur = end
    path = []
    while True:
      if cur is None:
        break
      path.append(cur)
      cur = previous[cur]
    path.reverse()
    visited = sub_list(close, path)
    return len(path)-1, path, visited
