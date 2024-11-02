# https://atcoder.jp/contests/abc017/tasks/abc017_4
#
# 解説読みました．
# でもTLE
# 
#   - 足し算の回数が重複してしまう
#   - setでの存在確認をしてしまっている

N, M = map(int, input().split())
fi = [int(input()) for _ in range(N)]

MOD = 10**9 + 7

dp = [0] * (N+1)
dp[0] = 1
dp[1] = 1

s = set()
s.add(fi[0])

r = 1
l = 0 

while r < N:
    if fi[r] in s:
        s.remove(fi[l])
        l += 1
    else:
        s.add(fi[r])
        dp[r+1] = sum(dp[l:r+1]) % MOD
        r += 1

print(dp[N])

