# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=2429
# 
# 既存の丸をすべて消すコスト(B)を基準にする。
# あるマスに○を置くコストCi,jは、
# 　○がある場合は消さずに残す -Eij
# 　○がない場合は書く　　　　 Wij
# 
# Cijで、これの合計を最小化する。
# iは(１〜N)で、最小化するπ(i)の順列を求める
# i　jのマッチングをする問題になる。
# 
# MinCostFlowはダイクストラで、Potentialを使って負の辺を扱う。
#


from heapq import heappop, heappush

class MinCostFlow:
    def __init__(self, size):
        self.graph = [[] for _ in range(size)]

    def add_edge(self, src, dst, capacity, cost):
        # 辺 = [行き先, 逆辺のインデックス, 残余容量, 費用]
        forward = [dst, len(self.graph[dst]), capacity, cost]
        reverse = [src, len(self.graph[src]), 0, -cost]
        self.graph[src].append(forward)
        self.graph[dst].append(reverse)
        return forward

    def flow(self, source, sink, required, initial_potential):
        size = len(self.graph)

        # 計算済みの初期ポテンシャルをコピーして使う
        potential = list(initial_potential)

        total_cost = 0
        inf = float("inf")

        while required > 0:
            dist = [inf] * size
            prev = [None] * size
            dist[source] = 0
            queue = [(0, source)]

            while queue:
                d, v = heappop(queue)
                if d != dist[v]:
                    continue
                for k, (to, rev, cap, cost) in enumerate(self.graph[v]):
                    if cap == 0:
                        continue

                    # ポテンシャルで費用を補正してDijkstraを使う
                    nd = d + cost + potential[v] - potential[to]

                    if nd < dist[to]:
                        dist[to] = nd
                        prev[to] = (v, k)
                        heappush(queue, (nd, to))

            if dist[sink] == inf:
                raise ValueError("必要な流量を流せません")

            for v in range(size):
                if dist[v] != inf:
                    potential[v] += dist[v]

            amount = required
            v = sink
            while v != source:
                u, k = prev[v]
                amount = min(amount, self.graph[u][k][2])
                v = u

            v = sink
            while v != source:
                u, k = prev[v]
                edge = self.graph[u][k]
                edge[2] -= amount
                self.graph[v][edge[1]][2] += amount

                # 探索用の補正費用ではなく、登録した辺の費用を加算
                total_cost += amount * edge[3]
                v = u

            required -= amount

        return total_cost




n = int(input())

W = [list(map(int, input().split())) for _ in range(n)]
E = [list(map(int, input().split())) for _ in range(n)]
N = [[a == 'o' for a in input()] for _ in range(n)]

# 頂点番号
# 行: 0 ～ n-1
# 列: n ～ 2n-1
# 始点: 2n、終点: 2n+1
s = 2 * n
t = 2 * n + 1

mcf = MinCostFlow(2 * n + 2)

# 既存の丸をすべて消す場合の費用
base = sum(E[i][j] for i in range(n) for j in range(n) if N[i][j])

# 後でどのマスが選ばれたか調べるため、辺を保存する
edges = [[None] * n for _ in range(n)]

# 始点 → 各行：容量1、費用0
for i in range(n):
    mcf.add_edge(s, i, 1, 0)

# 各列 → 終点：容量1、費用0
for j in range(n):
    mcf.add_edge(n + j, t, 1, 0)

# 各行 → 各列：容量1、費用C[i][j]
# 負の費用もそのまま登録する
for i in range(n):
    for j in range(n):
        cost = -E[i][j] if N[i][j] else W[i][j]
        edges[i][j] = mcf.add_edge(i, n + j, 1, cost)

# 初期ポテンシャル = 初期グラフでの始点からの最短距離
#
# 初期状態では逆辺の容量が0なので、
# 始点 → 行 → 列 → 終点の順に計算できる。
#
# 始点・各行: 0
# 各列j:      min_i C[i][j]
# 終点:       全列のポテンシャルの最小値
initial_potential = [0] * (2 * n + 2)

for j in range(n):
    initial_potential[n + j] = min(
        edges[i][j][3] for i in range(n)
    )

initial_potential[t] = min(initial_potential[n:2 * n])

# n単位流して完全マッチングを求める
flow_cost = mcf.flow(s, t, n, initial_potential)
mincost = base + flow_cost

# 最終配置と初期配置の違いから、操作を作る
operations = []

for i in range(n):
    for j in range(n):
        # 辺は [行き先, 逆辺の番号, 残余容量, 費用]
        # 元の容量1が0になった辺には、最終的に1単位流れている
        selected = edges[i][j][2] == 0

        if N[i][j] and not selected:
            operations.append((i + 1, j + 1, "erase"))
        elif not N[i][j] and selected:
            operations.append((i + 1, j + 1, "write"))

print(mincost)
print(len(operations))

for operation in operations:
    print(*operation)