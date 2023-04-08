# https://atcoder.jp/contests/arc057/tasks/arc057_b
# 
# dp[i][j] : i日目までにj日期限がよくなる必要な勝ち数の最小値
# dp[N][?] <= K

N, K = map(int, input().split())
A = []
for _ in range(N):
    A.append(int(input()))

dp = [[float('inf')] * (N+1) for _ in range(N+1)]
dp[0][0] = 0

count = 0
for i in range(N):
    for j in range(i + 1):
        d = dp[i][j] * A[i] // count + 1 if count > 0 else 1
        if d <= A[i]:
            dp[i + 1][j + 1] = min(dp[i][j + 1], dp[i][j] + d)
        dp[i + 1][j] = min(dp[i + 1][j], dp[i][j])
    count += A[i]
if K == count:
    print(1)
else: 
    for i in range(N, -1, -1):
        if dp[N][i] <= K:
            print(i)
            break
            