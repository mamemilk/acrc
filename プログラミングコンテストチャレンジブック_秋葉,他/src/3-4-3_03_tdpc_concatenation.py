# https://atcoder.jp/contests/tdpc/tasks/tdpc_concatenation
# 解説見る。
#　DP[n][i][j]：長さnの文字列で、直近7文字がビット列iで、
#　

MOD = 10 ** 9 + 7
N, L = map(int, input().split())
Y = [0] * 256
for _ in range(N):
    w = input()
    l = len(w)
    a = int(w, 2)
    m = (1 << l) - 1
    for i in range(256):
        if i & m == a: Y[i] |= 1 << l - 1

X = [[0] * 256 for _ in range(128)]
X[0][1] = 1
for _ in range(L):
    nX = [[0] * 256 for _ in range(128)]
    for ni in range(256):
        nni = ni & 127
        for j in range(256):
            nj = ((j << 1) ^ 1 if j & Y[ni] else j << 1) & 255
            nX[nni][nj] = (nX[nni][nj] + X[ni//2][j]) % MOD
    X = nX
print(sum(sum(x[1::2]) for x in X) % MOD)