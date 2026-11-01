# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=2316
# ある点からある線分に距離1の交点を引けるか？という問題を繰り返せばよい。
# ただし対角の頂点(距離√2)が先に床にぶつかる場合があるので、それも調べる。
# numpyが使えないので、非Numpyで書き直す

import math

def circle_segment_intersection(A, P, Q, r=1.0):
    """
    点Aから距離rにある、線分P-Q上の交点を返す。
    交点が複数ある場合は東側(tが大きい方)を返す。
    存在しない場合はNone。
    """
    dx, dy = Q[0] - P[0], Q[1] - P[1]
    sx, sy = P[0] - A[0], P[1] - A[1]

    a = dx*dx + dy*dy
    b = 2 * (sx*dx + sy*dy)
    c = sx*sx + sy*sy - r*r

    disc = b*b - 4*a*c
    if disc < 0:
        return None
    sqrt_disc = math.sqrt(disc)
    # 桁落ちを抑えた二次方程式の解
    q = -0.5 * (b + math.copysign(sqrt_disc, b))
    if q == 0:
        roots = [-b / (2*a)]
    else:
        roots = [q/a, c/q]
    # 線分上の交点で、Aより東にあるものを採用
    valid = [t for t in roots if 0 <= t <= 1]
    if not valid:
        return None
    t = max(valid)
    X = (P[0] + t*dx, P[1] + t*dy)
    if X[0] > A[0]:
        return X
    else:
        return None

def find_cross(A, XY, start, r):
    """
    線分 XY[start:] の中で、Aから距離rの東側の交点を探す。
    複数の線分で見つかったら最も東の線分のものを返す。
    """
    res = None, start
    for i in range(start, len(XY) - 1):
        cross = circle_segment_intersection(A, XY[i], XY[i+1], r)
        if cross is not None:
            res = cross, i
    return res

N, A, B = map(int, input().split())
XY = [list(map(int, input().split())) for _ in range(N)]

xa = A
ya = (XY[1][1] - XY[0][1]) / (XY[1][0] - XY[0][0]) * (A - XY[0][0]) + XY[0][1]

A = (float(xa), ya)

count = 0
seg = 0

while True:
    cross1, seg1 = find_cross(A, XY, seg, 1.0)            # 隣の頂点
    cross2, seg2 = find_cross(A, XY, seg, math.sqrt(2))   # 対角の頂点
    if cross1 is None:
        break

    p1 = (cross1[0] - A[0], cross1[1] - A[1])
    p2 = (cross2[0] - A[0], cross2[1] - A[1]) if cross2 is not None else p1
    # 対角の頂点は隣の頂点より45°手前にある。
    # 距離√2の床上の点が距離1の点より45°以上反時計回り側なら、対角が先にぶつかる。
    if p1[0]*p2[1] - p1[1]*p2[0] <= 1.0:
        A, seg = cross1, seg1
        count += 1
    else:
        A, seg = cross2, seg2
        count += 2

    if A[0] > B:
        break

print(["Red", "Green", "Blue", "White"][(count-1)%4])

# import numpy as np

# def circle_segment_intersection(A, P, Q, r=1.0):
#     """
#     点Aから距離rにある、線分P-Q上の交点を返す。
#     交点が複数ある場合は東側(tが大きい方)を返す。
#     存在しない場合はNone。
#     """
#     A = np.asarray(A, dtype=float)
#     P = np.asarray(P, dtype=float)
#     Q = np.asarray(Q, dtype=float)

#     d = Q - P
#     s = P - A

#     a = np.dot(d, d)
#     b = 2 * np.dot(s, d)
#     c = np.dot(s, s) - r*r

#     disc = b*b - 4*a*c
#     if disc < 0:
#         return None
#     sqrt_disc = np.sqrt(disc)
#     # 桁落ちを抑えた二次方程式の解
#     q = -0.5 * (b + np.copysign(sqrt_disc, b))
#     if q == 0:
#         roots = [-b / (2*a)]
#     else:
#         roots = [q/a, c/q]
#     # 線分上の交点で、Aより東にあるものを採用
#     valid = [t for t in roots if 0 <= t <= 1]
#     if not valid:
#         return None
#     t = max(valid)
#     if (P + t*d)[0] > A[0]:
#         return P + t*d
#     else:
#         return None

# def find_cross(A, XY, start, r):
#     """
#     線分 XY[start:] の中で、Aから距離rの東側の交点を探す。
#     複数の線分で見つかったら最も東の線分のものを返す。
#     """
#     res = None, start
#     for i in range(start, len(XY) - 1):
#         cross = circle_segment_intersection(A, XY[i], XY[i+1], r)
#         if cross is not None:
#             res = cross, i
#     return res

# N, A, B = map(int, input().split())
# XY = [list(map(int, input().split())) for _ in range(N)]

# xa = A
# ya = (XY[1][1] - XY[0][1]) / (XY[1][0] - XY[0][0]) * (A - XY[0][0]) + XY[0][1]

# A = [xa, ya]

# count = 0
# seg = 0

# while True:
#     cross1, seg1 = find_cross(A, XY, seg, 1.0)          # 隣の頂点
#     cross2, seg2 = find_cross(A, XY, seg, np.sqrt(2))   # 対角の頂点
#     if cross1 is None:
#         break

#     p1 = cross1 - A
#     p2 = cross2 - A if cross2 is not None else p1
#     # 対角の頂点は隣の頂点より45°手前にある。
#     # 距離√2の床上の点が距離1の点より45°以上反時計回り側なら、対角が先にぶつかる。
#     if p1[0]*p2[1] - p1[1]*p2[0] <= 1.0:
#         A, seg = cross1, seg1
#         count += 1
#     else:
#         A, seg = cross2, seg2
#         count += 2

#     if A[0] > B:
#         break

# print(["Red", "Green", "Blue", "White"][(count-1)%4])


