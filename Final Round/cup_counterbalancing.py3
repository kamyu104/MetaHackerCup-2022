# Copyright (c) 2022 kamyu. All rights reserved.
#
# Meta Hacker Cup 2022 Final Round - Problem F. Cup Counterbalancing
# https://www.facebook.com/codingcompetitions/hacker-cup/2022/final-round/problems/F
#
# Time:  O(N * S), pass in PyPy3 but Python3
# Space: O(N)
#

from random import random, seed
from math import atan2, pi, cos, sin

def inner_product(a, b):
    return a[0]*b[0]+a[1]*b[1]

def add(a, b):
    return [a[0]+b[0], a[1]+b[1]]

def sub(a, b):
    return [a[0]-b[0], a[1]-b[1]]

def mult(a, v):
    return [a[0]*v, a[1]*v]

def div(a, v):
    return [a[0]/v, a[1]/v]

def rotate(a, d):
    return [a[0]*cos(d)+a[1]*cos(pi/2+d), a[0]*sin(d)+a[1]*sin(pi/2+d)]

def length_square(a):
    return a[0]*a[0]+a[1]*a[1]

def length(a):
    return (a[0]*a[0]+a[1]*a[1])**0.5

def angle(x):
    return atan2(x[1], x[0])

def inside_colinear_segment(s, p):
    return inner_product(sub(p, s[0]), sub(p, s[1])) <= 0

def segment(a, b):
    d = sub(b, a)
    return ((a, b), div(d, length(d)))

def intersection(s, u, p, R_square):
    closet = add(s[0], mult(u, inner_product(sub(p, s[0]), u)))
    d_square = length_square(sub(closet, p))
    result = []
    if d_square <= R_square:
        l = (R_square-d_square)**0.5
        if l == 0:
            if inside_colinear_segment(s, closet):
                result.append(closet)
        else:
            p1 = add(closet, mult(u, l))
            if inside_colinear_segment(s, p1):
                result.append(p1)
            p2 = add(closet, mult(u, -l))
            if inside_colinear_segment(s, p2):
                result.append(p2)
    return result

def cup_counterbalancing():  # Time: O(N)
    def check(p, R_square):
        angles = [angle(sub(x, p)) for s, u in segments for x in intersection(s, u, p, R_square)]
        a, b = [], []
        mn_a = mn_b = pi
        mx_a = mx_b = -pi
        for x in angles:  # write verbosely to speed up performance
            if x < 0:
                if x < mn_a:
                    mn_a = x
                if x > mx_a:
                    mx_a = x
                a.append(x)
            else:
                if x < mn_b:
                    mn_b = x
                if x > mx_b:
                    mx_b = x
                b.append(x)
        return len(a) > 0 and len(b) > 0 and mn_b < mx_a+pi and mn_a+pi < mx_b

    N, R, L = map(int, input().split())
    R_square = R**2
    points = [list(map(int, input().split())) for _ in range(N)]
    segments = [segment(points[i], points[(i+1)%len(points)]) for i in range(len(points))]
    u = mult(rotate((1, 0), random()*pi/4), L/SAMPLE**0.5)
    v = [-u[1], u[0]]
    total = good = 0
    for idx, j, d in ((0, 0, 1), (1, -1, -1)):
        start = [0, 0]
        found = True
        while found:
            found = False
            i = 0
            curr = start
            while curr[0] <= L and curr[1] <= L:
                if 0 <= curr[idx]:
                    found = True
                    if check(curr, R_square):
                        good += 1
                    total += 1
                i += 1
                curr = add(start, mult(u, i))
            j += d
            start = mult(v, j)
    return good/total

seed(0)
SAMPLE = 10**8
for case in range(int(input())):
    print('Case #%d: %s' % (case+1, cup_counterbalancing()))
