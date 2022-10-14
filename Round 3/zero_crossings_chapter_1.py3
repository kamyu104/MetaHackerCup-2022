# Copyright (c) 2022 kamyu. All rights reserved.
#
# Meta Hacker Cup 2022 Round 3 - Problem E1. Zero Crossings - Chapter 1
# https://www.facebook.com/codingcompetitions/hacker-cup/2022/round-3/problems/E1
#
# Time:  O((N * M + Q) * log(N * M + Q))
# Space: O(N * M + Q)
#

from sortedcontainers import SortedList

def cross(o, a, b):
    return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

class Edge(object):
    def __init__(self, a, b):
        assert(a <= b)
        self.a = a
        self.b = b

    def __repr__(self):
        return f"({self.a}, {self.b})"

    def __eq__(self, other):
        return (self.a, self.b) == (other.a, other.b)

    def __lt__(self, other):
        if self.a == other.a:
            return cross(self.a, self.b, other.b) > 0
        if other.a[0] <= self.a[0] < other.b[0]:
            return cross(other.a, self.a, other.b) > 0
        elif self.a[0] <= other.a[0] < self.b[0]:
            return cross(self.a, other.a, self.b) < 0
        assert(False)

def iter_dfs1(adj):
    hashes = [None]*len(adj)
    stk = [(1, 0)]
    while stk:
        step, u = stk.pop()
        if step == 1:
            stk.append((2, u))
            for v in reversed(adj[u]):
                stk.append((1, v))
        elif step == 2:
            hashes[u] = hash(tuple(sorted(hashes[v] for v in adj[u])))
    return hashes

def iter_dfs2(adj, hashes):
    stk = [(0, None)]
    while stk:
        u, h = stk.pop()
        hashes[u] = hash((h, hashes[u]))
        for v in reversed(adj[u]):
            stk.append((v, hashes[u]))

def find_parents(N, Q, events):
    def find_parent(e):
        i = sl.bisect_left((e,))
        return sl[i][1] if sl[i][2] else parent1[sl[i][1]]

    parent1, parent2 = [-1]*(N+1), [-1]*(2*Q)
    sl = SortedList([(Edge((MIN_X_Y-1, MAX_X_Y+1), (MAX_X_Y+1, MAX_X_Y+1)), 0, True)])
    for (_, t, _), idx, e, upper in events:
        if t == 0:
            sl.remove((e, idx, upper))
        elif t == 1:
            if parent1[idx] == -1:
                parent1[idx] = find_parent(e)
            sl.add((e, idx, upper))
        elif t == 2:
            parent2[idx] = find_parent(e)
    return parent1, parent2

def zero_crossings_chapter_1():
    N = int(input())
    events = []
    for idx in range(1, N+1):
        M = int(input())
        X_Y = list(map(int, input().split()))
        V = [(X_Y[2*i], X_Y[2*i+1]) for i in range(M)]
        for i in range(M):
            a, b = V[i], V[(i+1)%M]
            if a[0] == b[0]:
                continue
            upper = True
            if a[0] > b[0]:
                upper = False
                a, b = b, a
            events.append(((a[0], 1, -a[1]), idx, Edge(a, b), upper))
            events.append(((b[0], 0, -b[1]), idx, Edge(a, b), upper))
    Q = int(input())
    for idx in range(Q):
        A, B, C, D = map(int, input().split())
        for i, a in enumerate([(A, B), (C, D)]):
          events.append(((a[0], 2, -a[1]), 2*idx+i, Edge(a, a), False))
    events.sort(key=lambda x: x[0])  # sort by (a_x, t, -a_y)
    parent1, parent2 = find_parents(N, Q, events)
    adj = [[] for _ in range(N+1)]
    for i in range(1, N+1):
        adj[parent1[i]].append(i)
    hashes = iter_dfs1(adj)
    iter_dfs2(adj, hashes)
    return sum(hashes[parent2[2*idx+0]] == hashes[parent2[2*idx+1]] for idx in range(Q))

MIN_X_Y, MAX_X_Y = 0, 10**9
for case in range(int(input())):
    print('Case #%d: %s' % (case+1, zero_crossings_chapter_1()))
