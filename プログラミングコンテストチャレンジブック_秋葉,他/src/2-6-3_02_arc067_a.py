# https://atcoder.jp/contests/abc052/tasks/arc067_a
# 
# 素因数分解した後の素因数の集計は，こちらを参考にした．
# https://note.nkmk.me/python-prime-factorization/
# 

import collections
from functools import reduce

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

arr = eratos(1000)
primes = []
for n, isprime in enumerate(arr):
    if isprime:
        primes.append(n)

def factorize(N):
    ans = []
    for p in primes:
        while N % p == 0:
            ans.append(p)
            N = N//p
            if N == 1:
                return ans

N = int(input())

pre = []
for n in range(2, N+1):
    pre += factorize(n)

print(reduce(lambda p,c: p*(c+1), collections.Counter(pre).values(), 1) % (10**9 + 7))