# Copyright (c) 2022 kamyu. All rights reserved.
#
# Meta Hacker Cup 2022 Round 1 - Problem A2. Consecutive Cuts - Chapter 2
# https://www.facebook.com/codingcompetitions/hacker-cup/2022/round-1/problems/A2
#
# Time:  O(N)
# Space: O(1)
#
# rolling hash solution
#

from functools import reduce

def check(A, B, i):
    return all(A[(i+j)%len(A)] == B[j]for j in range(len(A)))

def hash(nums):
    return [reduce(lambda h, x: (h*p+x)%MOD, nums) for p in P]

def update(h, base, x):
    return [(h[i]*P[i]+x*(1-base[i]))%MOD for i in range(len(P))]

def consecutive_cuts_chapter_2():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    base = [pow(p, N, MOD) for p in P]
    got, want = hash(A), hash(B)
    for i in range(N):
        if got == want and check(A, B, i):
            if (N == 2 and K%2 == int(i != 0)) or (N > 2 and K != int(i == 0)):
                return "YES"
        got = update(got, base, A[i])
    return "NO"

MOD, P = 10**9+7, (113, 109)  # double hash (single hash is enough)
for case in range(int(input())):
    print('Case #%d: %s' % (case+1, consecutive_cuts_chapter_2()))
