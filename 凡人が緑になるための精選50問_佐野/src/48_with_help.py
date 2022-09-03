'''
https://atcoder.jp/contests/abc178/tasks/abc178_e

テキストを参照した．無念．

マンハッタン距離→チェビシェフ距離に変換

'''

N = int(input())

points = []
for i in range(N):
    x,y = map(int, input().split())
    points.append((x,y))

xs_converted = []
ys_converted = []

for (x,y) in points:
    xs_converted.append(x+y)
    ys_converted.append(x-y)

print(max(abs(max(xs_converted) - min(xs_converted)), 
          abs(max(ys_converted) - min(ys_converted))))
