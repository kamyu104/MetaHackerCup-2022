# Copyright (c) 2022 kamyu. All rights reserved.
#
# Meta Hacker Cup 2022 Round 2 - Problem C. Balance Scale
# https://www.facebook.com/codingcompetitions/hacker-cup/2022/round-2/problems/C
#
# Time:  precompute: O(MAX_N * MAX_C)
#        runtime:    O(N)
# Space: precompute: O(MAX_N * MAX_C)
#        runtime:    O(1)
#

def add(a, b):
    return (a+b)%MOD

def sub(a, b):
    return (a-b)%MOD

def mult(a, b):
    return (a*b)%MOD

def lazy_init(n):
    while len(INV) <= n:
        FACT.append(FACT[-1]*len(INV) % MOD)
        INV.append(INV[MOD%len(INV)]*(MOD-MOD//len(INV)) % MOD)
        INV_FACT.append(INV_FACT[-1]*INV[-1] % MOD)

def nCr(n, k, inverse=False):
    if not (0 <= k <= n):
        return 0
    lazy_init(n)
    return (FACT[n]*INV_FACT[n-k] % MOD) * INV_FACT[k] % MOD if not inverse else (INV_FACT[n]*FACT[n-k] % MOD) * FACT[k] % MOD

def inv(n):
    lazy_init(n)
    return INV[n]

def balance_scale():
    N, K = map(int, input().split())
    K += 1
    C_W = [tuple(map(int, input().split())) for _ in range(N)]
    less = sum(c for c, w in C_W if w < C_W[0][1])
    equal = sum(c for c, w in C_W if w == C_W[0][1])
    total = sum(c for c, _ in C_W)
    return mult(mult(sub(nCr(less+equal, K), nCr(less, K)), mult(C_W[0][0], inv(equal))), nCr(total, K, True))

FACT, INV, INV_FACT = [[1]*2 for _ in range(3)]
MOD = 10**9+7
for case in range(int(input())):
    print('Case #%d: %s' % (case+1, balance_scale()))
