"""A*"""

from Utility import *

def A_star_no_bonus(start, end, matrix, heuristic):
    pq = {start: [0, euclid_norm(start, end)]}
    close = []
    previous = init_pre(matrix)
    top = None
    cost = None
    while len(pq) != 0:
        top = next(iter(pq))
        s = pq.pop(top)
        if top == end:
            cost = s[0]
            break
        open = [i for i in pq.keys()]
        close.append(top)
        ss = succs(matrix, top, [], close)
        for i in ss:
            d = heuristic(i, end)
            if previous[i] is None:
                previous[i] = top
                pq[i] = [s[0] + 1, d]
            elif s[0] < pq[i][0]:
                previous[i] = top
                pq[i] = [s[0] + 1, d]
        pq = dict(sorted(pq.items(), key=lambda v: v[1][0] + v[1][1]))

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
        return cost, path, visited
