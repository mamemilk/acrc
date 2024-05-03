# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=2286
# 
# 分母，分子は，それぞれ1~Nを取り得りえて，最大N*N個
#    1/1を超えない，
#    分母，分子が互いに素
# を求めればよい?
# 

import math

def eratos(M):
    arr = [True for _ in range(M+1)] # True when found as prime
    arr[0] = False
    arr[1] = False
    for s in range(2,M+1):
        if arr[s]: # prime
            gain = 2
            while gain * s <= M:
                arr[gain*s] = False
                gain += 1
    return arr

arr = eratos(10**6)

def isprime(N):
    return arr[N]

def iscoprime(a,b):
    return math.gcd(a,b)==1


t = int(input())

for _ in range(t):
    n = int(input())

    ans = 2 # for 0/1 & 1/1
    for bunbo in range(2, n+1):
        for bunsi in range(1, bunbo):
            if isprime(bunbo):
                ans += 1
            elif iscoprime(bunbo,bunsi):
                ans += 1

    print(ans)
