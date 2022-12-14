# Copyright (c) 2022 kamyu. All rights reserved.
#
# Meta Hacker Cup 2022 Round 2 - Problem D1. Work-Life Balance - Chapter 1
# https://www.facebook.com/codingcompetitions/hacker-cup/2022/round-2/problems/D1
#
# Time:  O((N + M) * logN)
# Space: O(N)
#

class BIT(object):  # 0-indexed.
    def __init__(self, n):
        self.__bit = [0]*(n+1)  # Extra one for dummy node.

    def add(self, i, val):
        i += 1  # Extra one for dummy node.
        while i < len(self.__bit):
            self.__bit[i] += val
            i += (i & -i)

    def query(self, i):
        i += 1  # Extra one for dummy node.
        ret = 0
        while i > 0:
            ret += self.__bit[i]
            i -= (i & -i)
        return ret

def swap(left, right, x, y, cnt):
    left[x] -= cnt
    right[x] += cnt
    right[y] -= cnt
    left[y] += cnt

def update(total, diff, left, right, x, y):
    cnt = min(left[x], right[y], diff//(y-x))
    swap(left, right, x, y, cnt)
    diff -= cnt*(y-x)
    total += cnt
    return total, diff

def work_life_balance_chapter_1():
    def query(Z):
        left = [bits[i].query(Z) for i in range(3)]
        right = [bits[i].query(N-1)-left[i] for i in range(3)]
        diff = sum((i+1)*right[i] for i in range(3))-sum((i+1)*left[i] for i in range(3))
        if diff == 0:
            return 0
        if diff%2:
            return -1
        diff //= 2
        if diff < 0:
            diff = -diff
            left, right = right, left
        total, diff = update(0, diff, left, right, 0, 2)
        total, diff = update(total, diff, left, right, 0, 1)
        total, diff = update(total, diff, left, right, 1, 2)
        return total if diff == 0 else -1

    N, M = map(int, input().split())
    A = list(map(lambda x: int(x)-1, input().split()))
    bits = [BIT(N) for _ in range(3)]
    for i, x in enumerate(A):
        bits[x].add(i, 1)
    result = 0
    for _ in range(M):
        X, Y, Z = map(lambda x: int(x)-1, input().split())
        bits[A[X]].add(X, -1)
        A[X] = Y
        bits[A[X]].add(X, 1)
        result += query(Z)
    return result

INF = float("inf")
for case in range(int(input())):
    print('Case #%d: %s' % (case+1, work_life_balance_chapter_1()))
