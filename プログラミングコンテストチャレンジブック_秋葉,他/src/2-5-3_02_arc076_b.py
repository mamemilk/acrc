# https://atcoder.jp/contests/abc065/tasks/arc076_b
# 最初何も考えずにエッジを全都市同士で結ぶ　→　TLE．
# 解説読んで以下に変更．

import math

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

N = int(input())
A = []
for i in range(N):
    x, y = map(int, input().split())
    A.append((i,x,y))

es = []

Ax = sorted(A, key=lambda ele: ele[1])
for i in range(len(Ax)-1):
    au = Ax[i]
    av = Ax[i+1]
    es.append({'u':au[0], 'v':av[0], 'cost': av[1] - au[1]})

Ay = sorted(A, key=lambda ele: ele[2])
for i in range(len(Ay)-1):
    au = Ay[i]
    av = Ay[i+1]
    es.append({'u':au[0], 'v':av[0], 'cost': av[2] - au[2]})

print(kruskal(N, es))