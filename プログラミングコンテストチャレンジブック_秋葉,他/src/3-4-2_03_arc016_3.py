# https://atcoder.jp/contests/arc016/tasks/arc016_3

# 例題の期待値
#   5%のアイドルを引いてから95%のアイドルを引く場合の回数期待値   (1 + 1/0.95)とその確率0.05
#   95%のアイドレスを引いてから5%のアイドルを引く場合の回数期待値 (1 + 1/0.05)とその確率0.95
#   (1 + 1/0.95)*0.05 + (1 + 1/0.05)*0.95 = 20.052631578947366
#   これに300円かけると，6015.789473684円．
# 
# この解説をがっつり読む．そして写経する．
# https://www.creativ.xyz/arc016c-605/
# 
# アイドルが3種類以上あるときは，ダブルかダブらないかの条件付き確率で期待値を求める．
# 
import sys
sys.setrecursionlimit(2000)

import math
EPS = 1e-6

# N : アイドルの種類
# M : くじの種類
N, M = map(int, input().split())

C = []
cost = []
idol = [] # 2-dim
p = [] # 2-dim

for _ in range(M):
    # C : 一つのくじに含まれる手札の種類
    C_, cost_ = map(int, input().split())
    C.append(C_)
    cost.append(cost_)
    idol_row = []
    p_row = []
    for __ in range(C_):
        idol_, p_ = map(int, input().split())
        idol_row.append(idol_ - 1)
        p_row.append(p_)
    idol.append(idol_row)
    p.append(p_row)

dp = [-1 for _ in range(1<<N)]
dp[(1<<N)-1] = 0

def calc(state):
    if dp[state] + EPS >= 0:
        return dp[state]
    
    minimum = math.inf
    for i in range(M):
        # i番目のガチャでの期待値
        success = 0 # 未入手のアイドルを獲得できる確率 (ダブらない確率)
        expect = 0 
        for j in range(C[i]):
            if state & (1<<idol[i][j]) == 0:
                success += p[i][j] / 100

        if success <= EPS:
            continue

        for j in range(C[i]):
            if state & (1<<idol[i][j]) == 0:
                # j番目のアイドルが未入手のとき
                expect += p[i][j] / 100 / success * calc(state | (1<<idol[i][j]))
        expect += cost[i] / success
        minimum = min(minimum, expect)
    dp[state] = minimum
    return dp[state]

print(calc(0))

