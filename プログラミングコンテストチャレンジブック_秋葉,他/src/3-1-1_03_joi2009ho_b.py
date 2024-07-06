# https://atcoder.jp/contests/joi2009ho/tasks/joi2009ho_b

from bisect import bisect_right

d = int(input()) # distance 
n = int(input()) # num stores
m = int(input()) # num orders 

Ds = [0]
for _ in range(n-1):
    di = int(input())
    Ds.append(di)
Ds.sort()
Ds.append(d)

Os = []
for _ in range(m):
    oi = int(input())
    Os.append(oi)

# print(d, n, m)
# print(Ds)
# print(Os)

res = 0
for oi in Os:
    right_index = bisect_right(Ds, oi)
    left_index = right_index - 1

    res += min(oi-Ds[left_index], Ds[right_index]-oi)

print(res)
