# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=1350
# 
# 最小全域木を一回求める．"no alternative edge"は必ずここに含まれる．
# この最小全域木で使ったedgeを全体グラフGから一個ずつ抜いてそのG'で作られる最小全域木のコストが
#     同じなら，抜いた木は NOT "no alternative edge"
#     大きいなら，抜いた木は，"no alternative edge"
#
# python3だとTLE, pypyでacceptだた．

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
    
    edges = []
    for i in range(E):
        e = es[i]
        if not uf.same(e['u'], e['v']):
            uf.unite(e['u'], e['v'])
            res += e['cost']
            edges.append(e)
    return res, edges

es = []

N, M = map(int, input().split())
for _ in range(M):
    s, d, c = map(int, input().split())
    es.append({'v': s-1, 'u': d-1, 'cost': c})
    
# res_num = 0
# res_cost = 0
# cost, edges = kruskal(N, es)
# for e in edges:
#     es_ = es.copy()
#     es_.remove(e)
#     new_cost, new_edges = kruskal(N, es_)
#     if new_cost == cost:
#         pass
#     else:
#         res_num += 1
#         res_cost += e['cost']

# print(res_num, res_cost)

res_num = 0
res_cost = 0
cost, edges = kruskal(N, es)
for e in edges:
    index_r = es.index(e)
    es_ = es[0:index_r] + es[index_r+1:]
    new_cost, new_edges = kruskal(N, es_)
    if new_cost == cost:
        pass
    else:
        res_num += 1
        res_cost += e['cost']

print(res_num, res_cost)