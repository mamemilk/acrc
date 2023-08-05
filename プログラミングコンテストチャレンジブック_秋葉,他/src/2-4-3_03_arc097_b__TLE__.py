# https://atcoder.jp/contests/arc097/tasks/arc097_b

class UnionFind():

    def __init__(self, N):
        self.parent = [i for i in range(N+1)]
        self.rank = [0 for _ in range(N+1)]
        self._members = [ [i] for i in range(N+1)]
        
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
            root = y
        else:
            self.parent[y] = x
            root = x
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1
            
        self._members[root] = self._members[x] + self._members[y]

    def members(self, x):
        return self._members[self.root(x)]


N, M = map(int, input().split())
P = [0] + list(map(int, input().split()))

uf = UnionFind(N)

for _ in range(M):
    x, y = map(int, input().split())
    uf.unite(x,y)

# print([uf.root(i) for i in range(1,N+1)])
# print([uf.members(i) for i in range(1, N+1)])

ans = 0
for i in range(1, N+1):
    if uf.same(i, P[i-1]):
        ans += 1
    # for j in uf.members(i):
    #     if P[j] == i:
    #         ans += 1
    #         break

print(ans)