# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DPL_1_C&lang=jp

N, W = map(int, input().split())
VW = []
for _ in range(N):
    v, w = map(int, input().split())
    VW.append((v,w))

DP = [[0 for _ in range(W+1)] for _ in range(N+1)]

def solve():
    for i in range(N):
        for j in range(W+1):
            if j < VW[i][1]:
                DP[i+1][j] = DP[i][j]
            else:
                DP[i+1][j] = max(DP[i][j], DP[i+1][j-VW[i][1]]+VW[i][0])

solve()
print(DP[-1][-1])
