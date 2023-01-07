# https://atcoder.jp/contests/abc083/tasks/arc088_a

X,Y = map(int, input().split())

temp = X
i = 0

while temp <= Y:
    temp = temp*2
    i += 1

print(i)