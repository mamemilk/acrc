# https://atcoder.jp/contests/utpc2013/tasks/utpc2013_08
# 


N, M = map(int, input().split())
Pi = list(map(int, input().split()))
Qi = list(map(int, input().split()))
XYAB = []
for _ in range(M):
    x,y,a,b = list(map(int, input().split()))    
    XYAB.append((x-1,y-1,a,b))

edges = []
for i in range(N):
    edges.append((0, i,  Pi[i]))
    edges.append((i, 0,  0))
    edges.append((0, i+N,0))
    edges.append((i+N, 0,  Qi[i]))

for x,y,a,b in XYAB:
    edges.append((x,   y+N, -a))
    edges.append((y+N, x, b))

# edge : [(s, t, d)], d: weight
def bellmanford(start,num_vertex,edges):
    d = [float("inf")] * num_vertex
    d[start] = 0

    for _ in range(num_vertex-1):
        for p,q,r in edges:
            if d[p] != float("inf") and d[q] > d[p] + r:
                d[q] = d[p] + r

    for _ in range(num_vertex-1):
        for p,q,r in edges:
            if d[p] != float("inf") and d[q] > d[p] + r:
                d[q] = d[p] + r

    return d


a = bellmanford(0, 2*N, edges)

if a is None or a[0] < 0:
    print('no')
else :
    print('yes')
