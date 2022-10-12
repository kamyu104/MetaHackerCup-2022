# Copyright (c) 2022 kamyu. All rights reserved.
#
# Meta Hacker Cup 2022 Round 3 - Problem C. Second Mistake
# https://www.facebook.com/codingcompetitions/hacker-cup/2022/round-3/problems/C
#
# Time:  O(3 * L * (N + Q))
# Space: O(3 * L * Q)
#

from collections import Counter

def add(a, b):
    return (a+b)%MOD

def sub(a, b):
    return (a-b)%MOD

def mult(a, b):
    return (a*b)%MOD

def pow(i):
    while not (i < len(POW)):
        POW.append(mult(POW[-1], BASE))
    return POW[i]

def second_mistake():
    def find_diff_1_hashes(f):
        for _ in range(int(input())):
            V = input()
            h = 0
            for i, c in enumerate(V):
                c = ord(c)-ord('a')
                h = add(h, mult(c, pow(i)))
            for i, c in enumerate(V):
                c = ord(c)-ord('a')
                for x in META:
                    x = ord(x)-ord('a')
                    if x == c:
                        continue
                    nh = add(sub(h, mult(c, pow(i))), mult(x, pow(i)))
                    f(nh, i)

    def f(nh, i):
        cnt[nh, i] += 1
        cnt[nh] += 1

    def g(nh, i):
        result[0] += cnt[nh]-cnt[nh, i]

    cnt = Counter()
    find_diff_1_hashes(f)
    result = [0]
    find_diff_1_hashes(g)
    return result[0]//2

MOD = (1<<64)-59  # largest 64-bit prime
BASE = 113
POW = [1]
META = "meta"
for case in range(int(input())):
    print('Case #%d: %s' % (case+1, second_mistake()))
