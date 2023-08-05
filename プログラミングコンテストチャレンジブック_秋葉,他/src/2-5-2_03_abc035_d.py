# https://atcoder.jp/contests/abc035/tasks/abc035_d
# 
# 道路は一方通行．
# 滞在する都市は，1都市のみになる，，，はず．
# 各都市までの往復の時間を求める．
# 制限時間から往復の時間を引いた時間だけ引いた分だけ滞在する場合を，獲得所持金とする．
# 各都市に対して獲得所持金を求めて，一番大きい値を使う．

from heapq import heappush, heappop
 
N, M, T = map(int, input().split())
Ai = list(map(int, input().split()))

def dijkstra(s, roads):
    costs = [float('inf')] * len(roads)
    costs[s] = 0
    queue = [(0, s)]
    while queue:
        d, v = heappop(queue)
        if d > costs[v]:
            continue
        for v2, d2 in roads[v]:
            if d + d2 >= costs[v2]:
                continue
            costs[v2] = d + d2
            heappush(queue, (d + d2, v2))
    return costs
 
road_jun = [[] for _ in range(N)]
road_gyaku = [[] for _ in range(N)]
for _ in range(M):
    a, b, c = map(int, input().split())
    road_jun[a-1].append((b-1, c, ))
    road_gyaku[b-1].append((a-1, c, ))
    
time_jun = dijkstra(0, road_jun) 
time_gyaku = dijkstra(0, road_gyaku) 
 
ans = 0
for i in range(N):
    ans = max(ans, (T - time_jun[i] - time_gyaku[i]) * Ai[i])
print(ans)