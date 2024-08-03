# https://atcoder.jp/contests/arc060/tasks/arc060_a
# 
# 

N, A = map(int, input().split())
Xi = [*map(int, input().split())]

S = max(sum(Xi), N*A)+1

# dp[j][k][s] x1,,,xjからk枚選んでxiの合計をsにするような選び方の総数 
dp = [[[0]*S for k in range(N+1)] for j in range(N)]
dp[0][0][0] = 1
dp[0][1][Xi[0]] = 1

for j in range(1, N):
    for k in range(N+1):
        for s in range(S):
            dp[j][k][s] = dp[j-1][k][s]
            if j>0 and s >= Xi[j]:
                dp[j][k][s] += dp[j-1][k-1][s-Xi[j]]

# import pprint
# pprint.pprint(dp)

print(sum([dp[-1][k][k*A] for k in range(1, N+1)]))