# https://atcoder.jp/contests/abc197/tasks/abc197_d
# アフィン変換をそのまま実装．

from math import pi, sin, cos

N = int(input())
x,y = map(int, input (). split())

xn2, yn2 = map(int, input().split())

Cx = (x + xn2 ) / 2
Cy = (y + yn2 ) / 2

t = 2*pi / N

x_ = cos(t) * x - sin(t) * y + Cx-Cx*cos (t) + Cy*sin(t)
y_ = sin(t) * x + cos(t) * y + Cy-Cx*sin(t) - Cy*cos(t)

print(x_, y_)