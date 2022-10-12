# Copyright (c) 2022 kamyu. All rights reserved.
#
# Meta Hacker Cup 2022 Round 3 - Problem C. Second Mistake
# https://www.facebook.com/codingcompetitions/hacker-cup/2022/round-3/problems/C
#
# Time:  O(3 * L * (N + Q))
# Space: O(3 * L * N)
#

from collections import Counter
from functools import reduce

def add(a, b):
    return (a+b)%MOD

def mult(a, b):
    return (a*b)%MOD

def pow(i):
    while not (i < len(POW)):
        POW.append(mult(POW[-1], BASE))
    return POW[i]

def second_mistake():
    def find_diff_1_hashes(f):
        result = 0
        for _ in range(int(input())):
            V = input()
            h = reduce(lambda h, i: add(h, mult(LOOKUP[V[i]], pow(i))), range(len(V)), 0)
            result += sum(f(add(h, mult(LOOKUP[x]-LOOKUP[c], pow(i))), i) for i, c in enumerate(V) for x in LOOKUP.keys() if x != c)
        return result//2

    def f(h, i):
        cnt[h, i] += 1
        cnt[h] += 1
        return 0

    def g(h, i):
        return cnt[h]-cnt[h, i] if h in cnt else 0

    cnt = Counter()
    find_diff_1_hashes(f)
    return find_diff_1_hashes(g)

MOD = (1<<64)-59  # largest 64-bit prime
BASE = 113
POW = [1]
META = "meta"
LOOKUP = {x:i for i, x in enumerate(META)}
for case in range(int(input())):
    print('Case #%d: %s' % (case+1, second_mistake()))
