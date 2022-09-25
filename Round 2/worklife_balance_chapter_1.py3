# Copyright (c) 2022 kamyu. All rights reserved.
#
# Meta Hacker Cup 2022 Round 2 - Problem A1. Perfectly Balanced - Chapter 1
# https://www.facebook.com/codingcompetitions/hacker-cup/2022/round-2/problems/A1
#
# Time:  O((N + M) * logN)
# Space: O(N)
#

def ceil_divide(a, b):
    return (a+b-1)//b

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

def case1(left, right, diff):
    total = 0
    cnt = min(left[0], right[2], diff//4)
    swap(left, right, 0, 2, cnt)
    diff -= cnt*4
    total += cnt
    cnt = min(left[0], right[1], diff//2)
    swap(left, right, 0, 1, cnt)
    diff -= cnt*2
    total += cnt
    cnt = min(left[1], right[2], diff//2)
    swap(left, right, 1, 2, cnt)
    diff -= cnt*2
    total += cnt
    return total if diff == 0 else INF

def case2(left, right, diff):
    total = 0
    cnt = min(left[0], right[2], ceil_divide(diff, 4))
    swap(left, right, 0, 2, cnt)
    diff -= cnt*4
    total += cnt
    cnt = min(left[1], right[0], (-diff)//2 if diff < 0 else 0)
    swap(left, right, 1, 0, cnt)
    diff += cnt*2
    total += cnt
    cnt = min(left[2], right[1], (-diff)//2 if diff < 0 else 0)
    swap(left, right, 2, 1, cnt)
    diff += cnt*2
    total += cnt
    return total if diff == 0 else INF

def worklife_balance_chapter_1():
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
        bits[A[X]].add(X, +1)
        left = [bits[i].query(Z) for i in range(3)]
        right = [bits[i].query(N-1)-left[i] for i in range(3)]
        total_left = sum((i+1)*left[i] for i in range(3))
        total_right = sum((i+1)*right[i] for i in range(3))
        if total_left > total_right:
            left, right = right, left
            total_left, total_right = total_right, total_left
        Q = min(case1(left, right, total_right-total_left), case2(left, right, total_right-total_left))
        result += Q if Q != INF else -1
    return result

INF = float("inf")
for case in range(int(input())):
    print('Case #%d: %s' % (case+1, worklife_balance_chapter_1()))
