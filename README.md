# [MetaHackerCup-2022](https://www.facebook.com/hackercup/past_rounds/) ![Language](https://img.shields.io/badge/language-Python3-orange.svg) [![License](https://img.shields.io/badge/license-MIT-blue.svg)](./LICENSE) ![Progress](https://img.shields.io/badge/progress-26%20%2F%2030-ff69b4.svg) ![Visitors](https://visitor-badge.laobi.icu/badge?page_id=kamyu104.metahackercup.2022)

Python3 solutions of Meta Hacker Cup 2022. Solution begins with `*` means it will get TLE in the largest data set (total computation amount > `10^8`, which is not friendly for Python3 to solve in 5 ~ 15 seconds). A `6-minute` timer is set for uploading the result this year.

* [Hacker Cup 2021](https://github.com/kamyu104/FacebookHackerCup-2021)
* [Qualification Round](https://github.com/kamyu104/MetaHackerCup-2022#qualification-round)
* [Round 1](https://github.com/kamyu104/MetaHackerCup-2022#round-1)
* [Round 2](https://github.com/kamyu104/MetaHackerCup-2022#round-2)
* [Round 3](https://github.com/kamyu104/MetaHackerCup-2022#round-3)
* [Final Round](https://github.com/kamyu104/MetaHackerCup-2022#final-round)
  
## Qualification Round
| # | Title | Solution | Time | Space | Difficulty | Tag | Note |
|---| ----- | -------- | ---- | ----- | ---------- | --- | ---- |
|A| [Second Hands](https://www.facebook.com/codingcompetitions/hacker-cup/2022/qualification-round/problems/A)| [Python3](./Qualification%20Round/second_hands.py3) | _O(N)_ | _O(N)_ | Easy | | Greedy |
|B1| [Second Friend](https://www.facebook.com/codingcompetitions/hacker-cup/2022/qualification-round/problems/B1)| [Python3](./Qualification%20Round/second_friend.py3) | _O(R * C)_ | _O(1)_ | Easy | | Constructive Algorithms |
|B2| [Second Second Friend](https://www.facebook.com/codingcompetitions/hacker-cup/2022/qualification-round/problems/B2)| [Python3](./Qualification%20Round/second_second_friend.py3) | _O(R * C)_ | _O(R * C)_ | Medium | | Constructive Algorithms, BFS |
|C1| [Second Meaning](https://www.facebook.com/codingcompetitions/hacker-cup/2022/qualification-round/problems/C1)| [Python3](./Qualification%20Round/second_meaning.py3) | _O(N^2)_ | _O(N)_ | Easy | | Constructive Algorithms |
|C2| [Second Second Meaning](https://www.facebook.com/codingcompetitions/hacker-cup/2022/qualification-round/problems/C2)| [Python3](./Qualification%20Round/second_second_meaning.py3) | _O(NlogN)_ | _O(logN)_ | Medium | | Constructive Algorithms |
|D| [Second Flight](https://www.facebook.com/codingcompetitions/hacker-cup/2022/qualification-round/problems/D)| [Python3](./Qualification%20Round/second_flight.py3) [Python3](./Qualification%20Round/second_flight2.py3) | _O(N + Q + M * min(sqrt(Q), N))_ | _O(N + M + Q)_ | Hard | | Graph, Memoization |

## Round 1
| # | Title | Solution | Time | Space | Difficulty | Tag | Note |
|---| ----- | -------- | ---- | ----- | ---------- | --- | ---- |
|A1| [Consecutive Cuts - Chapter 1](https://www.facebook.com/codingcompetitions/hacker-cup/2022/round-1/problems/A1)| [Python3](./Round%201/consecutive_cuts_chapter_1.py3) | _O(N)_ | _O(1)_ | Easy | | Constructive Algorithms, String |
|A2| [Consecutive Cuts - Chapter 2](https://www.facebook.com/codingcompetitions/hacker-cup/2022/round-1/problems/A2)| [Python3](./Round%201/consecutive_cuts_chapter_2.py3) [Python3](./Round%201/consecutive_cuts_chapter_2-2.py3) [Python3](./Round%201/consecutive_cuts_chapter_2-3.py3) | _O(N)_ | _O(1)_ | Medium | | Constructive Algorithms, String, KMP Algorithm, Z-Function, Rabin-Karp Algorithm, Rolling Hash |
|B1| [Watering Well - Chapter 1](https://www.facebook.com/codingcompetitions/hacker-cup/2022/round-1/problems/B1)| [Python3](./Round%201/watering_well_chapter_1.py3) | _O(N + Q + min(N * Q, MAX_A_B_X_Y^2))_ | _O(min(N + Q, MAX_A_B_X_Y))_ | Easy | | Math, Freq Table |
|B2| [Watering Well - Chapter 2](https://www.facebook.com/codingcompetitions/hacker-cup/2022/round-1/problems/B2)| [Python3](./Round%201/watering_well_chapter_2.py3) | _O(N + Q)_ | _O(1)_ | Easy | | Math |
|C| [Lemonade Life](https://www.facebook.com/codingcompetitions/hacker-cup/2022/round-1/problems/C)| [PyPy3](./Round%201/lemonade_life.py3) | _O(NlogN + V^2)_ | _O(N + V)_ | Hard | | Geometry, Convex Hull, Monotone Chain Algorithm, Graph, Dijkstra's Algorithm |

## Round 2
| # | Title | Solution | Time | Space | Difficulty | Tag | Note |
|---| ----- | -------- | ---- | ----- | ---------- | --- | ---- |
|A1| [Perfectly Balanced - Chapter 1](https://www.facebook.com/codingcompetitions/hacker-cup/2022/round-2/problems/A1)| [Python3](./Round%202/perfectly_balanced_chapter_1.py3) | _O(N + Q)_ | _O(N)_ | Easy | | Prefix Sum |
|A2| [Perfectly Balanced - Chapter 2](https://www.facebook.com/codingcompetitions/hacker-cup/2022/round-2/problems/A2)| [Python3](./Round%202/perfectly_balanced_chapter_2.py3) | _O((N + Q) * logN)_ | _O(N)_ | Medium | | Hash, BIT, Fenwick Tree |
|B| [Balance Sheet](https://www.facebook.com/codingcompetitions/hacker-cup/2022/round-2/problems/B)| [Python3](./Round%202/balance_sheet.py3) | _O(NlogN + N * K)_ | _O(N * K)_ | Medium | | Sort, Greedy, DP |
|C| [Balance Scale](https://www.facebook.com/codingcompetitions/hacker-cup/2022/round-2/problems/C)| [Python3](./Round%202/balance_scale.py3) | precompute: _O(MAX\_N * MAX\_C)_<br>runtime: _O(N)_ | precompute: _O(MAX\_N * MAX\_C)_<br>runtime: _O(1)_ | Easy | | Combinatorics, Probability |
|D1| [Work-Life Balance - Chapter 1](https://www.facebook.com/codingcompetitions/hacker-cup/2022/round-2/problems/D1)| [Python3](./Round%202/work_life_balance_chapter_1.py3) | _O((N + M) * logN)_ | _O(N)_ | Medium | | BIT, Fenwick Tree, Greedy |
|D2| [Work-Life Balance - Chapter 2](https://www.facebook.com/codingcompetitions/hacker-cup/2022/round-2/problems/D2)| [Python3](./Round%202/work_life_balance_chapter_2.py3) | _O((N + M) * logN)_ | _O(N)_ | Hard | | BIT, Fenwick Tree, Greedy |

## Round 3
| # | Title | Solution | Time | Space | Difficulty | Tag | Note |
|---| ----- | -------- | ---- | ----- | ---------- | --- | ---- |
|A| [Fourth Player](https://www.facebook.com/codingcompetitions/hacker-cup/2022/round-3/problems/A)| [Python3](./Round%203/fourth_player.py3) | _O(NlogN)_ | _O(N)_ | Medium | | Games, Greedy |
|B| [Third Trie](https://www.facebook.com/codingcompetitions/hacker-cup/2022/round-3/problems/B)| [Python3](./Round%203/third_trie.py3) | _O(N * M)_ | _O(T)_ | Easy | | Trie, Combinatorics |
|C| [Second Mistake](https://www.facebook.com/codingcompetitions/hacker-cup/2022/round-3/problems/C)| [Python3](./Round%203/second_mistake.py3) | _O(3 * L * (N + Q))_ | _O(3 * L * N)_ | Easy | | Rabin-Karp Algorithm, Hash Table |
|D1| [First Time - Chapter 1](https://www.facebook.com/codingcompetitions/hacker-cup/2022/round-3/problems/D1)| [Python3](./Round%203/first_time_chapter_1.py3) | _O(M + NlogN)_ | _O(N)_ | Medium | | Unordered Set |
|D2| [First Time - Chapter 2](https://www.facebook.com/codingcompetitions/hacker-cup/2022/round-3/problems/D2)| [Python3](./Round%203/first_time_chapter_2.py3) | _O(M + NlogN)_ | _O(N)_ | Hard | | Unordered Set, Segment Tree, Number Theory |
|E1| [Zero Crossings - Chapter 1](https://www.facebook.com/codingcompetitions/hacker-cup/2022/round-3/problems/E1)| [Python3](./Round%203/zero_crossings_chapter_1.py3) [Python3](./Round%203/zero_crossings_chapter_1_2.py3) | _O((N * M + Q) * log(N * M + Q))_ | _O(N * M + Q)_ | Hard | | Offline Solution, Geometry, Sort, Line Sweep, Treap, Sorted List, Binary Search, Tree, DFS, Hash |
|E2| [Zero Crossings - Chapter 2](https://www.facebook.com/codingcompetitions/hacker-cup/2022/round-3/problems/E2)| [PyPy3](./Round%203/zero_crossings_chapter_2.py3) | _O((N * M) * log(N * M) + Q * log(N * M))_ | _O((N * M) * log(N * M)_ | Hard | | Online Solution, Geometry, Sort, Line Sweep, Persistent Treap, Binary Search, Tree, DFS, Hash |

## Final Round
| # | Title | Solution | Time | Space | Difficulty | Tag | Note |
|---| ----- | -------- | ---- | ----- | ---------- | --- | ---- |
|A| [ML Modeling](https://www.facebook.com/codingcompetitions/hacker-cup/2022/final-round/problems/A)| [PyPy3](./Final%20Round/ml_modeling.py3) | _O(MAX_X * MAX_Y * MAX_R * MIN_N + (MAX_X * MAX_Y)^2 + N)_ | _O(MAX_X * MAX_Y)_ | Medium | | Geometry |
|B| [Emerald Exhibiting](https://www.facebook.com/codingcompetitions/hacker-cup/2022/final-round/problems/B)| [PyPy3](./Final%20Round/emerald_exhibiting.py3) | _O(P * log(logN))_ | _O(P)_ | Medium | | Combinatorics, Number Theory |
|C| [Tile Transposing](https://www.facebook.com/codingcompetitions/hacker-cup/2022/final-round/problems/C)| | | | Hard | | |
|D| [Alphabet Adventuring](https://www.facebook.com/codingcompetitions/hacker-cup/2022/final-round/problems/D)| | | | Hard | | |
|E| [Hazelnut Harvesting](https://www.facebook.com/codingcompetitions/hacker-cup/2022/final-round/problems/E)| | | | Hard | | |
|F| [Cup Counterbalancing](https://www.facebook.com/codingcompetitions/hacker-cup/2022/final-round/problems/F)| | | | Very Hard | | |