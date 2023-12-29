# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=GRL_1_B&lang=jp
# 
# 負値があるのでBellman-Ford

# edge : [(s, t, d)], d: weight
def bellmanford(start,num_vertex,edges):
    d = [float("inf")] * num_vertex
    d[start] = 0

    # 一週目，始点以外のすべてのvertexに対してエッジの全探索をする．
    for _ in range(num_vertex-1):
        for p,q,r in edges:
            if d[p] != float("inf") and d[q] > d[p] + r:
                d[q] = d[p] + r

    # 負の経路の判定 : もう一週してコストがへることがあったら負の経路あり．
    for _ in range(num_vertex-1):
        for p,q,r in edges:
            if d[p] != float("inf") and d[q] > d[p] + r:
                return None

    return d

V, E, r = map(int, input().split())
edges = []
for _ in range(E):
    s, t, d = map(int, input().split())
    edges.append((s,t,d))

a = bellmanford(r, V, edges)

if a is not None:
    ans = map(lambda ele: "INF" if ele == float("inf") else ele, a)
    print(*list(ans), sep="\n")
else :
    print("NEGATIVE CYCLE")