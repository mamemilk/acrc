# https://atcoder.jp/contests/abc016/tasks/abc016_4
# 頂点と交差することはないので，各線分と交点が何個あるかを数える．
# 交点 / 2 + 1が分割個数
# 
# 交点が存在するかは外積の符号の個数で求める
#    A, Bが線分CDの両側にあるかは外積の符号が異なれば判定できる．
# 短いチョップ用にA, Bが線分CDの両側にあるかと，C, Dが線分ABの両側にあるかを判定する．

ax, ay, bx, by = map(int, input().split())
N = int(input())
XY = [tuple(map(int, input().split())) for _ in range(N)]
XY += [XY[0]]

count = 0 
for (x1, y1), (x2, y2) in zip(XY, XY[1:]):
    cross_c = (bx - ax) * (y1 - ay) - (by - ay) * (x1 - ax)
    cross_d = (bx - ax) * (y2 - ay) - (by - ay) * (x2 - ax)
    
    cross_a = (x2 - x1) * (ay - y1) - (y2 - y1) * (ax - x1)
    cross_b = (x2 - x1) * (by - y1) - (y2 - y1) * (bx - x1)

    if cross_c * cross_d < 0 and cross_a * cross_b < 0:
        count += 1

print(count//2+1)