'''
https://atcoder.jp/contests/abc141/tasks/abc141_d

heapqつかったら簡単だった．

'''

import heapq 
N, M = map(int, input().split())
A = list(map(lambda s: -int(s), input().split()))

heapq.heapify(A)

for i in range(M):
    m = heapq.heappop(A) / 2
    heapq.heappush(A, m)

print(sum(map(lambda a: int(-a), A)))