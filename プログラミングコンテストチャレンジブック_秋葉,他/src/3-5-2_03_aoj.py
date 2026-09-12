# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=1163&lang=jp
# 

import math 

def solve():
    m, n = map(int, input().split())
    if m == 0 and n == 0:
        return False

    blues = list(map(int, input().split()))
    while len(blues) < m:
        blues += list(map(int, input().split()))
    reds = list(map(int, input().split()))
    while len(reds) < n:
        reds += list(map(int, input().split()))
    
    SOURCE = m + n 
    SINK = m + n + 1
    Df = [{} for _ in range(m+n+2)]

    for i in range(m):
        Df[SOURCE][i] = 1
        Df[i][SOURCE] = 0
    
    for i in range(m, m+n):
        Df[i][SINK] = 1
        Df[SINK][i] = 0
        
    for bindex, blue in enumerate(blues):
        for rindex, red in enumerate(reds):
            if math.gcd(blue, red) > 1:
                Df[bindex][m+rindex] = 1
                Df[m+rindex][bindex] = 0

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
        used = [False] * (m+n+2)
        f = dfs(SOURCE, SINK, float('inf'), used)
        if f == 0:
            break
        flow += f

    print(flow)
    return True

while solve():
    pass
