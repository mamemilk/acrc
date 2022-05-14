#https://atcoder.jp/contests/abc188/tasks/abc188_b

N=int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

dp=0
for i in range(N):
    dp += A[i] * B[i]

if dp == 0:
    print('Yes')
else:
    print('No')