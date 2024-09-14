# https://atcoder.jp/contests/abc038/tasks/abc038_c
# 
# l <= rであって，l<=i<r ???? 解せん．
# しゃくとり法ではなく，微分して連続の長さを配列にいったん格納．
# その長さをたたみ込んだ．

import numpy as np

N = int(input())
ai = np.array([*map(int, input().split())])
dai = np.diff(ai)

# print(dai)

l = 0

lens = []

for d in dai:
    if d > 0:
        l += 1
    else :
        lens.append(l)
        l = 0
lens.append(l)

print(sum([((l+1)*l) // 2 for l in lens]) + N)
