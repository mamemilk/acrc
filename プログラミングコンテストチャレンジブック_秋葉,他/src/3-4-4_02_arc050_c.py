# https://atcoder.jp/contests/arc050/tasks/arc050_c
# 八木さんのカンニング

from math import gcd
A, B, MOD = map(int, input().split())

def mulmatmod(a,b):
    m,n = len(a), len(b[0])
    res = [[0]*n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            for k in range(len(b)):
                res[i][j] +=a[i][k] * b[k][j]
                res[i][j] %=MOD
    return res

def powmatmod(a,p):
    m = len(a)
    res = [[0]*m for _ in range(m)]
    
    # 単位行列で初期化
    for i in range(m):
        res[i][i]= 1

    while p>0:
        if p & 1:
            res = mulmatmod(res,a)
        a = mulmatmod(a,a)
        p >>=1
    return res   

C=[[10,1],[0,1]]

g = gcd(A,B)

fA=powmatmod(C,A)[0][1]
D=[[powmatmod(C,g)[0][0],1],[0,1]]
fB_fD=powmatmod(D, B//g)[0][1]

print(fA*fB_fD%MOD)