# Copyright (c) 2022 kamyu. All rights reserved.
#
# Meta Hacker Cup 2022 Round 1 - Problem C. Lemonade Life
# https://www.facebook.com/codingcompetitions/hacker-cup/2022/round-1/problems/C
#
# Time:  O(NlogN + V^2), O(V) = O(len(hull)) = O(MAX_X_Y^(2/3)), pass in PyPy3 but Python3
# Space: O(N + V)
#

# Template: https://en.wikibooks.org/wiki/Algorithm_Implementation/Geometry/Convex_hull/Monotone_chain#Python
def convex_hull(points):  # Time: O(NlogN), Space: O(N)
    points = sorted(set(points))

    if len(points) <= 1:
        return points

    def cross(o, a, b):
        return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

    lower = []
    for p in points:
        while len(lower) >= 2 and cross(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)
    upper = []
    for p in reversed(points):
        while len(upper) >= 2 and cross(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)
    return lower[:-1] + upper[:-1]

def lemonade_life():
    N, K, D = map(int, input().split())
    houses = [tuple(map(int, input().split())) for _ in range(N)]
    hull = convex_hull(houses)
    src, dst = hull.index(houses[0]), hull.index(houses[-1])
    dist = [INF]*len(hull)
    dist[src] = 0
    lookup = [False]*len(hull)
    for _ in range(len(hull)):  # Time: O(V^2), Space: O(V)
        u = dst
        for v in range(len(hull)):
            if lookup[v]:
                continue
            if dist[v] < dist[u]:
                u = v
        if u == dst:
            break
        lookup[u] = True
        for v in range(len(hull)):
            if lookup[v]:
                continue
            d = (hull[u][0]-hull[v][0])**2+(hull[u][1]-hull[v][1])**2
            if d <= D**2:
                dist[v] = min(dist[v], dist[u]+max(K, d))
    return dist[dst] if dist[dst] != INF else -1

INF = float("inf")
for case in range(int(input())):
    print('Case #%d: %s' % (case+1, lemonade_life()))
