# Copyright (c) 2022 kamyu. All rights reserved.
#
# Meta Hacker Cup 2022 Qualification Round - Problem B2. Watering Well - Chapter 2
# https://www.facebook.com/codingcompetitions/hacker-cup/2022/round-1/problems/B2
#
# Time:  O(N + Q)
# Space: O(1)
#

def watering_well_chapter_2():
    N = int(input())
    X_square_total = X_total = Y_square_total = Y_total = 0
    for _ in range(N):
        X, Y = list(map(int, input().split()))
        X_total, X_square_total = (X_total+X)%MOD, (X_square_total+X**2)%MOD
        Y_total, Y_square_total = (Y_total+Y)%MOD, (Y_square_total+Y**2)%MOD
    result = 0
    for _ in range(int(input())):
        X, Y = list(map(int, input().split()))
        result = (result+(X_square_total-2*X_total*X+N*X**2))%MOD
        result = (result+(Y_square_total-2*Y_total*Y+N*Y**2))%MOD
    return result

MOD = 10**9+7
for case in range(int(input())):
    print('Case #%d: %s' % (case+1, watering_well_chapter_2()))
