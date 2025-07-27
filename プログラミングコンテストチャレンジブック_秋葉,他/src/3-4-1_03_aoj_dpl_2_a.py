# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DPL_2_A&lang=jp

V, E = map(int, input().split())
G = [[float('inf') for _ in range(V)] for __ in range(V)] 
for _ in range(E):
    s, t, d = map(int, input().split())
    G[s][t] = d

dp = [[float('inf') for _ in range(V)] for __ in range(1<<V)]

dp[0][0] = 0

def cost(s, t):
    return G[s][t]

for S in range(1<<V):
    for v in range(V):
        for u in range(V):
            if S != 0 and not (S & (1<<u)): continue

            if (S & (1<<v)) == 0 and v != u:
                dp[S | (1<<v)][v] = min(
                    dp[S | (1<<v)][v], 
                    dp[S][u] + cost(u, v)
                    )

# print(dp)

ans_pre = min(dp[-1])
if ans_pre == float('inf'):
    print(-1)
else:
    print(ans_pre)
