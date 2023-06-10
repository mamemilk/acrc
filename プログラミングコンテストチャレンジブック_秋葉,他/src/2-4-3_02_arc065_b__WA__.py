# https://atcoder.jp/contests/abc049/tasks/arc065_b

class UnionFind():

    def __init__(self, N):
        self.parent = [i for i in range(N+1)]
        self.rank = [0 for _ in range(N+1)]
        self.counts = [1 for _ in range(N+1)]
        
    def root(self, x):
        return x if self.parent[x] == x else self.root(self.parent[x])
    
    def same(self, x, y):
        return self.root(x) == self.root(y)
    
    def unite(self, x, y):
        x = self.root(x)
        y = self.root(y)
        if x == y :
            return

        c = self.counts[x] + self.counts[y]

        if self.rank[x] < self.rank[y]:
            self.parent[x] = y
            self.counts[y] = c # y is root. store count in root 
        else:
            self.parent[y] = x
            self.counts[x] = c # x is root. store count in root
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1
 
    def count(self, x):
        return self.counts[self.root(x)]


N, K, L = map(int, input().split())

uf_doro = UnionFind(N)
uf_both = UnionFind(N)

for _ in range(K): # doro
    p, q = map(int, input().split())
    uf_doro.unite(p, q)

for _ in range(L): # doro
    p, q = map(int, input().split())

    if uf_doro.same(p, q):
        uf_both.unite(p,q)

for i in range(1, N+1):
    print(uf_both.count(i), end=' ')

print('')

# print(uf_both.counts)
# print(uf_both.parent)
# print([uf_both.root(i) for i in range(N+1)])
