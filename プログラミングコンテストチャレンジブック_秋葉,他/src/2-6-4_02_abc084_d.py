# https://atcoder.jp/contests/abc084/tasks/abc084_d



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

arr = eratos(10**5)

nitasuuji = []

for i in range(3, 10**5, 2):
    if arr[i]:
        j = (i + 1) // 2
        if arr[j]:
            nitasuuji.append(i)

# print(nitasuuji)    

# 累積和

Q = int(input())
for _ in range(Q):
    l, r = map(int, input().split())
    print(len(list(filter(lambda ele: l<=ele and ele<=r, nitasuuji))))


