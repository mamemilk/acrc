# https://atcoder.jp/contests/abc168/tasks/abc168_d
#
# N: 部屋の個数
# M: 通路の個数
# どの部屋も接続されている．
# 
# Noになることがあるか?，を小一時間悩む．
# A->1という最短経路があったら，Aに隣接する任意の部屋Bの最短経路は，
#   B->1か，
#   B->A->1
# になり，Bの道しるべは最短のものが一つ決められる．
# Bに隣接するCもまた同様で，Noは生まれない．
# 
# 
# -TLEが解消されず
# 


N, M = map(int, input().split())
connects = [[] for i in range(N)]

for i in range(M):
    a,b = map(int, input().split())
    connects[a-1].append(b)
    connects[b-1].append(a)

sirube = [None for i in range(N)]
#visited = []
visited = [False for i in range(N)]
starts = [1]

# while len(visited) < N:
while len(starts) > 0:
    for s in starts:
        # visited.append(s)
        visited[s-1] = True
        starts_next = []
        for e in (connects[s-1]):
            if sirube[e-1] != None:
                pass
            else:
                sirube[e-1] = s
            
            #if e not in visited:    # ここが遅い．
            if not visited[e-1]:
                starts_next.append(e)

    starts = starts_next

print('Yes')
for ele in sirube[1:]:
    print(ele)
