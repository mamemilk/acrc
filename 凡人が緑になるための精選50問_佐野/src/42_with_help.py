'''
https://atcoder.jp/contests/dp/tasks/dp_d

自力でできず，カンニング．
また，Pythonでは，TLE解消せずで，PyPyを使った．

以下の表を使って，DPを行う．
行がi, 列がWで，[i][W]にはWまで入れる場合の最適値が入る．

  i 
W   0 1 2 3 ... W
  0 0 0 0 0 ... 0
  1             sum_value
  2
  3


i=1から開始，
iのアイテムを入れる場合，入れない場合で，
真上のマス or 真上のマスのweight分左にいったマスで，比較して，大きい方を入れる．

'''

N, W = map(int, input().split())
Wi = [0]
Vi = [0]
for i in range(N):
    w, v = map(int,input().split())
    Wi.append(w)
    Vi.append(v)

Dp = [[0 for j in range(W+1)] for i in range(N+1)]

for i in range(N):
    for w in range(W+1):
        if Wi[i+1] <= w:
            Dp[i+1][w] = max(Dp[i+1][w], Dp[i][w-Wi[i+1]]+Vi[i+1])

        Dp[i+1][w] = max(Dp[i+1][w], Dp[i][w])

print(Dp[-1][-1])