# Copyright (c) 2022 kamyu. All rights reserved.
#
# Meta Hacker Cup 2022 Round 1 - Problem A1. Consecutive Cuts - Chapter 1
# https://www.facebook.com/codingcompetitions/hacker-cup/2022/round-1/problems/A1
#
# Time:  O(N)
# Space: O(1)
#

def check(A, B, i):
    return all(A[(i+j)%len(A)] == B[j]for j in range(len(A)))

def consecutive_cuts_chapter_1():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    i = next((i for i, x in enumerate(A) if x ==(B[0])), -1)
    if i != -1 and check(A, B, i):
        if (N == 2 and K%2 == int(i != 0)) or (N > 2 and K != int(i == 0)):
            return "YES"
    return "NO"

for case in range(int(input())):
    print('Case #%d: %s' % (case+1, consecutive_cuts_chapter_1()))
