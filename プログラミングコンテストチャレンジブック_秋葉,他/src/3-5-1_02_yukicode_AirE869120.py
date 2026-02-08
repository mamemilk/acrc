# https://yukicoder.me/problems/no/654

'''
https://kmjp.hatenablog.jp/entry/2018/02/24/0930

    M個の飛行機の便に対しては、対応する(町,時刻)の頂点間で容量W[i]の有向辺を張る。
    同じ町に滞在し続けることができるので、同じ町における時刻の頂点間は、過去から未来に向け容量無限の辺を張る。

    Q[i]+D＞10^9のケースもあるので、「時刻10^9の時点でN番の町～～」の条件が一見ややこしいが、Q[i]の最大値は10^9なので「時刻2*10^9の時点でN番の町～～」とみなしてしまっても問題ない。

賢い。。。

座標圧縮の部分は鳥海さんの回答をカンニングさせていただきました。

'''

N, M, d = map(int, input().split())
E = [] # zahyo asshuku you no edge list
T = [set() for _ in range(N)] 
for _ in range(M):
    u, v, p, q, c = map(int, input().split()) # uのp時刻からvのq時刻へ容量cの便
    u -= 1
    v -= 1
    q += d # 到着時刻に滞在時間dを足す
    E.append(((u, p), (v, q), c))
    T[u].add(p)
    T[v].add(q)


# 場所、時刻をグラフのノードとする残余ネットワークを作る。
# 時刻の座標圧縮と、同じ街で別時刻の頂点をつなぐ変を追加する。
Df = []
V = 0
id = {}
for u in range(N):
    Vs = V
    for t in sorted(T[u]): # uの時刻tに対応する頂点
        id[(u, t)] = V
        Df.append({})
        if V > Vs:
            Df[V-1][V] = float('inf') # 同じ時間の街にとどまる辺は無限でよい。
            Df[V][V-1] = 0 # 昔の時間には戻れない。
        V += 1

# 容量を追加
for a, b, c in E:
    x = id[a]
    y = id[b]
    if y in Df[x]:
        Df[x][y] += c
    else:
        Df[x][y] = c
        Df[y][x] = 0


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