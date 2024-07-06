# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=2220

# 
# 極値を見つけてその数と符号を確認すればよいのでは?
# 
# f(x) = ax^3 + bx^2 + cx + d
# f'(x) = 3ax^2 + 2bx + c
# f'(x)の判別式 
#   D(x) = b^2 - 3ac
#
# 0 >= D 極値が2個 or 1個
# 
# 0 < D 極値が0個，単調増加
#   

import math

def solve(a,b,c,d):
    def func(x):
        return a*(x**3) + b*(x**2) + c*x + d

    def D():
        return b**2 - 3*a*c
    
    def kai_dfunc():
        if D == 0:
            return [-b/(3*a)]
        if D > 0:
            return [(-b + math.sqrt(D))/(3*a), (-b - math.sqrt(D))/(3*a),]
        if D < 0:
            return []

    def bs(left, right):
        up = func(right) >= func(left) 
        while True:
            half = (left + right) / 2
            half_f = func(half)

            if abs(half_f) <= 0.001:
                break

            if up:
                if half_f >= 0:
                    left, right = left, half
                else:
                    left, right = half, right
            else:
                if half_f >= 0:
                    left, right = half, right
                else:
                    left, right = left, half

    if D() == 0:
        print( bs(-1000000, 1000000,) )
    if D() > 0:
        kda = kai_dfunc()
        print( bs(-1000000, kda[0]))
        print( bs(kda[0], kda[1]))
        print( bs(kda[1], 1000000))
    if D() < 0:
        print( bs(-1000000, 1000000,) )



N = int(input())
for _ in range(N):
    a,b,c,d = map(int, input().split())

    solve(a,b,c,d)
