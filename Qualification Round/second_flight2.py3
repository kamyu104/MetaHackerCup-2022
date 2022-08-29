# Copyright (c) 2022 kamyu. All rights reserved.
#
# Meta Hacker Cup 2022 Qualification Round - Problem D. Second Flight
# https://www.facebook.com/codingcompetitions/hacker-cup/2022/qualification-round/problems/D
#
# Time:  O(N + Q + M * sqrt(Q))
# Space: O(N + M + Q)
#

def second_flight():
    N, M, Q = map(int, input().split())
    adj = [{} for _ in range(N)]
    for _ in range(M):
        A, B, C = map(int, input().split())
        A -= 1
        B -= 1
        adj[A][B] = adj[B][A] = C
    result = []
    lookup = {}
    for _ in range(Q):
        X, Y = map(int, input().split())
        X -= 1
        Y -= 1
        if (len(adj[X]), X) > (len(adj[Y]), Y):
            X, Y = Y, X
        if X*N+Y in lookup:
            result.append(lookup[X*N+Y])
            continue
        cnt = sum(min(adj[X][Z], adj[Y][Z]) for Z in adj[X].keys() if Z in adj[Y])
        if Y in adj[X]:
            cnt += 2*adj[X][Y]
        lookup[X*N+Y] = cnt
        result.append(cnt)
    return " ".join(map(str, result))

for case in range(int(input())):
    print('Case #%d: %s' % (case+1, second_flight()))
