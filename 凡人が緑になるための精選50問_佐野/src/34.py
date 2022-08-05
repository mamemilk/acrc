# https://atcoder.jp/contests/abc169/tasks/abc169_d
# 素因数分解して，
# N = p1**e1 * p2**e2 * ...
#   (p1,p2...は互いに異なる素数)
# eiを，1+2+3+....+6+(6より大きい整数)で分割

N = int(input())

import math

def factorize(n):
    if n == 1:
        return []

    res = []
    tmp = n
    for i in range(2,int(math.sqrt(n))+1):
        count = 0
        while tmp % i == 0:
            tmp = tmp // i
            count += 1
        if count != 0:
            res.append((i,count))
    if tmp!=1:
        res.append((tmp,1))
    if len(res)==0:
        res.append((n,1))
    return res

def decompose(e):
    count = 0
    n = 1
    remain = e
    while True:
        if remain - n <= n:
            count += 1
            break
        else:
            remain -= n
            n += 1
            count += 1
    return count

print(sum([decompose(e) for (p,e) in factorize(N)]))
