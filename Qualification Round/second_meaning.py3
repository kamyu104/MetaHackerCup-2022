# Copyright (c) 2021 kamyu. All rights reserved.
#
# Meta Hacker Cup 2022 Qualification Round - Problem C1. Second Meaning
# https://www.facebook.com/codingcompetitions/hacker-cup/2022/qualification-round/problems/C1
#
# Time:  O(N^2)
# Space: O(N)
#

def encode(n, x):
    code = ['-' if x == '.' else '.', x]
    result = [code[0]]*(n+1)
    result.append(code[1])
    return "".join(result)

def second_meaning():
    N = int(input())
    S = input()
    result = [encode(i, S[0]) for i in range(N-1)]
    return "\n%s" % "\n".join(result)

MAX_L = 8
for case in range(int(input())):
    print('Case #%d: %s' % (case+1, second_meaning()))
