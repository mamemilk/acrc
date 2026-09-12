# https://atcoder.jp/contests/JAG2014Spring/tasks/icpc2014spring_c?lang=ja
#
#　一個前の問題と同じだが、一個前ではコストCijがIJ単独できまってたが、
#　この問題は前後の依存関係がありそうなのをどうするかが悩む。
#
#　文字コードをコストにすればいいじゃんっと思ったが、最小化される合計値が、Azが正しい答えのときにBBが最小値になっちゃう。
#　(カンニングしたが思いつきたかった発想ではあるが、)　N+1進数的な基数で重みつけすればよい。


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
board = [input() for _ in range(n)]

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

# 各文字の個数は n 以下なので、n+1 進数なら繰り上がらない。
radix = n + 1
char_cost = {
    ch: -(radix ** (51 - k))
    for k, ch in enumerate(alphabet)
}

# 行: 0 ～ n-1
# 列: n ～ 2n-1
# 始点: 2n、終点: 2n+1
s = 2 * n
t = 2 * n + 1

mcf = MinCostFlow(2 * n + 2)
edges = [[None] * n for _ in range(n)]

# 始点 → 各行：容量1、費用0
for i in range(n):
    mcf.add_edge(s, i, 1, 0)

# 各列 → 終点：容量1、費用0
for j in range(n):
    mcf.add_edge(n + j, t, 1, 0)

# 各行 → 各列：容量1、文字に対応する負の費用
for i in range(n):
    for j in range(n):
        edges[i][j] = mcf.add_edge(
            i, n + j, 1, char_cost[board[i][j]]
        )

# 初期ポテンシャル：元のコードと同じ計算。
initial_potential = [0] * (2 * n + 2)

for j in range(n):
    initial_potential[n + j] = min(
        edges[i][j][3] for i in range(n)
    )

initial_potential[t] = min(initial_potential[n:2 * n])

# n単位流して、最適な完全マッチングを求める。
mcf.flow(s, t, n, initial_potential)

# 最終的に選ばれたマスの文字を回収する。
selected = []

for i in range(n):
    for j in range(n):
        if edges[i][j][2] == 0:
            selected.append(board[i][j])

# 選ぶ順序は自由なので、昇順に並べる。
print("".join(sorted(selected)))




