# https://atcoder.jp/contests/code-festival-2017-qualb/tasks/code_festival_2017_qualb_c
# 解説を読みました．

import sys
sys.setrecursionlimit(1000000000)

N, M = map(int, input().split())
G = [[] for _ in range(N+1)]
color = [-1 for _ in  range(N+1)]
for i in range(M):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)
  
is_nibu_graph = True
 
def dfs(a, c):
    global is_nibu_graph
    color[a] = c
    for b in G[a]:
        if color[b] == -1:
            dfs(b, 1-c)
        else:
            if color[b] != 1-c:
                is_nibu_graph = False

dfs(1, 0)
if is_nibu_graph:
    print(color.count(0)*color.count(1) - M)
else:
    print(N*(N-1)//2 - M)