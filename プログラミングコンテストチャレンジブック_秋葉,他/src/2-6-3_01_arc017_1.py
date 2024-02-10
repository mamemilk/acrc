# https://atcoder.jp/contests/arc017/tasks/arc017_1
# 

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

N = int(input())
# N = 1000000

arr = eratos(1000000)
# arr = eratos(30)
print('YES' if arr[N] else 'NO')