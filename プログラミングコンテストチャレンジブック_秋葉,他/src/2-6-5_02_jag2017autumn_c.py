# https://atcoder.jp/contests/jag2017autumn/tasks/jag2017autumn_c
# 
# https://qiita.com/rsk0315_h4x/items/ff3b542a4468679fb409
# を参考に，sqrt(B)までの数の篩を持つときに，primeかどうかではなく素因数を持つことにする．
# 最小の素因数は篩作るときにすぐ見つかるが，素因数で割った時の結果が2~sqrt(B)にいるか保証がないのでそこが困った．
# is_prime2には最大の素因数が入ってて，必ずis_prime中の素因数で素因数分解される．

import math

# def eratos(N):
#     is_prime = [True for _ in range(N+1)] # True when found as prime
#     is_prime[0] = False
#     is_prime[1] = False
#     # for s in range(2,):
#     i = 2
#     while i * i <= N:
#         if is_prime[i]: # prime
#             j = i*i
#             while j <= N:
#                 is_prime[j] = False
#                 j += i
#         i += 1
#     return is_prime

def kukan_eratos(A,B):
    sqrt_b = int(math.sqrt(B)) + 1
    is_prime = [_ for _ in range(sqrt_b+1)]

    # v is prime when [v-A] is True
    is_prime2 = [_+A for _ in range(B-A+1)]
    
    for i in range(2, sqrt_b+1):
        if is_prime[i] < i: continue

        j = i * i # 2*iではなく，i*iでよいはず
        while j * j <= B:
            is_prime[j] = i
            j += i

        # A以上の最小のiの倍数
        start = A + (-A) % i
        if start == i:
            start = i * 2

        q = start 
        while q <= B:
            is_prime2[q-A] = i
            q += i

    return is_prime, is_prime2

A, B = map(int, input().split())
is_prime, is_prime2 = kukan_eratos(A,B)
# print(is_prime, is_prime2)


num_fact = []
for tmp, p in zip([_+A for _ in range(B-A+1)], is_prime2):
    original = tmp
    a = []
    if tmp == p:
        tmp = tmp // p
        a.append(p)
    else:
        for i in range(p, 1, -1):
            if is_prime[i] == i:
                while tmp % i == 0:
                    tmp = tmp // i
                    a.append(i)

    count = len(a)
    if tmp != 1:
        count += 1
        
    num_fact.append(count)

    # print(tmp, p, tmp//p)
    #print(original, p, a, tmp)
# print(num_fact)

ans = 0
for i in num_fact:
    if is_prime[i] == i and i != 1:
        ans += 1

print(ans)
