# https://atcoder.jp/contests/joi2014ho/tasks/joi2014ho3

import itertools

N = int(input())
A = []
for _ in range(N): 
    A.append(int(input()))

# 円で一週するので，配列をつなげる．その積分値を作って差分でバームクーヘンの長さを求める
Acum = [0] + list (itertools.accumulate(A+A))
total = Acum[N]

j = 0 
k = 0 
wmax = 0
for i in range(N):
    while Acum[j] - Acum[i] <= total // 3:
        j += 1
    w1 = Acum[j] - Acum[i]
    while Acum[k] - Acum[j] <= (total-w1) // 2:
        k += 1
    w2 = Acum[k] - Acum[j]
    w3 = total-w1-w2
    wmax = max(wmax, w3, Acum[k-1] - Acum[j])
    
print(wmax)