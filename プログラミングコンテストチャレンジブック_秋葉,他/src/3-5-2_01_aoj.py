# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=GRL_7_A&lang=jp
# 
# 

X, Y, E = map(int, input().split())
SOURCE = X+Y
SINK = X+Y + 1
Df = [{} for _ in range(X+Y+2)] # source, sinkを最後につける

for x in range(X):
    Df[SOURCE][x] = 1
    Df[x][SOURCE] = 0

for y in range(Y):
    Df[X+y][SINK] = 1
    Df[SINK][X+y] = 0

for _ in range(E):
    x, y = map(int, input().split())
    Df[x][X + y] = 1
    Df[X + y][x] = 0

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
    used = [False] * (X+Y+2)
    f = dfs(SOURCE, SINK, float('inf'), used)
    if f == 0:
        break
    flow += f

print(flow)
