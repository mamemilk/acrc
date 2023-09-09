# https://atcoder.jp/contests/indeednow-finalb-open/tasks/indeednow_2015_finalb_d
# 
#   全マスをたどる，移動のコストがないので．得点は，
#     全マスの得点
#     移動ボーナス
# 
#   これらを別々に計算する．
#   スタート，ゴールは無視して大丈夫(移動コストがないので)
# 
#   移動ボーナスは最大全域木，
#       prim法でやると，pypyでもTLE, krushal法でやった．
#   


'''
import math

def prim(V: int, cost): # cost = int[V][V]
    # cost = [[math.inf for _ in range(V)] for __ in range(V)]
    mincost = [math.inf for _ in range(V)]
    used = [False for _ in range(V)]

    mincost[0] = 0
    res = 0

    while True:
        v = - 1

        # すでにT(貪欲的に作られた木)に属しているXに属さない頂点のうち，Xからの辺のコストが最小になる頂点を探す．
        # 貪欲的に木を作るときに，最小コストになる頂点(v)から辺をつないで行く
        for u in range(V):
            if not used[u] and (v == -1 or mincost[u] < mincost[v]):
                v = u
        
        if v == -1:
            break
        used[v] = True
        res += mincost[v]

        for u in range(V):
            mincost[u] = min(mincost[u], cost[v][u])

    return res


H,W = map(int, input().split())
_ = input()
_ = input()

V = H*W
cost = [[math.inf for _ in range(V)] for __ in range(V)]

Phw = []
sum_a = 0
for h in range(H):
    Pw = list(map(int, input().split()))
    sum_a += sum(Pw)
    Phw.append(Pw)

for h in range(H):
    for w in range(W):
        index_v = h * W + w

        # UP
        if h != 0:
            index_u = (h-1) * W + w
            cost[index_v][index_u] = - Phw[h][w] * Phw[h-1][w]
        # DOWN 
        if h != H-1:
            index_u = (h+1) * W + w
            cost[index_v][index_u] = - Phw[h][w] * Phw[h+1][w]
        # LEFT
        if w != 0:
            index_u = h * W + (w-1)
            cost[index_v][index_u] = - Phw[h][w] * Phw[h][w-1]
        # RIGHT
        if w != W-1:
            index_u = h * W + (w+1)
            cost[index_v][index_u] = - Phw[h][w] * Phw[h][w+1]
        
        
sum_b = prim(V, cost)
print(sum_a - sum_b)

'''

class UnionFind():

    def __init__(self, N):
        self.parent = [i for i in range(N+1)]
        self.rank = [0 for _ in range(N+1)]
        
    def root(self, x):
        return x if self.parent[x] == x else self.root(self.parent[x])
    
    def same(self, x, y):
        return self.root(x) == self.root(y)
    
    def unite(self, x, y):
        x = self.root(x)
        y = self.root(y)
        if x == y :
            return
        
        if self.rank[x] < self.rank[y]:
            self.parent[x] = y
        else:
            self.parent[y] = x
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1

def kruskal(V, es): # es = {u: int, v: int, cost: int} []
    es.sort(key=lambda ele: ele['cost'])
    E = len(es)
    uf = UnionFind(V)
    res = 0
    
    for i in range(E):
        e = es[i]
        if not uf.same(e['u'], e['v']):
            uf.unite(e['u'], e['v'])
            res += e['cost']
    return res
    
H,W = map(int, input().split())
_ = input()
_ = input()

V = H*W
Phw = []
sum_a = 0
for h in range(H):
    Pw = list(map(int, input().split()))
    sum_a += sum(Pw)
    Phw.append(Pw)

es = []

for h in range(H):
    for w in range(W):
        index_v = h * W + w

        # UP
        if h != 0:
            index_u = (h-1) * W + w
            es.append({'v': index_v, 'u': index_u, 'cost': - Phw[h][w] * Phw[h-1][w]})
        # DOWN 
        if h != H-1:
            index_u = (h+1) * W + w
            es.append({'v': index_v, 'u': index_u, 'cost': - Phw[h][w] * Phw[h+1][w]})
        # LEFT
        if w != 0:
            index_u = h * W + (w-1)
            es.append({'v': index_v, 'u': index_u, 'cost': - Phw[h][w] * Phw[h][w-1]})
        # RIGHT
        if w != W-1:
            index_u = h * W + (w+1)
            es.append({'v': index_v, 'u': index_u, 'cost': - Phw[h][w] * Phw[h][w+1]})
        
        
sum_b = kruskal(V, es)
print(sum_a - sum_b)