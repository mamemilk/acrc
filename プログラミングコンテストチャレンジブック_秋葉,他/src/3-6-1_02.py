# https://atcoder.jp/contests/arc042/tasks/arc042_b
# 垂線の最短距離もしくは，垂線が交わらない場合はどちらかの線への短い方

import math
px, py = map(int, input().split())
N = int(input()) # N角形

ab = [tuple(map(int, input().split())) for _ in range(N)]
ab += [ab[0]] # 最後の辺から最初の点に戻るので

ans = float('inf') 
for (ax, ay), (bx, by) in zip(ab, ab[1:]):
    ab_x = bx - ax
    ab_y = by - ay
    ap_x = px - ax
    ap_y = py - ay
    
    ab_squared = ab_x**2 + ab_y**2 # 各頂点は重ならないので0より大きい        
    t = (ap_x * ab_x + ap_y * ab_y) / ab_squared # 線上の点のパラメータtを求める(直交ベクトルは内積0から展開する)

    hx = ax + t * ab_x
    hy = ay + t * ab_y
    # 交点が線分上にあるかどうかにかかわらず垂線が常に最短
    ans = min(ans, math.sqrt((px - hx)**2 + (py - hy)**2))

print(ans)