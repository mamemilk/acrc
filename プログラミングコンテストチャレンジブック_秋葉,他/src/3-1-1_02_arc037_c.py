# https://atcoder.jp/contests/arc037/tasks/arc037_c
# 
# N < 30000
#
# Ai * Biの計算をしたら負けな気がするので，しない方法を考える．

from bisect import bisect_right

N, K = map(int, input().split())
A = sorted(list(map(int, input().split())))
B = sorted(list(map(int, input().split())))

lb = A[0] * B[0]
ub = A[-1] * B[-1]

while lb <= ub:
    x = (lb+ub)//2
    num = 0
    for a in A:
        num += bisect_right(B, x//a)
        if num >= K:
            break
    if num >= K:
        ub = x - 1
    else:
        lb = x + 1

print(lb)