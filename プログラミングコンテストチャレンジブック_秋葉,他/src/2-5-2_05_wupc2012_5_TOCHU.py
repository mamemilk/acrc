# https://atcoder.jp/contests/wupc2012-closed/tasks/wupc2012_5

# 街から一本しか道は出てない→道をたどっていって終点にたどりつくかつかないか．
# かかる時間 = Σ Ci[i] * 奇数 (where iはたどったときの街インデックス)

N, M = map(int, input().split())
edge = [() for _ in range(N)]
for _ in range(M):
    f, t, c = map(int, input().split())
    edge[f] = (t, c)

pass_cities = []
pass_costs = []
start = 0
next = -1
while next != N - 1:
    next = edge[start][0]
    cost = edge[start][1]
    pass_cities.append(start)
    pass_costs.append(cost)
    start = next

# print(pass_cities, pass_costs)

total = sum(pass_costs)
if total % 4 == 0 or total % 7 == 0:
    print(total)
else: 
    pass