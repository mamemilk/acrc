# https://atcoder.jp/contests/arc016/tasks/arc016_3

'''
蟻本の説明は絶望的にわからなかったので、以下のサイトでFord-Fulkerson法を学習した。
https://www.youtube.com/watch?v=TjOA3vK0HCI

備忘録
- ネットワークの接続とキャパシタc(a)を表現したいグラフをD,fとする。
- 頂点A,Bが辺aでつながれているときに、現在流れる流量f(a)とし、
  増やせる量c(a)-f(a)、減らせる量f(a)でA,Bを接続するグラフDfを残余ネットワークとする。
  量０のときは辺がない, 残余ネットワークは、f(a)によって接続がかわる。
- 残余ネットワークでSource SからSink Tまで接続できるパスを増加道という。

- 流量f(a)が最大となる必要十分条件は、残余ネットワークに増加道が存在しないことである。

- カットとは、S側に属する頂点集合XとT側に属する頂点集合Yに分けたときに、
  XからYへ向かう辺の集合のことである。

- 最大流の値と、最小カットの容量は等しい。

'''

V, E = map(int, input().split()) # Vertex, Edge
Df = [{} for _ in range(V)] # ui, vi, ci : uからvへ流せる容量ci, Zanyo Network
for _ in range(E):
    u, v, c = map(int, input().split())
    Df[u][v] = c # 初期流量0 なので、uからvへ流せる容量はc
    Df[v][u] = 0

def dfs(v, t, f, used):
    if v == t:
        return f
    used[v] = True
    for nv in Df[v]:
        if not used[nv] and Df[v][nv] > 0:
            d = dfs(nv, t, min(f, Df[v][nv]), used)
            if d > 0:
                Df[v][nv] -= d
                Df[nv][v] += d
                return d
    return 0


flow = 0
while True:
    used = [False] * V
    f = dfs(0, V-1, float('inf'), used)
    if f == 0:
        break
    flow += f

print(flow)




