# https://atcoder.jp/contests/abc032/tasks/abc032_c

N, K = map(int, input().split())

si = [int(input()) for _ in range(N)]


l = 0
r = 0
mul = 1
ans = 0

while l < N:
    while r < N and mul * si[r] <= K:
        mul *= si[r]
        r += 1

    if l == r: 
        l += 1
        r = l
    else:
        ans = max(ans, r-l)
        if si[l] == 0:
            ans = N
            break
        mul = mul // si[l]
        l += 1

print(ans)