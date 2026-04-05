# https://atcoder.jp/contests/kupc2016/tasks/kupc2016_e
# 
# ヤギが端にいたら -1
# ヤギとグリッドの外を分離する。--> 最小カット
# 柵はマス目におかれるので辺がカットされるのではない。マスを2つのノードにわけて
# 容量1のその間に置く。
# 

import sys
sys.setrecursionlimit(1000000)

def dfs(v, t, f):
    if v == t: return f
    used[v] = True
    for to in G[v]:
        if not used[to] and G[v][to] > 0:
            d = dfs(to, t, min(f, G[v][to]))
            if d > 0:
                G[v][to] -= d
                G[to][v] += d
                return d
    return 0

H, W = map(int, input().split())
V = 2 * H * W + 2 # S, Tを追加
G = [{} for _ in range(V)] # 疎にしたいので、辞書
S = 0
T = V - 1
n = 1
for i in range(H):
    for j, a in enumerate(input()):
        if a == 'X':
            G[n][n+1] = float('inf')
            G[n+1][n] = 0
            G[S][n+1] = float('inf')
            G[n+1][S] = 0
        else:
            G[n][n+1] = 1
            G[n+1][n] = 0

        if i > 0:
            G[n+1][n-2*W] = float('inf')
            G[n-2*W][n+1] = 0
        if i < H - 1:
            G[n+1][n+2*W] = float('inf')
            G[n+2*W][n+1] = 0
        if j > 0:
            G[n+1][n-2] = float('inf')
            G[n-2][n+1] = 0
        if j < W - 1:
            G[n+1][n+2] = float('inf')
            G[n+2][n+1] = 0

        if i == 0 or i == H - 1 or j == 0 or j == W - 1:
            G[n+1][T] = float('inf')
            G[T][n+1] = 0
        n += 2

flow = 0
while True:
    used = [False] * V
    f = dfs(S, T, float('inf'))
    if f == 0: break
    flow += f
print(flow if flow < float('inf') else -1)