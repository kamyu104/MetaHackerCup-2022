# Copyright (c) 2022 kamyu. All rights reserved.
#
# Meta Hacker Cup 2022 Round 3 - Problem D2. First Time Chapter 2
# https://www.facebook.com/codingcompetitions/hacker-cup/2022/round-3/problems/D2
#
# Time:  O(M + NlogN)
# Space: O(N)
#

def gcd(a, b):
    while b:
        a, b = b, a%b
    return a

# Template:
# https://github.com/kamyu104/LeetCode-Solutions/blob/master/Python/longest-increasing-subsequence-ii.py
class SegmentTree(object):
    def __init__(self, N,
                 build_fn=lambda _: 0,
                 query_fn=lambda x, y: y if x is None else x if y is None else max(x, y),
                 update_fn=lambda x: x):
        self.tree = [None]*(2*2**((N-1).bit_length()))
        self.base = len(self.tree)//2
        self.query_fn = query_fn
        self.update_fn = update_fn
        for i in range(self.base, self.base+N):
            self.tree[i] = build_fn(i-self.base)
        for i in reversed(range(1, self.base)):
            self.tree[i] = query_fn(self.tree[2*i], self.tree[2*i+1])

    def update(self, i, h):
        x = self.base+i
        self.tree[x] = self.update_fn(h)
        while x > 1:
            x //= 2
            self.tree[x] = self.query_fn(self.tree[x*2], self.tree[x*2+1])

def first_time_chapter_2():
    def merge(a, b):  # Total Time: O(NlogN)
        if len(group[a]) > len(group[b]):
            group[a], group[b] = group[b], group[a]
        for x in group[a]:  # only keep the start of the segment with the same color
            if x-1 in group[b]:
                st.update(x, 0)
            if x+1 in group[b]:
                st.update(x+1, 0)
        while group[a]:
            group[b].add(group[a].pop())

    N, M = map(int, input().split())
    group = [{i} for i in range(N)]
    st = SegmentTree(N,
                     build_fn=lambda i: i,
                     query_fn=lambda x, y: y if x is None else x if y is None else gcd(x, y))
    result = [INF]*(N+1)
    result[1] = 0
    for t in range(1, M+1):
        A, B = map(int, input().split())
        merge(A-1, B-1)
        g = st.tree[1]  # gcd of all the starts of the segments with the same color
        result[g] = min(result[g], t)
    for K in range(1, N+1):
        result[K] = min(result[nK] for nK in range(0, N+1, K))
    return sum(result[K] if result[K] != INF else -1 for K in range(1, N+1))

INF = float("inf")
for case in range(int(input())):
    print('Case #%d: %s' % (case+1, first_time_chapter_2()))
