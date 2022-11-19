# https://atcoder.jp/contests/joi2010yo/tasks/joi2010yo_d
# 
# 

N = int(input())
K = int(input())
Cs = []
for i in range(N):
    Cs.append(int(input()))

import itertools

P = itertools.permutations(Cs, K)

ans = set()

for p in P:
    hoge = "".join(str(n) for n in p)
    # print(p, hoge)

    ans.add(int(hoge))

print(len(ans))