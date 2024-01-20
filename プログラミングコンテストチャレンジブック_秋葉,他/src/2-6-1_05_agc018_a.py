# https://atcoder.jp/contests/agc018/tasks/agc018_a
# 
# 解説読んで実装しました．
# 

import math

N, K = map(int, input().split())
Ai = [*map(int, input().split())]

gcd = math.gcd(*Ai)
m   = max(Ai)

if K % gcd==0 and K <= m:
    print("POSSIBLE")
else:
    print("IMPOSSIBLE")