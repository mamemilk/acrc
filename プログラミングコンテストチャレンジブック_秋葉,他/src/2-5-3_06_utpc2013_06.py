# https://atcoder.jp/contests/utpc2013/tasks/utpc2013_06
# 
# 問題の意味を理解するのに時間がかかった．．．．
#   初期状態は各点が個別のグループ．
#   Q個のクエリで，グループが併合される．
#   併合されたグループを連結する最小木の長さを答える．
#
#   併合されたグループを連結できない場合は，IMPOSSIBLEを出力する．
#
# 一回一回で，最小木探索をするとTLEにきっとなる．
# グループA,Bを統合するときのEDGESを，
#    Aの最小全域木で使われているEDGES
#    Bの最小全域木で使われているEDGES
#    Aのいずれかのノードと，BのいずれかのノードをつなげるEDGES
# を使って全域木を作る．
# 
# WAで苦戦中．．．



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

    ans_es = []
    
    for i in range(E):
        e = es[i]
        if not uf.same(e['u'], e['v']):
            uf.unite(e['u'], e['v'])
            res += e['cost']
            ans_es.append(e)
    return res, ans_es


es = []
N, M = map(int, input().split())
for _ in range(M):
    u, v, w = map(int, input().split())
    es.append({'u': u, 'v': v, 'cost': w})



group = UnionFind(N)


print_debug = print if False else lambda *ele: ele

used_es = {}
Q = int(input())
for _ in range(Q):
    p, q = map(int, input().split())

    # p, qが共に単独で，p,qに対するグループが"初めて"作られる
    if (p not in used_es.keys()) and (q not in used_es.keys()):
        candid_es = list(filter(lambda e: (e['u'] == p and e['v'] == q) or (e['u'] == q and e['v'] == p), es))
        res, ans_es = kruskal(N, candid_es)
        used_es[p] = ans_es
        used_es[q] = ans_es
        print_debug('case 1: ', res, ans_es)
    # pはグループに属していて，qは単独
    elif (p in used_es.keys()) and (q not in used_es.keys()):
        members = list(map(lambda e: e['u'], used_es[p])) + list(map(lambda e: e['v'], used_es[p]))
        candid_es = used_es[p] + list(filter(lambda e: (e['u'] == q and e['v'] in members) or (e['v'] == q and e['u'] in members), es))
        res, ans_es = kruskal(N, candid_es)
        used_es[p] = ans_es
        used_es[q] = ans_es
        print_debug('case 2: ', res, ans_es)
    # qはグループに属していて，pは単独
    elif (p not in used_es.keys()) and (q in used_es.keys()):
        members = list(map(lambda e: e['u'], used_es[q])) + list(map(lambda e: e['v'], used_es[q]))
        candid_es = used_es[q] + list(filter(lambda e: (e['u'] == p and e['v'] in members) or (e['v'] == p and e['u'] in members), es))
        res, ans_es = kruskal(N, candid_es)
        used_es[p] = ans_es
        used_es[q] = ans_es
        print_debug('case 3: ', res, ans_es)
    # 両方グループに属している
    else:
        if used_es[p] is used_es[q]:
            res, ans_es = kruskal(N, used_es[p])
            print_debug('case 4a: ', res, ans_es)
        else:
            members_p = list(map(lambda e: e['u'], used_es[p])) + list(map(lambda e: e['v'], used_es[p]))
            members_q = list(map(lambda e: e['u'], used_es[q])) + list(map(lambda e: e['v'], used_es[q]))
            candid_es = used_es[p] + used_es[q] \
                        + list(filter(lambda e: (e['u'] in members_p and e['v'] in members_q) or (e['v'] in members_p and e['u'] in members_q), es))
            res, ans_es = kruskal(N, candid_es)
            used_es[p] = ans_es
            used_es[q] = ans_es
            print_debug('case 4b: ', res, ans_es)
   


    if res == 0:
        print("IMPOSSIBLE")
    else:
        print(res)
