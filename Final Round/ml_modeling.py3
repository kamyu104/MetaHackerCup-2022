# Copyright (c) 2022 kamyu. All rights reserved.
#
# Meta Hacker Cup 2022 Final Round - Problem A. ML Modeling
# https://www.facebook.com/codingcompetitions/hacker-cup/2022/final-round/problems/A
#
# Time:  O(MAX_X * MAX_Y * MAX_R * MIN_N + (MAX_X * MAX_Y)^2 + N), pass in PyPy3 but Python3
# Space: O(MAX_X * MAX_Y)
#

from math import atan2

def check(P, x, y, r):
    return all((P[i][0]-x)**2 + (P[i][1]-y)**2 <= r**2 for i in range(MIN_N))

def overlapped_area(ax, ay, bx, by, r):
    d = ((ax-bx)**2+(ay-by)**2)**0.5
    h = (r**2-(d/2)**2)**0.5
    return 2*(r**2 * atan2(h, d/2))-h*d

def total_distance_square(P, x, y):
    return sum((p[0]-x)**2+(p[1]-y)**2 for p in P)

def ml_modeling():
    N = int(input())
    P = [list(map(float, input().split())) for _ in range(N)]
    candidates = []
    for x in range(MIN_X_Y, MAX_X_Y_R+1):
        for y in range(MIN_X_Y, MAX_X_Y_R+1):
            for r in range(MIN_R, MAX_X_Y_R):
                if check(P, x, y, r):
                    candidates.append((x, y, r))
                    break
    mn = (float("inf"), -1, -1, -1, -1, -1)
    for i in range(len(candidates)):
        ax, ay, ar = candidates[i]
        for j in range(i+1, len(candidates)):
            bx, by, br = candidates[j]
            if br != ar:
                continue
            r = ar
            if (ax-bx)**2+(ay-by)**2 >= (2*r)**2:
                continue
            mn = min(mn, (overlapped_area(ax, ay, bx, by, r), ax, ay, bx, by, r))
    _, ax, ay, bx, by, r = mn
    if total_distance_square(P, ax, ay) > total_distance_square(P, bx, by):
        ax, ay, bx, by = bx, by, ax, ay
    return f"{ax} {ay} {bx} {by} {r}"

MIN_N = 500
MIN_X_Y = 0
MIN_R = 1
MAX_X_Y_R = 50
for case in range(int(input())):
    print('Case #%d: %s' % (case+1, ml_modeling()))
