# https://atcoder.jp/contests/abc079/tasks/abc079_d
# 
# 9,8,7,,,,2, 0を1に変える最小値を求める．


H, W = map(int, input().split())

Cij = []
for _ in range(10):
    Cij.append([*map(int, input().split())])

for k in range(10):
    for s in range(10):
        for e in range(10):
            Cij[s][e] = min(Cij[s][e], Cij[s][k]+Cij[k][e])

costs = [*map(lambda ele: ele[1], Cij)]

Ayx = [] # 1-D array
for _ in range(H):
    Ayx += [*map(int, input().split())]

ans = 0
nums = [0 for _ in range(10)]
for i in range(10):
    nums[i] = Ayx.count(i)
    ans += costs[i] * nums[i]

print(ans)