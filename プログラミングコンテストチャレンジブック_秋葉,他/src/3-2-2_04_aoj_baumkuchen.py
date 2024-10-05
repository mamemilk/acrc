# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=0600


import itertools

N = int(input())
A = [int(input()) for _ in range(N)]
S = [0] + list(itertools.accumulate(A+A))
W = S[N]
j = 0
k = 0
max_w = 0
for i in range(N):
    while S[j] - S[i] < W // 3:
        j += 1
    w1 = S[j] - S[i]
    rest = (W - w1) / 2
    while S[k] - S[j] < rest:
        k += 1
    max_w = max(max_w, W-w1-(S[k]-S[j]),S[k-1]-S[j])
print (max_w)
