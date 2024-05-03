# https://atcoder.jp/contests/arc017/tasks/arc017_1
# 

def eratos(M):
    is_prime = [True for _ in range(M+1)] # True when found as prime
    is_prime[0] = False
    is_prime[1] = False
    # for s in range(2,):
    i = 2
    while i * i <= M:
        if is_prime[i]: # prime
            j = i*i
            while j <= M:
                is_prime[j] = False
                j += i
        i += 1
    return is_prime

N = int(input())
# N = 1000000

arr = eratos(1000000)
# arr = eratos(30)
print('YES' if arr[N] else 'NO')