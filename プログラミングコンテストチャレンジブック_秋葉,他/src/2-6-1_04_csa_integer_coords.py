# https://csacademy.com/contest/round-68/task/integer-coords/
# 
# 斜め線が何個の格子の上を通るかは，x,yの最大公倍数になる．
# 
#   gcd()

import math

N, M, K = map(int, input().split())

ans = 0
for x1 in range(N+1):
    for y1 in range(M+1):
        for x2 in range(N+1):
            for y2 in range(M+1):
                if x1 == x2 and y1 == y2:
                    continue
                dx = abs(x1-x2)
                dy = abs(y1-y2)
                if math.gcd(dx, dy) == K - 1:
                    ans += 1


ans = ans // 2

print(ans)