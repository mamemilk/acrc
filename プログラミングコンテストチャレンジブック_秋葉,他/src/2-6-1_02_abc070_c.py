# https://atcoder.jp/contests/abc070/tasks/abc070_c

import math
N = int(input())
Ti = []
for _ in range(N):
    Ti.append(int(input()))

print(math.lcm(*Ti))