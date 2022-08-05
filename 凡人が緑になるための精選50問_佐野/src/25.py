# https://atcoder.jp/contests/dp/tasks/dp_a
# 
# 動的計画法で解くのがよさそう．

N = int(input())
H = list(map(int, input().split()))

Costs = [0] * N

Costs[0] = 0
Costs[1] = abs(H[1] - H[0])
# Costs[2] = min(H[2]-H[0]+Costs[0], H[2]-H[1]+Costs[1])
# ...

for i in range(2,N):
    Costs[i] = min(abs(H[i]-H[i-2])+Costs[i-2], abs(H[i]-H[i-1])+Costs[i-1])

print(Costs[-1])