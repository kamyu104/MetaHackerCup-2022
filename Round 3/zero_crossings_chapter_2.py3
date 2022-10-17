# Copyright (c) 2022 kamyu. All rights reserved.
#
# Meta Hacker Cup 2022 Round 3 - Problem E2. Zero Crossings - Chapter 2
# https://www.facebook.com/codingcompetitions/hacker-cup/2022/round-3/problems/E2
#
# Time:  O((N * M) * log(N * M) + Q * log(N * M)), pass in PyPy3 but Python3
# Space: O((N * M) * log(N * M))
#

from random import seed, random
from copy import copy

class TreapNode(object):
    def __init__(self, key):
        self.key = key
        self.prior = random()
        self.left = None
        self.right = None

class PersistentTreap(object):
    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = self.__insert(self.root, key)

    def delete(self, key):
        self.root = self.__delete(self.root, key)

    def __insert(self, x, key):
        if not x:
            return TreapNode(key)
        y = copy(x)
        if key < y.key:
            y.left = self.__insert(y.left, key)
            if y.left.prior < y.prior:
                return self.__rotate_left(y)
        elif y.key < key:
            y.right = self.__insert(y.right, key)
            if y.right.prior < y.prior:
                return self.__rotate_right(y)
        return y

    def __delete(self, x, key):
        y = copy(x)
        if key < y.key:
            y.left = self.__delete(y.left, key)
        elif y.key < key:
            y.right = self.__delete(y.right, key)
        else:
            return self.__delete_node(y)
        return y

    def __delete_node(self, x):
        if x.left and x.right:
            if x.left.prior < x.right.prior:
                x.left = copy(x.left)
                y = self.__rotate_left(x)
                y.right = self.__delete_node(x)
            else:
                x.right = copy(x.right)
                y = self.__rotate_right(x)
                y.left = self.__delete_node(x)
            return y
        return x.right if x.right else x.left

    def __rotate_left(self, x):
        y = x.left
        x.left = y.right
        y.right = x
        return y

    def __rotate_right(self, x):
        y = x.right
        x.right = y.left
        y.left = x
        return y

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

def binary_search_right(left, right, check):
    while left <= right:
        mid = left + (right-left)//2
        if not check(mid):
            right = mid-1
        else:
            left = mid+1
    return right

def bisect_right(node, x):
    result = None
    while node:
        if x < node.key:
            result = node
            node = node.left
        else:
            node = node.right
    return result

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

def find_root(roots, a):
    return roots[binary_search_right(0, len(roots)-1, lambda x: roots[x][0] <= a[0])][1]

def find_parent(parent, root, e):
    node = bisect_right(root, (e,))
    return node.key[1] if node.key[2] else parent[node.key[1]]

def find_parents(N, events):
    parent = [-1]*(N+1)
    pt = PersistentTreap()
    pt.insert((Edge((MIN_X_Y-1, MAX_X_Y+1), (MAX_X_Y+1, MAX_X_Y+1)), 0, True))
    roots = [(MIN_X_Y-1, pt.root)]
    for (a_x, t, _), idx, e, upper in events:
        if t == 0:
            pt.delete((e, idx, upper))
        elif t == 1:
            if parent[idx] == -1:
                parent[idx] = find_parent(parent, pt.root, e)
            pt.insert((e, idx, upper))
        roots.append((a_x, pt.root))
    return parent, roots

def zero_crossings_chapter_2():
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
    events.sort(key=lambda x: x[0])  # sort by (a_x, t, -a_y)
    parent, roots = find_parents(N, events)
    adj = [[] for _ in range(N+1)]
    for i in range(1, N+1):
        adj[parent[i]].append(i)
    hashes = iter_dfs1(adj)
    iter_dfs2(adj, hashes)
    Q = int(input())
    result = R_E = 0
    for _ in range(Q):
        A, B, C, D, E = map(int, input().split())
        a, b = (A^R_E, B^R_E), (C^R_E, D^R_E)
        R = int(hashes[find_parent(parent, find_root(roots, a), Edge(a, a))] ==
                hashes[find_parent(parent, find_root(roots, b), Edge(b, b))])
        result += R
        R_E ^= R*E
    return result

seed(0)
MIN_X_Y, MAX_X_Y = 0, 10**9
for case in range(int(input())):
    print('Case #%d: %s' % (case+1, zero_crossings_chapter_2()))
