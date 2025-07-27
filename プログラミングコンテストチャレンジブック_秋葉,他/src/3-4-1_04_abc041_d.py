# https://atcoder.jp/contests/abc041/tasks/abc041_d

N, M = map(int, input().split())

faster = [0] * N # faster[x] = 1 << y: x faster than y 
for _ in range(M):
    x, y = map(int, input().split())
    faster[x-1] = faster[x-1] | (1 << (y-1))

dp = [0 for _ in range((1<<N))]
dp[0] = 1
for i in range(1 << N):
    for j in range(N):
        if not (i & (1<<j) or i & faster[j]):
        # if not (i & (1<<j)): 
            dp[i | 1 << j] += dp[i]

print(dp[-1])
