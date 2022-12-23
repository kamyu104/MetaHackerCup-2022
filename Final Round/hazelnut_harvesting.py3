# Copyright (c) 2022 kamyu. All rights reserved.
#
# Meta Hacker Cup 2022 Final Round - Problem E. Hazelnut Harvesting
# https://www.facebook.com/codingcompetitions/hacker-cup/2022/final-round/problems/E
#
# Time:  O(NlogN)
# Space: O(NlogN)
#

class SegmentTree(object):
    def __init__(self, N, recs):
        self.N = N
        self.recs = recs
        self.tree = [[[], []] for _ in range(2*2**((N-1).bit_length()))]
        self.lookup = [False]*len(recs)

    def update(self, L, R, v):
        def _update(i, left, right, L, R, v):
            self.tree[i][0].append(v)
            if (left, right) == (L, R):
                self.tree[i][1].append(v)
                return
            mid = left+(right-left)//2
            if R <= mid:
                _update(2*i, left, mid, L, R, v)
                return
            if L >= mid+1:
                _update(2*i+1, mid+1, right, L, R, v)
                return
            _update(2*i, left, mid, L, mid, v)
            _update(2*i+1, mid+1, right, mid+1, R, v)

        return _update(1, 0, self.N-1, L, R, v)

    def query(self, L, R, v):
        def _query(i, left, right, L, R, v):
            while self.tree[i][1] and self.lookup[self.tree[i][1][-1]]:
                self.tree[i][1].pop()
            if self.tree[i][1] and self.recs[self.tree[i][1][-1]][1] >= v:
                return self.tree[i][1][-1]
            if (left, right) == (L, R):
                while self.tree[i][0] and self.lookup[self.tree[i][0][-1]]:
                    self.tree[i][0].pop()
                if self.tree[i][0] and self.recs[self.tree[i][0][-1]][1] >= v:
                    return self.tree[i][0][-1]
                return -1
            mid = left+(right-left)//2
            if R <= mid:
                return _query(2*i, left, mid, L, R, v)
            if L >= mid+1:
                return _query(2*i+1, mid+1, right, L, R, v)
            l = _query(2*i, left, mid, L, mid, v)
            if l != -1:
                return l
            return _query(2*i+1, mid+1, right, mid+1, R, v)

        return _query(1, 0, self.N-1, L, R, v)

    def remove(self, i):
        self.lookup[i] = True

def hazelnut_harvesting():
    N = int(input())
    recs = []
    x_set, y_set = set(), set()
    for _ in range(N):
        X, Y = map(int, input().split())
        recs.append([X-1, X+1, Y-1, Y+1])
        for d in range(-1, 1+1):
            x_set.add(X+d)
            y_set.add(Y+d)
    x_idx = {x:i for i, x in enumerate(sorted(x_set))}
    y_idx = {y:i for i, y in enumerate(sorted(y_set))}
    for i, (l, r, d, u) in enumerate(recs):
        recs[i] = [x_idx[l], x_idx[r], y_idx[d], y_idx[u]]
    recs.sort(key=lambda x:x[0])
    st = SegmentTree(len(y_idx), recs)
    result = 0
    for i in range(len(recs)):
        while True:
            j = st.query(recs[i][2], recs[i][3], recs[i][0])
            if j == -1:
                st.update(recs[i][2], recs[i][3], i)
                result += (recs[i][1]-recs[i][0])*(recs[i][3]-recs[i][2])
                break
            result -= (recs[j][1]-recs[j][0])*(recs[j][3]-recs[j][2])
            recs[i] = [min(recs[i][0], recs[j][0]),
                       max(recs[i][1], recs[j][1]),
                       min(recs[i][2], recs[j][2]),
                       max(recs[i][3], recs[j][3])]
            st.remove(j)
    return result

for case in range(int(input())):
    print('Case #%d: %s' % (case+1, hazelnut_harvesting()))
