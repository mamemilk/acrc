# https://atcoder.jp/contests/jag2012autumn/tasks/icpc2012autumn_c
# 
#   Medianが最小値の全域木
#     最小全域木の場合にMedianが最小になりそう．


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
    costs = []
    es.sort(key=lambda ele: ele['cost'])
    E = len(es)
    uf = UnionFind(V)
    res = 0
    
    for i in range(E):
        e = es[i]
        if not uf.same(e['u'], e['v']):
            uf.unite(e['u'], e['v'])
            res += e['cost']
            costs.append(e['cost'])
    return res, costs
    

while True:
    es = []
    n, m = map(int, input().split())
    for _ in range(m):
        s, t, c = map(int, input().split())
        es.append({'u': s-1, 'v': t-1, 'cost': c})

    if n == 0 or m == 0:
        exit()

    pre = kruskal(n, es)[1]
    ans = pre[len(pre)//2]
    print(ans)


