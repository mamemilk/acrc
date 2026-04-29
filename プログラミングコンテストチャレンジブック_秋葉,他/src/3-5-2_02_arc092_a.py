# https://atcoder.jp/contests/abc091/tasks/arc092_a
# 
# 

N = int(input())
reds = []
for _ in range(N):
    reds.append(list(map(int, input().split())))
blues = []
for _ in range(N):
    blues.append(list(map(int, input().split())))

# reds.sort(key=lambda c: (c[0], c[1]))
# blues.sort(key=lambda c: (c[0], c[1]))

SOURCE = 2*N
SINK = 2*N+1
Df = [{} for _ in range(2*N+2)]

for i in range(N):
    Df[SOURCE][i] = 1
    Df[i][SOURCE] = 0

for i in range(N, 2*N):
    Df[i][SINK] = 1
    Df[SINK][i] = 0

for rindex, red in enumerate(reds):
    for bindex, blue in enumerate(blues):
        if red[0] < blue[0] and red[1] < blue[1]:
            Df[rindex][N+bindex] = 1
            Df[N+bindex][rindex] = 0

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
    used = [False] * (2*N+2)
    f = dfs(SOURCE, SINK, float('inf'), used)
    if f == 0:
        break
    flow += f

print(flow)
