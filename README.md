# [MetaHackerCup-2022](https://www.facebook.com/hackercup/past_rounds/) ![Language](https://img.shields.io/badge/language-Python3-orange.svg) [![License](https://img.shields.io/badge/license-MIT-blue.svg)](./LICENSE) ![Progress](https://img.shields.io/badge/progress-11%20%2F%2011-ff69b4.svg) ![Visitors](https://visitor-badge.laobi.icu/badge?page_id=kamyu104.metahackercup.2022)

Python3 solutions of Meta Hacker Cup 2022. Solution begins with `*` means it will get TLE in the largest data set (total computation amount > `10^8`, which is not friendly for Python3 to solve in 5 ~ 15 seconds). A `6-minute` timer is set for uploading the result this year.

* [Hacker Cup 2021](https://github.com/kamyu104/FacebookHackerCup-2021)
* [Qualification Round](https://github.com/kamyu104/MetaHackerCup-2022#qualification-round)
* [Round 1](https://github.com/kamyu104/MetaHackerCup-2022#round-1)

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
|C| [Lemonade Life](https://www.facebook.com/codingcompetitions/hacker-cup/2022/round-1/problems/C)| [PyPy3](./Round%201/lemonade_life.py3) | _O(NlogN + V^2)_ | _O(N + V)_ | Hard | | Geometry, Convex Hull, Monotone Chain Algorithm, Graph, Dijkstra Algorithm |
