# http://codeforces.com/contest/528/problem/B
# 
# Greedyで串の数は求まる．
# 串が貫く区間の数を求める必要がある．


N = int(input())

AB = []
for _ in range(N):
    x,w = map(int, input().split())
    AB.append((x-w, x+w))

maxOrder = sorted(AB, key=lambda ele:ele[1])

ans = 1
_, b_prev = maxOrder[0]

for a,b in maxOrder[1:]:
    if a >= b_prev:
        ans += 1
        b_prev = b
    

print(ans)
