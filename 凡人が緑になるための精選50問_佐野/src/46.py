'''
https://atcoder.jp/contests/abc153/tasks/abc153_e

Dp

体力hとして，h=0,1,2,....Hまでのコストを記載する，テーブルを作る．

h   0   1   2   3    .... H
c   0   inf inf inf       inf

1,,N番目の魔法ごとに，costを更新していく．

'''

import math

H, N = map(int, input().split())

Dp = [math.inf for i in range(H+1)]
Dp[0] = 0

for i in range(N):
    A,B = map(int, input().split())
    for h in range(H+1):
        if h+A <= H:
            Dp[h+A] = min(Dp[h+A], Dp[h]+B)
        else:
            Dp[H] = min(Dp[H], Dp[h]+B)

print(Dp[H])