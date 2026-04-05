# https://atcoder.jp/contests/arc074/tasks/arc074_d
# 
# 同じ列、同じ行の葉っぱには移動できてしまう。頂点数がmax(H,W)^2, 変数がmax(H,W)^3で、間に合わない。
# https://drken1215.hatenablog.com/entry/2020/01/29/011100
# 
# Super Nodeを追加して、計算量を下げる
# 


H, W = map(int, input().split())

G = [[] for _ in range(H+W)] # [0:H-1] => 行方向のSuperNode, [H:H+W-1] => 列方向のSuperNode
def add_edge(a, b, cap):
    G[a].append([b, cap, len(G[b])])
    G[b].append([a, 0, len(G[a]) - 1])
def dfs(v, t, f, cnt):
    if v == t: return f
    used[v] = True
    for e in G[v]:
        if not used[e[0]] and e[1] > 0:
            d = dfs(e[0], t, min(f, e[1]), cnt)
            if d > 0:
                e[1] -= d
                G[e[0]][e[2]][1] += d
                return d
    return 0

vindex = H+W
for i in range(H):
    for j,ch in enumerate(input()):
        if ch == 'S':
            G.append([])
            S = vindex
            add_edge(vindex, i,   float('inf')) # 行方向のSuperNodeに接続 S -> SuperNode
            add_edge(vindex, H+j, float('inf')) # 列方向のSuperNodeに接続 S -> SuperNode
            vindex += 1
        if ch == 'T':
            G.append([])
            T = vindex
            add_edge(i, vindex, float('inf'))   # SuperNode -> T
            add_edge(H+j, vindex, float('inf')) # SuperNode -> T 
            vindex += 1
        if ch == 'o':
            G.append([])
            add_edge(i, vindex, 1)   # SuperNode -> o
            add_edge(vindex, i, 1)   # o -> SuperNode 
            add_edge(H+j, vindex, 1) # SuperNode -> o
            add_edge(vindex, H+j, 1) # o -> SuperNode
            vindex += 1

flow = 0
while True:
    used = [False] * vindex
    f = dfs(S, T, float('inf'), 0)
    if f == 0 : break
    flow += f
if flow != float('inf'):
    print(flow)
else:
    print(-1)

