# https://atcoder.jp/contests/arc026/tasks/arc026_4
# 
# 費用を最小化するのではなく，
# 費用 / 時間 を最小化する．



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

N, M = map(int, input().split())
ABCTi = []
for _ in range(M):
    ABCTi.append((*map(int, input().split()), ))

l = 0
r = 1000000

for _ in range(50):
    x = (r+l)/2
    ABCTi.sort(key=lambda p: p[2]-x*p[3])

    total = 0
    uf = UnionFind(N)

    for a, b, c, t in ABCTi:
        af = c-t*x
        if uf.same(a, b) and af>0: 
            continue
        uf.unite(a, b)
        total += af

    if total <= 0:
        r = x
    else:
        l = x

print(r)

