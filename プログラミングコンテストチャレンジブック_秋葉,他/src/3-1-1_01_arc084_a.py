# https://atcoder.jp/contests/abc077/tasks/arc084_a
# 

from bisect import bisect_left, bisect_right

N = int(input())

As = sorted(map(int, input().split()))
Bs = sorted(map(int, input().split()))
Cs = sorted(map(int, input().split()))

res = 0
for B in Bs:
    num_A = bisect_left(As, B) 
    num_C = len(Cs) - bisect_right(Cs, B)
    res += num_A * num_C

print(res)