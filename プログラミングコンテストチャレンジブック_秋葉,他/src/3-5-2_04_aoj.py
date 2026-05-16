# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=2480
N, M = map(int, input().split())  # num of Alice's & Bob's
G = [[b - 1 for b in map(int, input().split())][1:] for _ in range(N)]

SOURCE = N + M
SINK = N + M + 1
Df = [{} for _ in range(N + M + 2)]  # source, sinkを最後につける

for x in range(N):
    Df[SOURCE][x] = 1
    Df[x][SOURCE] = 0

for y in range(M):
    Df[N + y][SINK] = 1
    Df[SINK][N + y] = 0

for x in range(N):
    for y in G[x]:
        Df[x][N + y] = 1
        Df[N + y][x] = 0

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
    used = [False] * (N + M + 2)
    f = dfs(SOURCE, SINK, float('inf'), used)
    if f == 0:
        break
    flow += f

print('Alice' if flow < M else 'Bob')