# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=2661
# 
# N <= 50, so brute force will be only 2500. 

import numpy as np 
N = int(input())
A = [list(map(int, input().split())) for _ in range(N)] 
N = int(input())
B = [list(map(int, input().split())) for _ in range(N)] 

A = np.array(A)
B = np.array(B)

# print(A, B)

min_gap = float('inf')
for a in A:
    # print(B-a)
    gaps = np.linalg.norm(B-a, axis=1)
    min_gap = min(min_gap, gaps.min())

print(min_gap)