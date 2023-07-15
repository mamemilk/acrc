# https://atcoder.jp/contests/abc126/tasks/abc126_d
import sys
sys.setrecursionlimit(100000)
N = int(input())
G = [[] for _ in range(N+1)]
color = [-1 for _ in range(N+1)]
for _ in range(N-1):
    u, v, w = map(int, input().split())
    G[u].append((v,w))
    G[v].append((u,w))

def dfs(v, c):
    color[v] = c
    for u, w in G[v]:
        if color[u] != -1:
            continue
        if w % 2 == 0:
            dfs(u, c)
        else:
            dfs(u, 1 - c)

dfs(1, 0)
print(*color[1:], sep='\n')