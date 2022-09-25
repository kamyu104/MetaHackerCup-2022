# Copyright (c) 2022 kamyu. All rights reserved.
#
# Meta Hacker Cup 2022 Round 2 - Problem D2. Work-Life Balance - Chapter 2
# https://www.facebook.com/codingcompetitions/hacker-cup/2022/round-2/problems/D2
#
# Time:  O((N + M) * logN)
# Space: O(N)
#

# Template:
# https://github.com/kamyu104/FacebookHackerCup-2021/blob/main/Round%203/expl_ore_ation_chapter_3-2.py
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

    def kth_element(self, k):
        floor_log2_n = (len(self.__bit)-1).bit_length()-1
        pow_i = 2**floor_log2_n
        total = pos = 0  # 1-indexed
        for _ in reversed(range(floor_log2_n+1)):  # O(logN)
            if pos+pow_i < len(self.__bit) and total+self.__bit[pos+pow_i] < k:  # find max pos s.t. total < k
                total += self.__bit[pos+pow_i]
                pos += pow_i
            pow_i >>= 1
        return (pos+1)-1  # 0-indexed, return min pos s.t. total >= k if pos exists else n

def work_life_balance_chapter_2():
    def query(Z):
        left = [bits[i].query(Z) for i in range(2)]
        right = [bits[i].query(N-1)-left[i] for i in range(2)]
        diff = sum((i+1)*right[i] for i in range(2))-sum((i+1)*left[i] for i in range(2))
        if diff == 0:
            return 0
        if diff%2:
            return -1
        diff //= 2
        x, y = 0, 1
        if diff < 0:
            diff = -diff
            x, y = y, x
        if left[x] < diff or right[y] < diff:
            return -1
        l = bits[x].kth_element(left[x]-diff)
        r = bits[y].kth_element(left[y]+diff)
        return (bits2[y].query(r)-bits2[y].query(Z)) - (bits2[x].query(Z)-bits2[x].query(l))

    N, M = map(int, input().split())
    A = list(map(lambda x: int(x)-1, input().split()))
    bits = [BIT(N) for _ in range(2)]
    bits2 = [BIT(N) for _ in range(2)]
    for i, x in enumerate(A):
        bits[x].add(i, 1)
        bits2[x].add(i, i)
    result = 0
    for _ in range(M):
        X, Y, Z = map(lambda x: int(x)-1, input().split())
        bits[A[X]].add(X, -1)
        bits2[A[X]].add(X, -X)
        A[X] = Y
        bits[A[X]].add(X, 1)
        bits2[A[X]].add(X, X)
        result += query(Z)
    return result

INF = float("inf")
for case in range(int(input())):
    print('Case #%d: %s' % (case+1, work_life_balance_chapter_2()))
