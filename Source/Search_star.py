"""Search Star"""
from Utility import *

def search_star(start, end, matrix, heuristic, bonus_points):
    pq = [[start, 0]]
    close = []
    previous = init_pre(matrix)
    weights = init_weights(matrix, bonus_points)
    fs_s = {}
    cost = 0
    while len(pq) != 0 and pq[0][0] != end:
        s = pq.pop(0)
        close.append(s[0])
        open = [i[0] for i in pq]
        ss = succs(matrix, s[0], open, close)
        for i in ss:
            d = heuristic(i, end)
            fs = s[1] + weights[i] + d
            if previous[i] is None:
                previous[i] = s[0]
                pq.append([i, fs])
                fs_s[i] = fs
            elif fs < fs_s[i]:
                pq.remove([i, fs_s[i]])
                previous[i] = s[0]
                pq.append([i, fs])
                fs_s[i] = fs

        pq.sort(key=lambda i: i[1])

    if len(pq) == 0:
        return None
    else:
        cur = end
        path = []
        while True:
            if cur is None:
                break
            path.append(cur)
            cost += weights[cur]
            cur = previous[cur]
        path.reverse()
        visited = sub_list(close, path)
        return cost, path, visited
