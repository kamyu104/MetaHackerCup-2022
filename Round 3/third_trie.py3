# Copyright (c) 2022 kamyu. All rights reserved.
#
# Meta Hacker Cup 2022 Round 3 - Problem B. Third Trie
# https://www.facebook.com/codingcompetitions/hacker-cup/2022/round-3/problems/B
#
# Time:  O(N * M)
# Space: O(T), T is the size of the merged trie
#

def nC3(n):
    return n*(n-1)*(n-2)//6

def fourth_player():
    def create_node():
        trie.append([0]*26)
        cnt.append(0)
        return len(trie)-1

    N = int(input())
    trie = [[0]*26]
    cnt = [0]
    for _ in range(N):
        M = int(input())
        lookup = [0]
        cnt[lookup[-1]] += 1
        for _ in range(M-1):
            P, C = input().split()
            P = int(P)
            if not trie[lookup[P-1]][ord(C)-ord('a')]:
                trie[lookup[P-1]][ord(C)-ord('a')] = create_node()
            lookup.append(trie[lookup[P-1]][ord(C)-ord('a')])
            cnt[lookup[-1]] += 1
    return sum(nC3(N)-nC3(N-c) for c in cnt)

for case in range(int(input())):
    print('Case #%d: %s' % (case+1, fourth_player()))
