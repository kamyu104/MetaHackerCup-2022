# Copyright (c) 2022 kamyu. All rights reserved.
#
# Meta Hacker Cup 2022 Round 3 - Problem D1. First Time - Chapter 1
# https://www.facebook.com/codingcompetitions/hacker-cup/2022/round-3/problems/D1
#
# Time:  O(M + NlogN)
# Space: O(N)
#

def ceil_divide(a, b):
    return (a+b-1)//b

def first_time_chapter_1():
    def merge(a, b):  # Total Time: O(NlogN)
        if len(group[a]) > len(group[b]):
            group[a], group[b] = group[b], group[a]
        cnt = len(group[a])+len(group[b])
        while group[a]:
            group[b].add(group[a].pop())
        return cnt-len(group[b])

    N, M, K = map(int, input().split())
    group = [{i//K} for i in range(N)]
    result = INF
    cnt = N-ceil_divide(N, K)
    for t in range(1, M+1):
        A, B = map(int, input().split())
        cnt -= merge(A-1, B-1)
        if cnt == 0:
            result = min(result, t)
    return result if result != INF else -1

INF = float("inf")
for case in range(int(input())):
    print('Case #%d: %s' % (case+1, first_time_chapter_1()))
