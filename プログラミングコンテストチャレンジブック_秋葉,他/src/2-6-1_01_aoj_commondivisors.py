# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=0583
# 

import math 
N = input()
nums = [*map(int, input().split())]

gcd = math.gcd(*nums)

# ここはスピード無視して計算
for i in range(1, gcd+1):
    if gcd % i == 0:
        print(i)

