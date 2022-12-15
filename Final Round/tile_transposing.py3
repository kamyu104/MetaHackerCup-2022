# Copyright (c) 2022 kamyu. All rights reserved.
#
# Meta Hacker Cup 2022 Final Round - Problem C. Tile Transposing
# https://www.facebook.com/codingcompetitions/hacker-cup/2022/final-round/problems/C
#
# Time:  O(M * N * log(M * N)), pass in PyPy3 but Python3
# Space: O(M * N)
#

class RollbackUnionFind(object):  # Time: O(n * alpha(n)), Space: O(n)
    def __init__(self, n):
        self.set = list(range(n))
        self.size = [1]*n
        self.snapshots = []  # added
        self.undos = []  # added

    def find_set(self, x):
        stk = []
        while self.set[x] != x:  # path compression
            stk.append(x)
            x = self.set[x]
        while stk:
            y = stk.pop()
            self.undos.append((~y, self.set[y]))  # added
            self.set[y] = x
        return x

    def union_set(self, x, y):
        x, y = self.find_set(x), self.find_set(y)
        if x == y:
            return False
        if self.size[x] > self.size[y]:  # union by size
            x, y = y, x
        self.undos.append((x, y))  # added
        self.set[x] = self.set[y]
        self.size[y] += self.size[x]
        return True

    def total(self, x):
        return self.size[self.find_set(x)]

    def snapshot(self):  # added
        self.snapshots.append(len(self.undos))

    def rollback(self):  # added
        for _ in range(len(self.undos)-self.snapshots.pop()):
            x, y = self.undos.pop()
            if x >= 0:
                self.size[y] -= self.size[x]
                self.set[x] = x
            else:
                self.set[~x] = y

def tile_transposing():
    def merge(i):
        lookup[i] = True
        r, c = divmod(i, C)
        for dr, dc in DIRECTIONS:
            nr, nc = r+dr, c+dc
            ni = nr*C+nc
            if 0 <= nr < R and 0 <= nc < C and G[ni] == G[i] and lookup[ni]:
                uf.union_set(i, ni)

    def dfs(left, right):
        if left == right:
            i = left
            r, c = divmod(i, C)
            for dr, dc in DIRECTIONS:
                nr, nc = r+dr, c+dc
                ni = nr*C+nc
                if not (0 <= nr < R and 0 <= nc < C and G[ni] != G[i]):
                    continue
                uf.snapshot()
                for dr, dc in DIRECTIONS:
                    nnr, nnc = nr+dr, nc+dc
                    nni = nnr*C+nnc
                    if 0 <= nnr < R and 0 <= nnc < C and nni != i and G[nni] == G[i]:
                        uf.union_set(i, nni)
                if uf.total(i) >= 3:
                    result[0] += uf.total(i)
                uf.rollback()
            return
        mid = left + (right-left)//2
        uf.snapshot()
        for i in range(mid+1, right+1):
            merge(i)
        dfs(left, mid)
        for i in range(mid+1, right+1):
            lookup[i] = False
        uf.rollback()
        uf.snapshot()
        for i in range(left, mid+1):
            merge(i)
        dfs(mid+1, right)
        for i in range(left, mid+1):
            lookup[i] = False
        uf.rollback()

    R, C = map(int, input().split())
    G = []
    for _ in range(R):
        G.extend(list(map(int, input().split())))
    uf = RollbackUnionFind(R*C)
    lookup = [False]*(R*C)
    result = [0]
    dfs(0, len(lookup)-1)
    return result[0]*2

DIRECTIONS = [(1, 0), (0, 1), (-1, 0), (0, -1)]
for case in range(int(input())):
    print('Case #%d: %s' % (case+1, tile_transposing()))
