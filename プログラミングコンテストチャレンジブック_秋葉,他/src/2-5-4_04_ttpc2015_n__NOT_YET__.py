# https://atcoder.jp/contests/ttpc2015/tasks/ttpc2015_n
# 
# a1 + ci0 <= a2 + T
# a2 + ci1 <= a3 + T
# a3 + ci2 <= a1 + T
# ...
# というような不等式を成り立たせる最小のTを求める．

N, M, K = map(int, input().split())
edges = []
for _ in range(K):
    v, val = map(int, input().split())

for _ in range(M):
    u, w, c = map(int, input().split())
