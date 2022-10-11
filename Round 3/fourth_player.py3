# Copyright (c) 2022 kamyu. All rights reserved.
#
# Meta Hacker Cup 2022 Round 3 - Problem A. Fourth Player
# https://www.facebook.com/codingcompetitions/hacker-cup/2022/round-3/problems/A
#
# Time:  O(NlogN)
# Space: O(N)
#
    
def fourth_player():
    N = int(input())
    A, B = [], []
    for i in range(4):
        C = list(map(int, input().split()))
        C.sort()
        if i == 0:
            new_A, new_B = C, []
        else:
            new_A, new_B = [], []
            for x in reversed(B):
                if C and C[-1] > x:
                    new_A.append(C.pop())
                else:
                    new_B.append(x)
            for x in A:
                if C and C[-1] > x:
                    new_A.append(C.pop())
                else:
                    new_A.append(x)
            new_A.sort()
            new_B.sort()
        B, A = new_A, new_B
    return len(A)

for case in range(int(input())):
    print('Case #%d: %s' % (case+1, fourth_player()))
