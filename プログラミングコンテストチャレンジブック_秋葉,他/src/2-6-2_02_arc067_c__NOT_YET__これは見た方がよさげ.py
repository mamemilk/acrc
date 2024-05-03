# https://atcoder.jp/contests/arc067/tasks/arc067_c
# 
# mod inverseなのか??? 鳥海さんの回答をカンニングしました．
# 
# 
# N人をグループ分けしたい。N人は互いに区別される。
#   - どのグループの人数も A人以上 B人以下である
#   - i=A,A+1,...,Bについて、i人のグループの個数は C個以上 D個以下である
# 
# A人に均等に割り振る場合の数は，
#    N人の順列 / A!**k / k!
# 分母は，これはグループ内並び順を取り除くため
# グループ同士の区別はないから，グループの並びの場合の数は取り除く


import math

N, A, B, C, D = map(int, input().split())

P = 10**9 + 7

fact = [1] + [0] * N
fact_inv = [1] + [0] * N

for i in range(1, N+1):
    fact[i] = (fact[i-1] * i) % P
    fact_inv[i] = pow(fact[i], -1, P)

dp = [0] * N + [1]
for i in range(A, B+1):
    for j in range(i*C, N+1):
        if dp[j] == 0:
            continue
        for k in range(C, D+1):
            if i * k > j:
                break
            p = math.perm(j, i*k)
            r1 = fact_inv[k]
            r2 = pow(fact_inv[i], k, P)
            dp[j-i*k] += dp[j] * p * r1 * r2 % P
            dp[j-i*k] %= P
print(dp[0])