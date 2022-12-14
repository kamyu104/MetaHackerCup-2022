# Copyright (c) 2022 kamyu. All rights reserved.
#
# Meta Hacker Cup 2022 Final Round - Problem B. Emerald Exhibiting
# https://www.facebook.com/codingcompetitions/hacker-cup/2022/final-round/problems/B
#
# Time:  O(P * log(logN)), pass in PyPy3 but Python3
# Space: O(P)
#

def linear_sieve_of_eratosthenes(n):
    primes = []
    spf = [-1]*(n+1)  # the smallest prime factor
    for i in range(2, n+1):
        if spf[i] == -1:
            spf[i] = i
            primes.append(i)
        for p in primes:
            if i*p > n or p > spf[i]:
                break
            spf[i*p] = p
    return primes

def count(n, p):
    result = 0
    while n//p:
        result += n//p
        n //= p
    return result

def emerald_exhibiting():
    N, K = map(int, input().split())
    if N == K:
        return 1
    is_one = is_two = is_three = True
    is_two_even_cnt = False
    total = 1
    for p in PRIMES:
        if p > N-1:
            break
        k = (count(N-1, p)-count(K, p))%2
        if k%2:
            is_one = False
        if p%4 == 3 and k%2:  # reference: https://en.wikipedia.org/wiki/Sum_of_two_squares_theorem
            is_two = False
        if p == 2:
            if not k%2:
                is_two_even_cnt = True
        else:
            total = (total * pow(p, k, 8))%8
    if is_two_even_cnt and total == 7:  # 4^a(8b+7), reference: https://en.wikipedia.org/wiki/Legendre%27s_three-square_theorem
        is_three = False
    return 1 if is_one else 2 if is_two else 3 if is_three else 4  # reference: https://en.wikipedia.org/wiki/Lagrange%27s_four-square_theorem

MAX_N = 10**9
PRIMES = linear_sieve_of_eratosthenes(MAX_N-1)
for case in range(int(input())):
    print('Case #%d: %s' % (case+1, emerald_exhibiting()))
