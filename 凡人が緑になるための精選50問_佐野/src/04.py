#https://atcoder.jp/contests/abc191/tasks/abc191_b

N,X = map(int, input().split())
A = list(map(int, input().split()))

Ad = []
for i in range(N):
    if A[i] == X:
        pass
    else:
        Ad.append(str(A[i]))

print(" ".join(Ad))