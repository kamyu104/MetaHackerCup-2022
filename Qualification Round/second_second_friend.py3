# Copyright (c) 2022 kamyu. All rights reserved.
#
# Meta Hacker Cup 2022 Qualification Round - Problem B1. Second Second Friend
# https://www.facebook.com/codingcompetitions/hacker-cup/2022/qualification-round/problems/B2
#
# Time:  O(R * C)
# Space: O(R * C)
#

def count(grid, r, c):
    cnt = 0
    for dr, dc in DIRECTIONS:
        nr, nc = r+dr, c+dc
        if not (0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] != '#'):
            continue
        cnt += 1
    return cnt

def second_second_friend():
    R, C = map(int, input().split())
    grid = [list(input()) for _ in range(R)]
    lookup = [[False]*len(grid[0]) for _ in range(len(grid))]
    cnt = [[0]*len(grid[0]) for _ in range(len(grid))]
    q = []
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == '#':
                continue
            if grid[r][c] == '^':
                lookup[r][c] = True
            else:
                grid[r][c] = '^'
            cnt[r][c] = count(grid, r, c)
            if cnt[r][c] > 1:
                continue
            cnt[r][c] = 0
            q.append((r, c))
    while q:
        new_q = []
        for r, c in q:
            if lookup[r][c]:
                return "Impossible"
            grid[r][c] = '.'
            for dr, dc in DIRECTIONS:
                nr, nc = r+dr, c+dc
                if not (0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and cnt[nr][nc]):
                    continue
                cnt[nr][nc] -= 1
                if cnt[nr][nc] > 1:
                   continue
                cnt[nr][nc] = 0
                new_q.append((nr, nc))
        q = new_q
    return "Possible\n%s" % "\n".join(map(lambda x: "".join(x), grid))

DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]
for case in range(int(input())):
    print('Case #%d: %s' % (case+1, second_second_friend()))
