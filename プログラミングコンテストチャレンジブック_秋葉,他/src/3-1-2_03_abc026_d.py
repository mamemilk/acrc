# https://atcoder.jp/contests/abc026/tasks/abc026_d

import math

A, B, C = map(int, input().split())

def func(t):
    return A * t + B * math.sin(C*t*math.pi)

left, right = 0, (100+B)/A

while True:
    half = (left+right)/2

    ans = func(half)
    if abs(ans - 100) <= 10**-6:
        break

    if ans < 100:
        left = half
    else:
        right = half

print(half)    


    