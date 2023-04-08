# https://atcoder.jp/contests/maximum-cup-2018/tasks/maximum_cup_2018_d
#
#   M: 一周の長さ
#   L: 待ち合わせの場所
#   X: 条例違反の周回数
#
# aを
# 

N, M, L, X =  map(int, input().split())

Ai = map(int, input().split())

dp = [0] + [X] * (M-1) # 何周で訪れられるか
 
for a in Ai:
  dp, dp_tmp = dp.copy(), dp
  for i in range(M):
    j = (i - a) % M
    dp[i] = min(dp_tmp[i], dp_tmp[j] + (j + a) // M)
 
print('Yes' if dp[L] < X else 'No')