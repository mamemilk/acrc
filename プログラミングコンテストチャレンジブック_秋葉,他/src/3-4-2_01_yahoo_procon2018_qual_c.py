# https://atcoder.jp/contests/yahoo-procon2018-qual/tasks/yahoo_procon2018_qual_c
# 解説読んだ．
# 
# 売却 : 高橋君は売却して現金手に入れられるが，青木君は商品の販売を一点停止できる．
# 購入 : 高橋君は現金の足りる分だけ買うことができる．
# 
# 最後に高橋君が持つ商品の価値の総和が得点
# 高橋君は得点を最大化，青木君は得点を最少化するように選択する．
# 
# 高橋君が，売却か購入かを決定する．
# 
# msk : bit列でしているする商品集合
# DP : n個売却して，商品集合mskすべてを購入した場合の最大価値
# 関数f : n品売って，購入可能な商品の集合がmskである場合の最大価値
# 
# 売却した場合，青木君が商品の売却停止した場合の得点最大値(高橋君は合理的に動くの)の最小値になる商品を選ぶ．
# 購入の場合は，高橋君が購入可能な商品を，n個まで売ったお金で買った時の最大価値
# 

import math

N = int(input())
X = list(map(int, input().split()))
C = list(map(int, input().split()))
V = list(map(int, input().split()))

dp = [[0]*(1<<N) for _ in range(N+1)]
memo = [[-1]*(1<<N) for _ in range(N+1)]

def f(n, msk):
    global memo
    if 0 <= memo[n][msk]:
        return memo[n][msk]
    if n == N:
        return 0
    
    # 売却のときの得点の損失見込み
    sold = math.inf
    for i in range(N):
        if msk & (1<<i):
            sold = min(sold, f(n+1, msk - (1<<i)))
    
    # 購入の時の獲得得点
    buy = dp[n][msk]

    memo[n][msk] = max(sold, buy)
    return memo[n][msk]


for n in range(N+1):
    yen = sum(X[0:n])

    for msk in range(0, 1<<N):
        co, va = 0, 0 
        for i in range(N):
            if msk & (1<<i): 
                co += C[i]
                va += V[i]

        if co <= yen:
            dp[n][msk] = va
        else:
            dp[n][msk] = 0
    
    for msk in range(0, 1<<N):
        for i in range(0, N):
            if msk & (1<<i):
                dp[n][msk] = max(dp[n][msk], dp[n][msk^(1<<i)])

print(f(0, (1<<N)-1))
