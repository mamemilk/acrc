# https://atcoder.jp/contests/agc001/tasks/agc001_b

# 解説を読む
# X + (N-X) + X + X + (N-X-X) + (N-X-X) + (N-X-X)
# 

import math
N, X = map(int,input().split())
ans = 3 * (N - math.gcd(N,X))
print(ans)