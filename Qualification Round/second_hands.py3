# Copyright (c) 2021 kamyu. All rights reserved.
#
# Meta Hacker Cup 2022 Qualification Round - Problem A. Second Hands
# https://www.facebook.com/codingcompetitions/hacker-cup/2022/qualification-round/problems/A
#
# Time:  O(N)
# Space: O(N)
#

from collections import Counter

def second_hands():
    N, K = map(int, input().split())
    S = map(int, input().split())
    return "YES" if N <= 2*K and max(Counter(S).values()) <= 2 else "NO"

for case in range(int(input())):
    print('Case #%d: %s' % (case+1, second_hands()))
