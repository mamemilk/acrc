# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=2347
# 
# 自力じゃ無理でした。。。
# H,H′ の完全マッチング2回 + N が奇数 でSunnyが判定できる。
# 完全マッチングはTutte行列で判定

import random

def perfect(n, edges):          # edges: 0-indexed の (u,v) リスト
    if n == 0: return True
    if n % 2 == 1: return False  # 奇数次の歪対称は det=0
    p = (1 << 61) - 1
    T = [[0] * n for _ in range(n)]
    for u, v in edges:
        r = random.randint(1, p - 1)
        T[u][v] = r
        T[v][u] = p - r
    # Gauss の消去で det が非ゼロか（ゼロピボットに当たれば det=0）
    for c in range(n):
        piv = -1
        for r in range(c, n):
            if T[r][c]:
                piv = r; break
        if piv == -1:
            return False
        if piv != c:
            T[c], T[piv] = T[piv], T[c]
        inv = pow(T[c][c], p - 2, p)
        rc = T[c]
        for r in range(c + 1, n):
            f = T[r][c]
            if f:
                f = f * inv % p
                rr = T[r]
                for k in range(c, n):
                    rr[k] = (rr[k] - f * rc[k]) % p
    return True

# 入力を読みながら、辺を2種類に振り分ける
#   - 頂点1に接する辺 -> 相手をnb1に記録 : 集合H'
#   - それ以外の辺 -> edgesに(u, v)で記録 : 集合H
N, M = map(int, input().split())
nb1 = set()
edges = []
for _ in range(M):
    u, v = list(map(int, input().split()))
    if u == 1:
        nb1.add(v)
    elif v == 1: 
        nb1.add(u)
    else: 
        edges.append((u, v))

# H : 頂点 2..N, 完全マッチングを持つか判定して持ってなかったらSunny条件満たさず
nH = N - 1
edgesH = [(u - 2, v - 2) for u, v in edges]
if not perfect(nH, edgesH):
    print("No")
    exit()

# H' : z1=nH, z2=nH+1 を N(1) 全てに接続
z1, z2 = nH, nH + 1
edgesHp = edgesH
for a in nb1:
    edgesHp.append((a - 2, z1))
    edgesHp.append((a - 2, z2))
print("Yes" if perfect(N + 1, edgesHp) else "No")

