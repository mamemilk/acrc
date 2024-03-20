# https://atcoder.jp/contests/arc017/tasks/arc017_1
# 
# 解説を見ました．

import math

def eratos(N):
    is_prime = [True for _ in range(N+1)] # True when found as prime
    is_prime[0] = False
    is_prime[1] = False
    # for s in range(2,):
    i = 2
    while i * i <= N:
        if is_prime[i]: # prime
            j = i*i
            while j <= N:
                is_prime[j] = False
                j += i
        i += 1
    return is_prime

def kukan_eratos(A,B):
    sqrt_b = int(math.sqrt(B)) + 1
    is_prime = [True for _ in range(sqrt_b+1)]

    # v is prime when [v-A] is True
    is_prime2 = [True for _ in range(B-A+1)]
    
    for i in range(2, sqrt_b+1):
        if not is_prime[i]: continue

        j = i * i # 2*iではなく，i*iでよいはず
        while j * j <= B:
            is_prime[j] = False
            j += i

        # A以上の最小のiの倍数
        start = A + (-A) % i
        if start == i:
            start = i * 2

        q = start 
        while q <= B:
            is_prime2[q-A] = False
            q += i

    return is_prime2

A, B = map(int, input().split())
a = kukan_eratos(A,B)
print(sum(a))
