# Copyright (c) 2022 kamyu. All rights reserved.
#
# Meta Hacker Cup 2022 Qualification Round - Problem B1. Second Friend
# https://www.facebook.com/codingcompetitions/hacker-cup/2022/qualification-round/problems/B1
#
# Time:  O(R * C)
# Space: O(1)
#

def second_friend():
    R, C = map(int, input().split())
    grid = [list(input()) for _ in range(R)]
    if  min(R, C) == 1 and any(x == '^' for row in grid for x in row):
        return "Impossible"
    c = '.' if min(R, C) == 1 else '^'
    result = (c*C for _ in range(R))
    return "Possible\n%s" % "\n".join(result)

for case in range(int(input())):
    print('Case #%d: %s' % (case+1, second_friend()))
