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
    A_square_total = A_total = B_square_total = B_total = 0
    for _ in range(N):
        A, B = list(map(int, input().split()))
        A_total, A_square_total = (A_total+A)%MOD, (A_square_total+A**2)%MOD
        B_total, B_square_total = (B_total+B)%MOD, (B_square_total+B**2)%MOD
    result = 0
    for _ in range(int(input())):
        X, Y = list(map(int, input().split()))
        result = (result+(N*X**2-2*A_total*X+A_square_total))%MOD
        result = (result+(N*Y**2-2*B_total*Y+B_square_total))%MOD
    return result

MOD = 10**9+7
for case in range(int(input())):
    print('Case #%d: %s' % (case+1, watering_well_chapter_2()))
