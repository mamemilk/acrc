# https://atcoder.jp/contests/tenka1-2012-qualc/tasks/tenka1_2012_9

n = int(input())

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

print(eratos(n-1).count(True))