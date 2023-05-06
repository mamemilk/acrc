# https://atcoder.jp/contests/abc085/tasks/abc085_b

N = int(input())
D = set()
for _ in range(N):
    d = int(input())
    D.add(d)

print(len(D))

