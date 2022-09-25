# Copyright (c) 2022 kamyu. All rights reserved.
#
# Meta Hacker Cup 2022 Round 2 - Problem A1. Perfectly Balanced - Chapter 2
# https://www.facebook.com/codingcompetitions/hacker-cup/2022/round-2/problems/A2
#
# Time:  O((N + Q) * logN)
# Space: O(N)
#

from random import seed, randint

def add(a, b):
    return (a+b)%MOD

def sub(a, b):
    return (a-b)%MOD

class BIT(object):  # 0-indexed.
    def __init__(self, n):
        self.__bit = [0]*(n+1)  # Extra one for dummy node.

    def add(self, i, val):
        i += 1  # Extra one for dummy node.
        while i < len(self.__bit):
            self.__bit[i] = add(self.__bit[i], val)  # modified
            i += (i & -i)

    def query(self, i):
        i += 1  # Extra one for dummy node.
        ret = 0
        while i > 0:
            ret = add(ret, self.__bit[i])  # modified
            i -= (i & -i)
        return ret

def hash(lookup, h_set, x):
    if x not in lookup:
        lookup[x] = randint(0, MOD-1)
        h_set.add(lookup[x])
    return lookup[x]

def perfectly_balanced_chapter_2():
    N = int(input())
    A = list(map(int, input().split()))
    lookup, h_set = {}, set()
    bit = BIT(len(A))
    for i, x in enumerate(A):
        bit.add(i, hash(lookup, h_set, x))
    result = 0
    for _ in range(int(input())):
        args = list(map(int, input().split()))
        if args[0] == 1:
            _, X, Y = args
            X -= 1
            bit.add(X, -hash(lookup, h_set, A[X]))
            A[X] = Y
            bit.add(X, hash(lookup, h_set, A[X]))
            continue
        _, L, R = args
        L -= 1
        R -= 1
        if (R-L+1)%2 == 0:
            continue
        h1 = sub(bit.query((L+R)//2), bit.query(L-1))
        h2 = sub(bit.query(R), bit.query((L+R)//2))
        if sub(h1, h2) in h_set:
            result += 1
            continue
        h1 = sub(bit.query((L+R)//2-1), bit.query(L-1))
        h2 = sub(bit.query(R), bit.query((L+R)//2-1))
        if sub(h2, h1) in h_set:
            result += 1
            continue
    return result

seed(0)
MOD = (1<<64)-59  # max 64-bit prime
for case in range(int(input())):
    print('Case #%d: %s' % (case+1, perfectly_balanced_chapter_2()))
