# Copyright (c) 2022 kamyu. All rights reserved.
#
# Meta Hacker Cup 2022 Qualification Round - Problem D. Second Flight
# https://www.facebook.com/codingcompetitions/hacker-cup/2022/qualification-round/problems/D
#
# Time:  O(N + (M + Q) * sqrt(M))
# Space: O(N + M * sqrt(M))
#

from collections import Counter

def second_flight():
    N, M, Q = map(int, input().split())
    adj = [{} for _ in range(N)]
    for _ in range(M):
        A, B, C = map(int, input().split())
        A -= 1
        B -= 1
        adj[A][B] = adj[B][A] = C
    count = [Counter() for _ in range(N)]
    for Y in range(N):  # Time: O(M * sqrt(M)), Space: O(M * sqrt(M))
        if len(adj[Y]) <= M**0.5:
            continue
        for Z in adj[Y].keys():
            for X in adj[Z].keys():
                if X == Y or (len(adj[X]), X) > (len(adj[Y]), Y):
                    continue
                count[X][Y] += min(adj[X][Z], adj[Y][Z])
    result = []
    for _ in range(Q):  # Time: O(Q * sqrt(M))
        X, Y = map(int, input().split())
        X -= 1
        Y -= 1
        if (len(adj[X]), X) > (len(adj[Y]), Y):
            X, Y = Y, X
        cnt = count[X][Y] if len(adj[Y]) > M**0.5 else sum(min(adj[X][Z], adj[Y][Z]) for Z in adj[X].keys() if Z in adj[Y])
        if Y in adj[X]:
            cnt += 2*adj[X][Y]
        result.append(cnt)
    return " ".join(map(str, result))

for case in range(int(input())):
    print('Case #%d: %s' % (case+1, second_flight()))
