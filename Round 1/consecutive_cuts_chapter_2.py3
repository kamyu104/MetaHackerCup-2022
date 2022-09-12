# Copyright (c) 2022 kamyu. All rights reserved.
#
# Meta Hacker Cup 2022 Qualification Round - Problem A2. Consecutive Cuts - Chapter 2
# https://www.facebook.com/codingcompetitions/hacker-cup/2022/round-1/problems/A2
#
# Time:  O(N)
# Space: O(N)
#
# kmp solution
#

def getPrefix(pattern):
    prefix = [-1]*len(pattern)
    j = -1
    for i in range(1, len(pattern)):
        while j+1 > 0 and pattern[j+1] != pattern[i]:
            j = prefix[j]
        if pattern[j+1] == pattern[i]:
            j += 1
        prefix[i] = j
    return prefix

def KMP(text, pattern, start):
    prefix = getPrefix(pattern)
    j = -1
    for i in range(start, len(text)):
        while j+1 > 0 and pattern[j+1] != text[i]:
            j = prefix[j]
        if pattern[j+1] == text[i]:
            j += 1
        if j+1 == len(pattern):
            yield i-j
            j = prefix[j]

def consecutive_cuts_chapter_2():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    it = KMP(A+A, B, 0)
    while True:
        i = next(it, -1)
        if i == -1 or i >= N:
            break
        if (N == 2 and K%2 == int(i != 0)) or (N > 2 and K != int(i == 0)):
            return "YES"
        if K == 0:
            break
    return "NO"

for case in range(int(input())):
    print('Case #%d: %s' % (case+1, consecutive_cuts_chapter_2()))
