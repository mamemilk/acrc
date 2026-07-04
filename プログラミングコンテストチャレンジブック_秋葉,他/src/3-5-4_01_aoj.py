# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=GRL_6_B&lang=jp
# 
# 増加道を探す際にコストの低いところから探すが、
# DFSでGreedyにやるとノードをたどったときに増やした経路のコストが低いかを保証できない。
# Dijkstraでコストの低い経路にそのボトルネック分を流す、を繰り返す。

import heapq

V, E, F = map(int, input().split()) # Vertex, Edge, Flow
Df = [{} for _ in range(V)] # 残余道: Df[u][v] = uからvへ流せる容量
Dc = [{} for _ in range(V)] # コスト: Dc[u][v] = uからvへ1流すときのコスト
for _ in range(E):
    u, v, c, d = map(int, input().split())
    Df[u][v] = c
    Df[v][u] = 0
    Dc[u][v] = d
    Dc[v][u] = -d # 逆辺は「払い戻し」なのでコストは負

INF = float('inf')
s, t = 0, V - 1
h = [0] * V # 各ノードのポテンシャル
cost = 0

while F > 0:
    # DFSの代わりに、残余グラフ上でreduced costによるDijkstra
    dist = [INF] * V
    prev = [-1] * V
    dist[s] = 0
    pq = [(0, s)]
    while pq:
        du, u = heapq.heappop(pq)
        if du > dist[u]:
            continue
        for nv in Df[u]:
            if Df[u][nv] > 0:
                nd = du + Dc[u][nv] + h[u] - h[nv] # reduced cost: 非負が保証される
                if nd < dist[nv]:
                    dist[nv] = nd
                    prev[nv] = u
                    heapq.heappush(pq, (nd, nv))

    if dist[t] == INF: # tに到達できない = これ以上流せない
        print(-1)
        exit()

    for v in range(V): # ポテンシャル更新
        if dist[v] < INF:
            h[v] += dist[v]

    # 最短路に沿ってボトルネック容量を求めて流す(prevを遡る)
    f = F
    v = t
    while v != s:
        f = min(f, Df[prev[v]][v])
        v = prev[v]
    v = t
    while v != s:
        Df[prev[v]][v] -= f
        Df[v][prev[v]] += f
        v = prev[v]
    F -= f
    cost += f * h[t] # h[t]はs→tの真の最短コストになっている

print(cost)