# https://atcoder.jp/contests/soundhound2018-summer-qual/tasks/soundhound2018_summer_qual_d

from heapq import heappush, heappop

n, m, s, t = map(int, input().split()) # s : start, t : terminal
edge = [[] for _ in range(n+1)]
for _ in range(m):
    u, v, a, b = map(int, input().split()) # a : yen, b : snuuk
    edge[u].append((v,a,b,))
    edge[v].append((u,a,b,))

def dijkstra(s, is_snuuk):
    S = [float("inf")]*(n+1)
    S[s] = 0
    h = []
    heappush(h,[0,s])
    while h:
        paid, now = heappop(h)
        for e in edge[now]:
            next = e[0]
            cost = e[2 if is_snuuk else 1]
            if paid+cost < S[next]:
                S[next] = paid+cost
                heappush(h,[paid+cost,next])
    return S[::-1]

ans = []
cost = 10**15
now = 0
for i,j in zip(dijkstra(s,False),dijkstra(t,True)):
    now = max(now,cost-i-j)
    ans.append(now)
print(*ans[:-1][::-1],sep="\n")

