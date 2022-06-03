# https://atcoder.jp/contests/abc167/tasks/abc167_c
# 総当たりだとすると，購入する本の組み合わせになるので，
# 12C1 + 12C2 + 12C3 + 12C4 + 12C5 + 12C6 + ...
# (12     66   + 220  + 990  + 792  + 924) * 2
# そんなに大きくないので，総当たりで求めることにする．

import itertools
import functools

N, M, X = list(map(int, input().split()))
C = []
A = []
for i in range(N):
    ROW = list(map(int, input().split()))
    Ci = ROW[0]
    Aij = ROW[1:]
    C.append(Ci)
    A.append(Aij)

OK_price = []
for i in range(0,N):
    for comb in itertools.combinations(range(0,N),i+1):
        price = sum([C[r] for r in comb])
        
        levels = []
        for m in range(M):
            levels.append(sum([A[r][m] for r in comb]) >= X)
        is_ok = functools.reduce(lambda a,b : a and b, levels)
        #print(levels, is_ok)
        if is_ok:
            OK_price.append(price)

if len(OK_price) == 0:
    print(-1)
else:
    print(min(OK_price))



