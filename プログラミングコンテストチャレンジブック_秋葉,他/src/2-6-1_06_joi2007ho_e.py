# https://atcoder.jp/contests/joi2007ho/tasks/joi2007ho_e
# 
# DFSで先端の重さを求めて行く．
#   重さは，left, rightの長さを，left, rightのgcdで割った値になる．

import math

def dfs(i):
    p, q, r, b = pqrb[i]
    if r == 0:
        x = 1
    else:
        x = dfs(r - 1)
    if b == 0:
        y = 1
    else:
        y = dfs(b - 1)
    lcm = x * p * y * q // math.gcd(x * p, y * q)
    return lcm // p + lcm // q


N = int(input())
pqrb = []
par = [0] * N
for i in range(N):
    p, q, r, b = map(int, input().split())
    if r != 0:
        par[r - 1] += 1
    if b != 0:
        par[b - 1] += 1
    pqrb.append([p, q, r, b])

for i in range(N):
    if par[i] == 0:
        print(dfs(i))