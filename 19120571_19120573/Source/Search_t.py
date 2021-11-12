"""Search T"""

from Utility import *

# Thuật giải A_t
def search_t(start, end, matrix, bonus_points):
    pq = [[start, 0]]
    close = []
    previous = init_pre(matrix)
    weights = init_weights(matrix, bonus_points)
    gs_s = {}
    cost = 0
    while len(pq) != 0 and pq[0][0] != end:
        s = pq.pop(0)
        close.append(s[0])
        open = [i[0] for i in pq]
        ss = succs(matrix, s[0], open, close)
        for i in ss:
            gs = s[1] + weights[i]
            if previous[i] is None:
                previous[i] = s[0]
                pq.append([i, gs])
                gs_s[i] = gs
            elif gs < gs_s[i]:
                pq.remove([i, gs_s[i]])
                previous[i] = s[0]
                pq.append([i, gs])
                gs_s[i] = gs
        if (pq[0][0] == end):
            cost = pq[0][1]

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
            cur = previous[cur]
        path.reverse()
        visited = sub_list(close, path)
        return cost, path, visited
