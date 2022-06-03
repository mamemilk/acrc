# https://atcoder.jp/contests/abc189/tasks/abc189_b

"""
どハマりした．
少数で計算して，精度問題で通らなかった．
"""

N, X = map(int, input().split())
A = []
A_sum = 0
for n in range(N):
    v,p = map(int, input().split())
    A.append( v * p )

for n,a in enumerate(A):
    A_sum += a
    if A_sum > X * 100:
        print(n+1)
        exit()
print(-1)
