# Copyright (c) 2022 kamyu. All rights reserved.
#
# Meta Hacker Cup 2022 Qualification Round - Problem B2. Watering Well - Chapter 1
# https://www.facebook.com/codingcompetitions/hacker-cup/2022/round-1/problems/B1
#
# Time:  O(min(N * Q, MAX_A_B_X_Y^2))
# Space: O(min(N + Q, MAX_A_B_X_Y))
#

from collections import Counter

def watering_well_chapter_1():
    N = int(input())
    A_cnt, B_cnt = Counter(), Counter()
    for _ in range(N):
        A, B = list(map(int, input().split()))
        A_cnt[A] += 1
        B_cnt[B] += 1
    X_cnt, Y_cnt = Counter(), Counter()
    for _ in range(int(input())):
        X, Y = list(map(int, input().split()))
        X_cnt[X] += 1
        Y_cnt[Y] += 1
    result = 0
    for X, cntX in X_cnt.items():
        for A, cntA in A_cnt.items():
            result = (result+cntX*cntA*(X-A)**2)%MOD
    for Y, cntY in Y_cnt.items():
        for B, cntB in B_cnt.items():
            result = (result+cntY*cntB*(Y-B)**2)%MOD
    return result

MOD = 10**9+7
for case in range(int(input())):
    print('Case #%d: %s' % (case+1, watering_well_chapter_1()))
