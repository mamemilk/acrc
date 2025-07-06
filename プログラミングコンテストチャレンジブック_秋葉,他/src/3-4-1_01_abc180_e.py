# https://atcoder.jp/contests/abc180/tasks/abc180_e
# ここ見てやる。
#   https://algo-logic.info/bit-dp/

N = int(input())
XYZ = [tuple(map(int, input().split())) for _ in range(N)]

dp = [[float('inf') for _ in range(N)] for __ in range(1<<N)]

dp[0][0] = 0

def cost(abc, pqr):
    return abs(abc[0]-pqr[0])+abs(abc[1]-pqr[1])+max(0, pqr[2]-abc[2])

for S in range(1<<N):
    for v in range(N):
        for u in range(N):
            if S != 0 and not (S & (1<<u)): continue

            if (S & (1<<v)) == 0 and v != u:
                dp[S | (1<<v)][v] = min(
                    dp[S | (1<<v)][v], 
                    dp[S][u] + cost(XYZ[u], XYZ[v])
                    )

print(dp[-1][0])