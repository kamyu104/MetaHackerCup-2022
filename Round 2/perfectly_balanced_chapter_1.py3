# Copyright (c) 2022 kamyu. All rights reserved.
#
# Meta Hacker Cup 2022 Round 2 - Problem A1. Perfectly Balanced - Chapter 1
# https://www.facebook.com/codingcompetitions/hacker-cup/2022/round-2/problems/A1
#
# Time:  O(N + Q)
# Space: O(N)
#

def perfectly_balanced_chapter_1():
    S = input()
    prefix = [[0]*26]
    for c in S:
        prefix.append(prefix[-1][:])
        prefix[-1][ord(c)-ord('a')] += 1
    result = 0
    for _ in range(int(input())):
        L, R = map(int, input().split())
        L -= 1
        R -= 1
        if (R-L+1)%2 == 0:
            continue
        cnt1 = [prefix[(L+R)//2+1][i]-prefix[L][i] for i in range(26)]
        cnt2 = [prefix[R+1][i]-prefix[(L+R)//2+1][i] for i in range(26)]
        if sum(abs(cnt1[i]-cnt2[i]) for i in range(26)) == 1:
            result += 1
            continue
        cnt1 = [prefix[(L+R)//2][i]-prefix[L][i] for i in range(26)]
        cnt2 = [prefix[R+1][i]-prefix[(L+R)//2][i] for i in range(26)]
        if sum(abs(cnt2[i]-cnt1[i]) for i in range(26)) == 1:
            result += 1
            continue
    return result

for case in range(int(input())):
    print('Case #%d: %s' % (case+1, perfectly_balanced_chapter_1()))
