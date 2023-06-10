# https://atcoder.jp/contests/atc001/tasks/unionfind_a

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
            
# uf = UnionFind(7)
# uf.unite(1,2)
# uf.unite(2,5)
# uf.unite(4,6)
# uf.unite(4,7)

# print(uf.same(1,2))
# print(uf.same(1,3))
# print(uf.same(1,4))

N, Q = map(int, input().split())
uf = UnionFind(N)
for _ in range(Q):
    p, a, b = map(int, input().split())

    if p == 0: # connecting query
        uf.unite(a,b)
    else: # judge query
        print('Yes' if uf.same(a,b) else 'No')
        
