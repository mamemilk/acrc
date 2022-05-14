# https://atcoder.jp/contests/abc180/tasks/abc180_c
import math

N = int(input())

res_half = []
for n in range(1, int(math.sqrt(N))+1):
    if N % n == 0:
        print(n)
        if N / n != n:
            res_half.append(str(N//n))
    else:
        pass

print('\n'.join(reversed(res_half)))
