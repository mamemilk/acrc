# https://atcoder.jp/contests/agc033/tasks/agc033_d

H, W = map(int, input().split())

Aij = []
for _ in range(H):
    Aij.append([0 if s=="." else 1 for s in input()])


print("give...")