# https://atcoder.jp/contests/arc093/tasks/arc093_c
# 
# 重み付き無向グラフが与えられて，辺を白黒に塗る．
#   白黒に塗った辺を含む全域木がある．
#   この全域木の最小全域木の重さがXである．
# 白黒に塗る場合の数を求める．
#
# 鳥海さんの回答をほとんどカンニング．．．．

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

    used = []
    unused = []
    
    for i in range(E):
        e = es[i]
        if not uf.same(e['u'], e['v']):
            uf.unite(e['u'], e['v'])
            res += e['cost']
            used.append(e)
        else:
            unused.append(e)

    return res, used, unused
   
N, M = map(int, input().split())
X = int(input())
es = []
for _ in range(M):
    u, v, w = map(int, input().split())
    u -= 1
    v -= 1
    es.append({'u': u, 'v': v, 'cost': w})

# 全体での最小全域木を求める．
S, used, unused = kruskal(N, es)

if S > X:
    print(0)
    exit()

# 求めた最小全域木の各頂点(i, v)間のパス上にある辺の重みの
# 最大値(pathMax[i][v])を求める．
paths = [[] for _ in range(N)]
for e in used:
    u, v, w = e['u'], e['v'], e['cost']
    paths[u].append((v, w))
    paths[v].append((u, w))
pathMax = [[-1] * N for _ in range(N)]
for i in range(N):
    pathMax[i][i] = 0
    stack = [(i, 0)]
    while stack:
        u, max_w = stack.pop()
        for v, w in paths[u]:
            if pathMax[i][v] == -1:
                pathMax[i][v] = max(max_w, w) 
                stack.append((v, pathMax[i][v]))

# 求めた最小全域木で使用しなかった辺(頂点u, v)の重みと
# pathMax[u][v] の差分(diff)が
#   X - S と等しい辺の数(eq)
#   X - S よりも大きい辺の数(up)
# を求める
eq = up = 0
for e in unused:
    u, v, w = e['u'], e['v'], e['cost']
    diff = w - pathMax[u][v]
    if diff == X - S:
        eq += 1
    if diff > X - S:
        up += 1

MOD = 10**9 + 7
ans = 2 * (2**eq - 1) * 2**up % MOD
if S == X:
    ans += (2**(N-1) - 2) * 2**(eq+up) % MOD
    ans %= MOD 
print(ans)