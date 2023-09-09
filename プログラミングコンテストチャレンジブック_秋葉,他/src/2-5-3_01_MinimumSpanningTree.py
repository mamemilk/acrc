# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=GRL_2_A&lang=jp

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
    




V, E = map(int, input().split())
# cost = [[math.inf for _ in range(V)] for __ in range(V)]
es = []
for _ in range(E):
    s, t, w = map(int, input().split())
    # cost[s][t] = w
    # cost[t][s] = w
    es.append({'u': s, 'v': t, 'cost': w})

print(kruskal(V, es))

# print(cost)
# print(prim(V, cost))
