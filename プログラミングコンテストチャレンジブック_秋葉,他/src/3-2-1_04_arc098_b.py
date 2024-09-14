# https://atcoder.jp/contests/abc038/tasks/abc038_c
# 

import numpy as np

N = int(input())
ai = np.array([*map(int, input().split())])

l = 0 
r = 0 
sum = 0
ans = 0


while l < N:
    while r < N and sum + ai[r] == sum ^ ai[r]:
        sum += ai[r]
        r += 1
    ans += r - l 
    sum -= ai[l]
    l += 1

print(ans)
    