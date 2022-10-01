# https://atcoder.jp/contests/arc029/tasks/arc029_1

import itertools
import math 

N = int(input())
T = []
for i in range(N):
    T.append(int(input()))

Tsum = sum(T)
diff = math.inf

if N == 1:
    print(T[0])
    exit(0)

for na in range(1, N//2+1):
    for comb in itertools.combinations(T,na):
        Asum = sum(comb)
        Bsum = Tsum - Asum

        diff = min(abs(Asum - Bsum), diff)

print((Tsum-diff)//2 + diff)