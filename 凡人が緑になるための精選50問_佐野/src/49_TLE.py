'''
https://atcoder.jp/contests/abc177/tasks/abc177_e

N個の要素が，互いに素なら pairwise coprime
N個の要素の最大公約数が1なら，setwise coprime

N個の要素をすべて因数分解して，

任意の二つの要素で，同じ因数を持たない→因数の全体集合のサイズ== sum(各因数の集合のサイズ)
すべての要素で同じ因数を持たない→ 各要素の因数の||集合をとりサイズが0　or 単純にGCD

'''

N = int(input())
A = list(map(int, input().split()))

# https://note.nkmk.me/python-prime-factorization/
def prime_factorize(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a


Factors = [set(prime_factorize(a)) for a in A]
AllFactors = set()
for fs in Factors:
    for f in fs:
        AllFactors.add(f)

Kaku_Insu_Size_Wa = sum(map(lambda a: len(a), Factors))

if Kaku_Insu_Size_Wa == len(AllFactors):
    print("pairwise coprime")
    exit(0)

import math
g = A[0]
for a in A[1:]:
    g = math.gcd(g, a)

if g == 1:
    print("setwise coprime")
    exit(0)

print("not coprime")

# print(Factors)

