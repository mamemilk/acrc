# https://atcoder.jp/contests/code-festival-2015-quala/tasks/codefestival_2015_qualA_d

N, M = map(int, input().split())
X = [None]
for _ in range(M):
    x = int(input())
    X.append(x)


def isok(T):
    D = [0 for _ in range(M + 1)]

    if X[1] > T: 
        return False
    for i in range(1,M+1):
        L = X[i] - D[i-1] - 1
        if i == M:
            R = min(max(T-2*L, (T-L)//2), N-X[i])
        else:
            R = min(max(T-2*L, (T-L)//2), X[i+1]-X[i]-1)
        if R < 0:
            R = 0 
        D[i] = X[i] + R
    print(D)
    return D[-1] == N

left, right = 0, 500000

while left+1 != right:
    # print(left, right)
    c = (left + right) // 2
    if isok(c):
        ok_t = c
        left, right = left, c
    else :
        left, right = c, right

print(ok_t)