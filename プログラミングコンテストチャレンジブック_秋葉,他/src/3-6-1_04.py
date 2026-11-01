# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=2661
#
# 折れ線1は (0,0) → 入力点 → (1000,0)，折れ線2は (0,1000) → 入力点 → (1000,1000)．
# 2本の折れ線は交わらないので，通れる最大直径 = 折れ線同士の最短距離
# = 全線分ペアの距離の最小値．線分同士が交わらないとき，線分間距離は
# 「端点と相手の線分の距離」4通りの最小値になる．
# 線分数は高々 51×51 なので総当たりで十分．

import math

def point_segment_dist(p, a, b):
    """点pと線分abの距離"""
    ax, ay = a
    bx, by = b
    px, py = p
    dx, dy = bx - ax, by - ay
    L2 = dx*dx + dy*dy
    if L2 == 0:
        return math.hypot(px - ax, py - ay)
    t = ((px - ax)*dx + (py - ay)*dy) / L2
    t = max(0.0, min(1.0, t))
    return math.hypot(px - (ax + t*dx), py - (ay + t*dy))

def segment_dist(a, b, c, d):
    """線分abと線分cdの距離(交わらない前提)"""
    return min(point_segment_dist(a, c, d),
               point_segment_dist(b, c, d),
               point_segment_dist(c, a, b),
               point_segment_dist(d, a, b))

N = int(input())
A = [tuple(map(int, input().split())) for _ in range(N)]
N = int(input())
B = [tuple(map(int, input().split())) for _ in range(N)]

A = [(0, 0)] + A + [(1000, 0)]
B = [(0, 1000)] + B + [(1000, 1000)]

min_gap = float('inf')
for a1, a2 in zip(A, A[1:]):
    for b1, b2 in zip(B, B[1:]):
        min_gap = min(min_gap, segment_dist(a1, a2, b1, b2))

print(f"{min_gap:.10f}")