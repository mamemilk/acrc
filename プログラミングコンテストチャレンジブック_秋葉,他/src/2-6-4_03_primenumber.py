# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=0009&lang=jp

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

while a := input():
    N = int(a)
    print(arr[:N+1].count(True))
