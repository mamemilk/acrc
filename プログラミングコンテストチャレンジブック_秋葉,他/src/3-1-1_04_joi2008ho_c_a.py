# https://atcoder.jp/contests/joi2008ho/tasks/joi2008ho_c
# 解説読む．

from bisect import bisect_left, bisect_right
from memory_profiler import profile
import numpy as np


N, M = map(int, input().split())
Ps = [0] # 得点しない用に0を入れておく
for _ in range(N):
    Ps.append(int(input()))

# 2回得点した時の合計を作る
Q = []
for pa in Ps:
    for pb in Ps:
        Q.append(pa+pb)

print(Q)

@profile()
def a(Q):
    Q = list(set(Q))
    # Q.sort()
    return Q

Q = a(Q)
# print(Q)
# print(Q[:bisect_right(Q, M)])
res = 0
for q in Q[:bisect_right(Q, M)]:
    r = bisect_right(Q, M-q)
    # print('lb:', r, M-q)
    res = max(res, q + Q[r-1])
print(res)