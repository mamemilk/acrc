# https://atcoder.jp/contests/abc032/tasks/abc032_d
#
# DPの方針はここを見させてもらった．
# https://qiita.com/tefuxu/items/baf4a70cbe93723ffe6a
#
# W, Vが大きくなる(wi, viが大きく，結果W,Vが大きくなりえる)
# W, Vの両方が大きい場合，Nは30が小さい．
# W, Vのどちらかが大きい場合，
#   dpの行はi番目の荷物として，列は
#     Vが大きいとき: 重みの合計がjで，中身が"最大の価値"
#     Wが大きいとき: 価値の合計がjで，中身が"i番目の荷物で価値jを達成する重みの和の最小値"
#   とする．

import bisect
from itertools import product

N, W = map(int, input().split())
VW = []
for _ in range(N):
    v,w = map(int, input().split())
    VW.append((v,w))

v_max = max(ele[0] for ele in VW)
w_max = max(ele[1] for ele in VW)
V_sum = sum(ele[0] for ele in VW)
W_sum = sum(ele[1] for ele in VW)


if W_sum <= W:
    print(V_sum)
    exit(0)

if w_max <= 1000:
    dp = [[0]*(W+1) for _ in range(N+1)]
    for i,(v,w) in enumerate(VW, 1): # enumerateの2番目のintは，indexの最初の数字指定
        for j in range(W+1):
            dp[i][j] = dp[i-1][j]
            if w <= j: 
                dp[i][j] = max(dp[i][j], dp[i-1][j-w] + v)
    print(dp[-1][W])
elif v_max <= 1000:
    dp = [[W+1]*(V_sum+1) for _ in range(N+1)]
    dp[0][0] = 0
    for i,(v,w) in enumerate(VW, 1):
        for j in range(V_sum+1):
            dp[i][j] = dp[i-1][j]
            if v<=j:
                dp[i][j] = min(dp[i][j], dp[i-1][j-v]+w)
    print(max(j for j,w in enumerate(dp[-1]) if w <= W))
else: # この条件が一番むずいのでは．．．写経しました．．．
    def enum(vw):
        l = [] 
        for p in product([True, False], repeat=len(VW)): # 
            sum_v = sum_w = 0
 
            for b, x in zip(p, vw):
                if b:
                    sum_v += x[0]
                    sum_w += x[1]
 
            l.append((sum_w, sum_v))
 
        return sorted(l, key=lambda x:x[0])
 
    def elim(vw):
        l = [(0,0)]
 
        for w, v in vw[1:]:
            if w > W:
                continue
            if v < l[-1][1]:
                continue
 
            l.append((w,v))
 
        return l
 
    A = elim(enum(VW[:N//2]))
    B = elim(enum(VW[N//2:]))        
 
    max_v = 0
 
    for w, v in B:
        i = bisect.bisect_left(A, (W-w, 10**20))
 
        if i != 0:
            max_v = max(max_v, v+A[i-1][1]) 
 
    print(max_v)