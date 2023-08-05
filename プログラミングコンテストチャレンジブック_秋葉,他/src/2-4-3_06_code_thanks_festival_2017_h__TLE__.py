# https://atcoder.jp/contests/code-thanks-festival-2017-open/tasks/code_thanks_festival_2017_h

class UnionFind:

    def __init__(self, N):
        self.parent = [i for i in range(N+1)]
        self.rank = [0 for _ in range(N+1)]
        self.time = [float('inf') for _ in range(N+1)]
        self.now = 0
    
    def root(self, x, t):
        while self.time[x] <= t:
             x = self.parent[x]
        return x

    def same(self, x, y, t):
        return self.root(x, t) == self.root(y, t)

    def unite(self, x, y):
        self.now += 1
        x = self.root(x, self.now)
        y = self.root(y, self.now)
        if x == y:
            return
        
        if self.rank[x] < self.rank[y]:
            self.parent[x] = y
            self.time[x] = self.now
        else:
            self.parent[y] = x
            self.time[y] = self.now
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1

N, M = map(int, input().split())
uf = UnionFind(N)

for _ in range(M):
    a, b = map(int, input().split())
    uf.unite(a, b)

Q = int(input())

ans = []
for _ in range(Q):
    x, y = map(int, input().split())
    found = False
    for t in range(1,M+1):
        if uf.same(x, y, t):
            ans.append(t)
            found = True
            break
    if not found:
        ans.append(-1)
print(*ans, sep = '\n')