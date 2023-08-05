# https://atcoder.jp/contests/maximum-cup-2018/tasks/maximum_cup_2018_c
# 
# Ai (i=1~N)には，1~Nの数字が，ダブり，スキップなしで記載される．
# 天使→悪魔→天使→悪魔→最初の天使の循環ができる　→　悪魔の最大数はこのループの要素数//2
#                                           できない→　矛盾
# 
# (鳥海さん回答)ダブりがないので，必ずループになる(ループが複数あるかもしれないが)．UnionFindを使わずとも解ける．

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
    
N = int(input())
uf = UnionFind(N)

for i in range(1,N+1):
    A = int(input())
    uf.unite(i,A)
 
from collections import Counter
c = Counter(uf.parent[1:])
ans = 0
for a in list(c.values()):
    if a % 2 == 1:
        print(-1)
        exit()
    else:
        ans += a//2

print(ans)