'''
https://atcoder.jp/contests/abc192/tasks/abc192_e

- heapqを使って最小値をpopする．
- popしたら，visited = Trueにする．
- popした街の隣接の街の時刻を更新する．
を繰り返す．

'''
import math
import heapq

N, M, X, Y = map(int, input().split())

connects = [[] for i in range(N+1)]
visited  = [False for i in range(N+1)]
times    = [math.inf for i in range(N+1)]

for i in range(M):
    a,b,t,k = map(int, input().split())
    connects[a].append((b,t,k))
    connects[b].append((a,t,k))

hque = []
# heapq.heapify(hque) # 0要素の場合はheapify不要
heapq.heappush(hque, (0, X))

while len(hque) > 0:
    time, town = heapq.heappop(hque)

    if visited[town]:
        continue

    visited[town] = True
    for (to, t, k) in connects[town]:
        times[to] = min(times[to], math.ceil(time/k)*k+t)
        heapq.heappush(hque, (times[to], to))

if times[Y] == math.inf:
    print(-1)
else:
    print(times[Y])





    

    





#[[-1 for j in range(N+1)] for i in range(N+1)]