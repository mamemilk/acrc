# https://atcoder.jp/contests/abc110/tasks/abc110_d
import math
import collections

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

N, M = map(int, input().split())

arr = eratos(int(math.sqrt(M)+1))
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

a = collections.Counter(factorize(M))

ans = 1
for v in a.values():
    ans *= math.comb(v+N-1, v)

    if ans > 10**9 + 7:
        ans = ans % (10**9 + 7)

print(ans)