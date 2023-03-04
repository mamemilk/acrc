# https://atcoder.jp/contests/abc153/tasks/abc153_e
# 

H, N = map(int, input().split())
AB = []
for _ in range(N):
    a, b = map(int, input().split()) 
    AB.append((a,b))

DP = [float("inf") for _ in range(H+1)]
DP[0] = 0
 
for i in range(H):
    for a, b in AB:
        if i + a > H:
            DP[H] = min(DP[H], DP[i] + b)
        else:
            DP[i + a] = min(DP[i + a], DP[i] + b)

print(DP[H])