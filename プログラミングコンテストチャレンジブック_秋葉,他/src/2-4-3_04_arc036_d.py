# https://atcoder.jp/contests/arc036/tasks/arc036_d

# 公式解説を読む．
# https://img.atcoder.jp/arc036/editorial.pdf


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
            



N, Q = map(int, input().split())

# 0 ~ N-1    : 青い点の，1~N
# N ~ 2N-1   : 赤い点の, 1~N

df = UnionFind(2*N)

for _ in range(Q):
    w, x, y, z = map(int, input().split())
    ao_x = x - 1
    ao_y = y - 1
    aka_x = x - 1 + N
    aka_y = y - 1 + N

    if w == 1: # build a road
        if z % 2 == 0: # 偶数
            df.unite(ao_x, ao_y)            
            df.unite(aka_x, aka_y)
        else: # 奇数
            df.unite(ao_x, aka_y)
            df.unite(aka_x, ao_y)
    else: # takahasi 
        if df.same(aka_x, aka_y):
            print("YES")
        else:
            print("NO")