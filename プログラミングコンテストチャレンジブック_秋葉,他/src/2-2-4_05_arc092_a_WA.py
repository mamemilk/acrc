# https://atcoder.jp/contests/abc091/tasks/arc092_a

N = int(input())
Ri = []
for _ in range(N):
    x,y = map(int, input().split())
    Ri.append((x,y))
Bi = []
for _ in range(N):
    x,y = map(int, input().split())
    Bi.append((x,y))

Bi.sort(key=lambda ele: ele[0])

tmp = 0
for b in Bi:
    candids = list(filter(lambda ele: ele[0] < b[0], Ri))
    if len(candids) == 0:
        continue
    bf = max(candids, key=lambda ele: ele[1])
    Ri.remove(bf)
    tmp += 1

print(tmp)