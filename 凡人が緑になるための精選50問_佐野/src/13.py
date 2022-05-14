# https://atcoder.jp/contests/abc189/tasks/abc189_b

N, X = map(int, input().split())
# V = []
# P = []
#A = []
A_sum = 0
for n in range(N):
    v,p = map(int, input().split())
    # V.append(v)
    # P.append(p)
    #A.append( v * p / 100)
    A_sum += v * p / 100
    if A_sum > X:
        break

if A_sum > X:
    print(n+1)
else:
    print(-1)
