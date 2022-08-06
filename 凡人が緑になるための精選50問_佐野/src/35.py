# https://atcoder.jp/contests/abc146/tasks/abc146_c
# 自力で解けずにカンニング．

A, B, X = map(int, input().split())

def price(N):
    return A*N + B * len(str(N))

#left, right = 1,10**9+1
left, right = 1,10**20

while left < right-1:
    N = (left + right) // 2
    if price(N) <= X:
        left = N
    else:
        right = N

if price(1) > X:
    left = 0

if 10**9 < left:
    left = 10**9

if price(N) > X:
    left = 0

print(left) #, right)