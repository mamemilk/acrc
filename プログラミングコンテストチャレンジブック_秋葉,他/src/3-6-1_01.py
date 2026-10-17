# https://atcoder.jp/contests/abc002/tasks/abc002_3
# ベクトルの外積はそのベクトルの平行四辺形の面積なのでそれを2で割る．

xa, ya, xb, yb, xc, yc = map(int, input().split())

a = (xb - xa)
b = (yb - ya)
c = (xc - xa)
d = (yc - ya)
print(abs(a*d - b*c) / 2)