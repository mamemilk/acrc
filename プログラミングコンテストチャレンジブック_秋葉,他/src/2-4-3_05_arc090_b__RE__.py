# https://atcoder.jp/contests/arc090/tasks/arc090_b
# 
# l, rが同じグループ→すでに拘束条件あり

class UnionFind():
    def __init__(self, N):
        self.parent = [i for i in range(N+1)]
        self.rank = [0 for _ in range(N+1)]
        self.weight = [0 for _ in range(N+1)]
        
    def root(self, x):
        return x if self.parent[x] == x else self.root(self.parent[x])
    
    def same(self, x, y):
        return self.root(x) == self.root(y)
    
    def unite(self, x, y, w):
        rx = self.root(x)
        ry = self.root(y)
        if rx == ry:
            return
        
        if self.rank[rx] < self.rank[ry]:
            self.parent[rx] = ry
            self.weight[rx] = self.weight[y] - w - self.weight[x]
        else:
            self.parent[ry] = rx
            self.weight[ry] = w + self.weight[x] - self.weight[y]
            if self.rank[rx] == self.rank[ry]:
                self.rank[rx] += 1
            
    def diff(self, x, y):
        return self.weight[y] - self.weight[x]
    
N, M = map(int, input().split())

uf = UnionFind(N)
for _ in range(M):
    l, r, d = map(int, input().split())
    if uf.same(l, r):
        if d != uf.diff(l,r):
            print('No')
            exit()
    else:
        uf.unite(l,r,d)
print('Yes')
