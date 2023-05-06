# https://atcoder.jp/contests/code-thanks-festival-2017-open/tasks/code_thanks_festival_2017_c
# 

import heapq

N, K = map(int, input().split())
AB = []
for _ in range(N):
    a,b = map(int, input().split())
    AB.append((a,b))

heapq.heapify(AB)

t = 0
for _ in range(K):
    ab = heapq.heappop(AB)
    t += ab[0]
    heapq.heappush(AB, (ab[0] + ab[1], ab[1]))

print(t)