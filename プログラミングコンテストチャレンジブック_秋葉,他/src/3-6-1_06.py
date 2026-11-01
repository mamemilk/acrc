# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=2316
# 
# muzui.... 
# ある点からある線分に距離1の交点を引けるか？という問題を繰り返せばよい。

import numpy as np

def circle_segment_intersection(A, P, Q):
    """
    点Aから距離1にある、線分P-Q上の交点を返す。
    交点が複数ある場合はPに近い方を返す。が、どういう場合だ？
    存在しない場合はNone。
    """
    A = np.asarray(A, dtype=float)
    P = np.asarray(P, dtype=float)
    Q = np.asarray(Q, dtype=float)

    d = Q - P
    r = P - A

    a = np.dot(d, d)
    b = 2 * np.dot(r, d)
    c = np.dot(r, r) - 1

    disc = b*b - 4*a*c
    if disc < 0:
        return None
    sqrt_disc = np.sqrt(disc)
    # 桁落ちを抑えた二次方程式の解
    q = -0.5 * (b + np.copysign(sqrt_disc, b))
    if q == 0:
        roots = [-b / (2*a)]
    else:
        roots = [q/a, c/q]
    # 線分上の交点で、Aより東にある採用
    valid = [t for t in roots if 0 <= t <= 1]
    if not valid:
        return None
    t = max(valid)
    if (P + t*d)[0] > A[0]:
        return P + t*d
    else:
        None

N, A, B = map(int, input().split())
XY = [list(map(int, input().split())) for _ in range(N)]

xa = A
ya = (XY[1][1] - XY[0][1]) / (XY[1][0] - XY[0][0]) * (A - XY[0][0]) + XY[0][1]

A = [xa, ya]

count = 0

while len(XY) >= 2:
    P = XY[0]
    Q = XY[1]

    cross = circle_segment_intersection(A, P, Q)
    if cross is not None:
        print('step', cross)
        chokkaku = [-(cross[1]-A[1]), (cross[0]-A[0])]
        A = cross
        count += 1
        if A[0] >= B or A[0]+chokkaku[0] >= B:
            break
    else:
        XY.pop(0)

print(["Red", "White", "Blue", "Green"][(count-1)%4])