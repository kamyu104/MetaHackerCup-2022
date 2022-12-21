# Copyright (c) 2022 kamyu. All rights reserved.
#
# Meta Hacker Cup 2022 Final Round - Problem D. Alphabet Adventuring
# https://www.facebook.com/codingcompetitions/hacker-cup/2022/final-round/problems/D
#
# Time:  O((R^2 + log(N + Q)) * (N + Q) + Q * (R^2 + log(N + Q))* log(N + Q))
# Space: O((R^2 + log(N + Q)) * (N + Q))
#

from functools import partial

# Template:
# https://github.com/kamyu104/GoogleKickStart-2020/blob/main/Round%20D/locked_doors.py
class TreeInfos(object):  # Time: O(NlogN), Space: O(NlogN), N is the number of nodes
    def __init__(self, adj, edges):
        def divide(u, p):
            def update_up(u, p):
                if p == -1:
                    return
                eid = edge_id[u, p]
                if not P[p]:
                    up[eid] = [eid]*(26*26)
                    return
                up[eid] = up[edge_id[p, P[p][0]]][:]
                for v, c in adj[p]:
                    if v == P[p][0] or v == u:
                        continue
                    up[eid][c*26+par_c[p]] = eid

            if p != -1:
                P[u].append(p)  # ancestors of the node i
                D[u] = D[p]+1
            i = 0
            while i < len(P[u]) and i < len(P[P[u][i]]):
                P[u].append(P[P[u][i]][i])
                i += 1
            update_up(u, p)  # added
            stk.append(partial(postprocess, u, p))
            for v, c in adj[u]:
                if v == p:
                    continue
                par_c[v] = c  # added
                stk.append(partial(divide, v, u))

        def postprocess(u, p):
            def update_down(u, p):
                nv, nc = heavy_child[u], heavy_c[u]
                if nv == -1:
                    down[u] = [u]*(26*26)
                    return
                down[u] = down[nv][:]
                for v, c in adj[u]:
                    if v == nv or v == p:
                        continue
                    down[u][c*26+nc] = u

            def update_heavy(u, p):
                mx = 0
                for v, c in adj[u]:
                    if v == p:
                        continue
                    size[u] += size[v]
                    if size[v] > mx:
                        mx = size[v]
                        heavy_descent[u], heavy_child[u], heavy_c[u] = heavy_descent[v], v, c

            update_heavy(u, p)  # added
            update_down(u, p)  # added

        N = len(adj)
        D, P = [0]*N, [[] for _ in range(N)]

        # added
        size = [1]*N
        par_c, heavy_c, heavy_child = [[-1]*N for _ in range(3)]
        heavy_descent, ancestor = list(range(N)), list(range(N))
        up = [None for _ in range(len(edges))]
        down = [None for _ in range(N)]
        edge_id = {(u, v): i for i, (u, v) in enumerate(edges)}

        stk = []
        stk.append(partial(divide, 0, -1))
        while stk:
            stk.pop()()

        self.adj = adj
        self.D, self.P = D, P

        # added
        self.edges = edges
        self.par_c, self.heavy_c, self.heavy_child = par_c, heavy_c, heavy_child
        self.heavy_descent, self.ancestor = heavy_descent, ancestor
        self.up, self.down = up, down
        self.edge_id = edge_id

    def __get_ancestor(self, u):
        stk = []
        while self.ancestor[u] != u:
            stk.append(u)
            u = self.ancestor[u]
        for x in stk:
            self.ancestor[x] = u
        return u

    def __get_up_edge(self, eid, pid):
        stk = []
        while self.up[eid][pid] != eid:
            stk.append(eid)
            eid = self.up[eid][pid]
        for x in stk:
            self.up[x][pid] = eid
        return eid

    def remove(self, u):
        p = self.P[u][0]
        self.ancestor[u] = self.__get_ancestor(p)
        if not self.P[p]:
            return
        c = next(c for v, c in self.adj[p] if v == u)
        par_eid = self.edge_id[p, self.P[p][0]]
        for v, _ in self.adj[p]:
            if v == self.P[p][0] or v != self.ancestor[v]:
                continue
            pid = c*26+self.par_c[p]
            self.up[self.edge_id[v, p]][pid] = self.__get_up_edge(par_eid, pid)

    def query(self, u, k, alpha):
        def binary_lift(u, k):
            for i in reversed(range(len(self.P[u]))):
                if k&(1<<i):
                    u = self.P[u][i]
            return u

        def go_up(u, k):
            if not self.P[u]:
                return u, k
            p = self.P[u][0]
            for v, c in self.adj[u]:
                if v == p or v != self.ancestor[v]:
                    continue
                if lookup[self.par_c[u]] > lookup[c]:
                    return u, k
            k0, u0 = k, u
            eid, v = self.edge_id[u, p], 0
            for pid in stops:
                _, nv = self.edges[self.__get_up_edge(eid, pid)]
                if self.D[nv] > self.D[v]:
                    v = nv
            diff = self.D[u]-self.D[v]
            if k <= diff:
                u = binary_lift(u, k)
                return u, 0
            k -= diff
            u = v
            nu = binary_lift(u0, k0-k-1)
            v, c = -1, 26
            for nv, nc in self.adj[u]:
                if (self.P[u] and nv == self.P[u][0]) or nv == nu or nv != self.ancestor[nv]:
                    continue
                if lookup[nc] < c:
                    c, v = lookup[nc], nv
            if v == -1:
                return u, 0
            k -= 1
            u = v
            return u, k

        def go_down(u, k):
            while k:
                if self.heavy_child[u] == -1:
                    break
                v = self.heavy_descent[u]
                for pid in stops:
                    nv = self.down[u][pid]
                    if self.D[nv] < self.D[v]:
                        v = nv
                v = self.__get_ancestor(v)
                diff = self.D[v]-self.D[u]
                if k <= diff:
                    v = binary_lift(v, diff-k)
                    return v, 0
                k -= diff
                nv, nc = -1, 26
                for nnv, nnc in self.adj[v]:
                    if (self.P[v] and nnv == self.P[v][0]) or nnv != self.ancestor[nnv]:
                        continue
                    if lookup[nnc] < nc:
                        nc, nv = lookup[nnc], nnv
                if nv == -1:
                    return v, 0
                k -= 1
                u = nv
            return u, k

        stops = [alpha[i]*26+alpha[j] for i in range(len(alpha)) for j in range(i+1, len(alpha))]
        lookup = [0]*26
        for i, c in enumerate(alpha):
            lookup[c] = i
        u, k = go_up(u, k)
        return go_down(u, k)[0]

def alphabet_adventuring():
    N = int(input())
    adj = [[] for _ in range(N)]
    edges = []
    for _ in range(N-1):
        u, v, c = input().split()
        u, v, c = int(u)-1, int(v)-1, ord(c)-ord('A')
        adj[u].append((v, c))
        adj[v].append((u, c))
        edges.append((u, v))
        edges.append((v, u))
    Q = int(input())
    queries = []
    for _ in range(Q):
        args = input().split()
        if args[0] == '1':
            adj.append([])
            u, v, c = len(adj)-1, int(args[1])-1, ord(args[2])-ord('A')
            adj[u].append((v, c))
            adj[v].append((u, c))
            edges.append((u, v))
            edges.append((v, u))
            queries.append((0, (u,)))
        else:
            queries.append((1, (int(args[1])-1, int(args[2]), list(map(lambda x: ord(x)-ord('A'), args[3])))))
    tree = TreeInfos(adj, edges)
    result = []
    for t, args in reversed(queries):
        if t == 0:
            u = args[0]
            tree.remove(u)
        else:
            u, k, alpha = args
            result.append(tree.query(u, k, alpha)+1)
    return " ".join(map(str, reversed(result)))

for case in range(int(input())):
    print('Case #%d: %s' % (case+1, alphabet_adventuring()))
