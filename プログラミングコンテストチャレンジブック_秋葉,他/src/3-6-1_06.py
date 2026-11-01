# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=2316
# 
# muzui.... 
# ある点からある線分に距離1の交点を引けるか？という問題を繰り返せばよい。

import numpy as np

def circle_segment_intersection(A, P, Q, r=1.0):
    """
    点Aから距離rにある、線分P-Q上の交点を全部返す。
    """
    A = np.asarray(A, dtype=float)
    P = np.asarray(P, dtype=float)
    Q = np.asarray(Q, dtype=float)

    d = Q - P
    s = P - A

    a = np.dot(d, d)
    b = 2 * np.dot(s, d)
    c = np.dot(s, s) - r*r

    disc = b*b - 4*a*c
    if disc < 0:
        return []
    sqrt_disc = np.sqrt(disc)
    # 桁落ちを抑えた二次方程式の解
    q = -0.5 * (b + np.copysign(sqrt_disc, b))
    if q == 0:
        roots = [-b / (2*a)]
    else:
        roots = [q/a, c/q]
    return [P + t*d for t in roots if -1e-9 <= t <= 1 + 1e-9]

def next_rotation(A, others, XY):
    """
    軸Aのまわりに時計回りに回したとき、othersの中で最初に床に触れる角度を返す。
    """
    best = None
    for X0 in others:
        rel = X0 - A
        a0 = np.arctan2(rel[1], rel[0])
        for P, Q in zip(XY, XY[1:]):
            for X in circle_segment_intersection(A, P, Q, np.linalg.norm(rel)):
                a1 = np.arctan2(X[1]-A[1], X[0]-A[0])
                theta = (a0 - a1) % (2*np.pi)   # 時計回りの角度
                if theta < 1e-7:                # すでに床にある頂点(軸の西隣など)
                    continue
                if best is None or theta < best:
                    best = theta
    return best

def rotate_cw(points, center, theta):
    c, s = np.cos(theta), np.sin(theta)
    R = np.array([[c, s], [-s, c]])
    return [center + R @ (p - center) for p in points]

def floor_y(XY, x):
    for (x0, y0), (x1, y1) in zip(XY, XY[1:]):
        if x0 - 1e-9 <= x <= x1 + 1e-9:
            return y0 + (y1 - y0) * (x - x0) / (x1 - x0)
    return -np.inf

N, A, B = map(int, input().split())
XY = [list(map(int, input().split())) for _ in range(N)]

xa = A
ya = (XY[1][1] - XY[0][1]) / (XY[1][0] - XY[0][0]) * (A - XY[0][0]) + XY[0][1]

A = np.array([xa, ya], dtype=float)

# 初期の正方形：西端Aから最初の線分に沿って一辺を置く
cross = circle_segment_intersection(A, XY[0], XY[1])
cross = max(cross, key=lambda X: X[0])
chokkaku = np.array([-(cross[1]-A[1]), (cross[0]-A[0])])
corners = [A, cross, cross + chokkaku, A + chokkaku]   # 反時計回り
A = cross

count = 0

while True:
    others = [X for X in corners if X is not A]
    theta = next_rotation(A, others, XY)
    corners = rotate_cw(corners, A, theta)
    count += 1

    # 床に接している頂点のうち最も東のものを次の軸にする
    touching = [X for X in corners if abs(X[1] - floor_y(XY, X[0])) < 1e-7]
    A = max(touching, key=lambda X: X[0])
    if A[0] > B:
        break

print(["Red", "Green", "Blue", "White"][count%4])