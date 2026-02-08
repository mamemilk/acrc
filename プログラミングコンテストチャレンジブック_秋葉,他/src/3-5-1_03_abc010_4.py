# https://atcoder.jp/contests/abc010/tasks/abc010_4

# 
# 特定の二人の友人関係を解消する　=　D,fにおける辺を削除する。
# 特定の一人のパスワードを変え、ログイン出来なくする　=　やり取りできない女の子を一人減らせる。
# 
# 

# 0 : Mr Takahashi
# Pi : Onnanoko IDs
N, G, E = map(int, input().split()) # N: num vertexes, G: num onnanoko, E: num edges
Pi = list(map(int, input().split())) 

Df = [{} for _ in range(N+1)]
for p in Pi:
    Df[p][N] = 1
    Df[N][p] = 0
for _ in range(E):
    a, b = map(int, input().split())
    Df[a][b] = 1
    Df[b][a] = 1


def dfs(v, t, f, used):
    if v == t:
        return f
    used[v] = True
    for nv in Df[v]:
        if not used[nv] and Df[v][nv] > 0:
            d = dfs(nv, t, min(f, Df[v][nv]), used)
            if d > 0:
                Df[v][nv] -= d
                Df[nv][v] += d
                return d
    return 0

flow = 0
while True:
    used = [False] * (N+1)
    f = dfs(0, N, float('inf'), used)
    if f == 0:
        break
    flow += f

print(flow)