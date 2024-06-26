# https://atcoder.jp/contests/joi2008ho/tasks/joi2008ho_c
# 解説読む．
#   2回得点した合計の集合を，listでもっておいてからsetにする，というのだとMLEで通らず．

from bisect import bisect_left, bisect_right


N, M = map(int, input().split())
Ps = [0] # 得点しない用に0を入れておく
for _ in range(N):
    Ps.append(int(input()))

# 2回得点した時の合計を作る
Q = set()
for pa in Ps:
    for pb in Ps:
        Q.add(pa+pb)

Q = sorted(Q)

# print(Q)
# print(Q[:bisect_right(Q, M)])
res = 0
for q in Q[:bisect_right(Q, M)]:
    r = bisect_right(Q, M-q)
    # print('lb:', r, M-q)
    res = max(res, q + Q[r-1])
print(res)