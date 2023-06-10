# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=2502
# kosu seigen nasi
# pittasi 
# 

n = int(input())
SLP = []
for _ in range(n):
    s,l,p = map(int, input().split())
    SLP.append((s,l,p))

m = int(input())





def solve():
    DP = [[0 for _ in range(W+1)] for _ in range(N+1)]
    for i in range(N):
        for j in range(W+1):
            if j < VW[i][1]:
                DP[i+1][j] = DP[i][j]
            else:
                DP[i+1][j] = max(DP[i][j], DP[i+1][j-VW[i][1]]+VW[i][0])

