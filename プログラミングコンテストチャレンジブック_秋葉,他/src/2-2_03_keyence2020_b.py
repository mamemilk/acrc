# https://atcoder.jp/contests/keyence2020/tasks/keyence2020_b
# 

N = int(input())

StartEnds = []
for i in range(0, N):
    x, l = map(int, input().split())
    StartEnds.append((x-l, x+l))

maxOrder = sorted(StartEnds, key=lambda ele: ele[1])

ans = 1
_, e_prev = maxOrder[0]

for s, e in maxOrder[1:]:
    if s >= e_prev:
        ans += 1
        e_prev = e

print(ans)