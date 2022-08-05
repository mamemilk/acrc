# https://atcoder.jp/contests/abc175/tasks/abc175_c

"""
-N // Dの答えが，切り上げで最初に間違う．
"""

X, K, D = map(int, input().split())


nabs = abs(X) // D
n = nabs if X >= 0 else -nabs

if K < nabs:
    n = K if n >= 0 else -K
    min0 = X - (n*D)
    print(abs(min0))
    exit()

min0 = X - (n*D)
if n >= 0:
    min1 = min0 - D
else:
    min1 = min0 + D

#print(min0, min1)

if (K - abs(n)) % 2 == 0:
    print(abs(min0))
else:
    print(abs(min1))
