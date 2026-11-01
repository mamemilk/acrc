# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=1039
# 
# Pi = (FPix, FPiy) : Frisbee pos 
# Fi = (FVix, FViy) : Fresbee velo 
# Di = (Dix, Diy),  : Dog Pos 
# u  = (cosθ, sinθ) : Dog Angle
# 
# 
# Pi + t Fi = Di + u Vi t 
#   ==> 最小のtが知りたい。
# Vi t u = Pi - Di + tFi 
#   ||u|| = 1 　なので、
# |Vi t|^2 = |Pi - Di + tFi|^2
# 
# ( ||Fi||^2 - Vi^2 )t^2 + 2(r F) t + ||r||^2 = 0
#
#　r=Pi - Di
# 

# tは判別式が成り立つなら、二次方程式の解の小さい方。
#
# で、ここで、θそのものは求めなくて良いことがわかる。ここがわからなかったので非常に悔しい。
# 犬の次地点への位置の更新は以下の移動量で行うことができる。tがわかれば求まる。
# Vi t u = Pi - Di + tFi
# 


import numpy as np

def eval():
    N, M = map(int, input().split()) # N is num dogs, M is num frisbees
    if N == 0 and M == 0:
        return False

    Di = np.zeros((N, 2))
    Vi = np.zeros((N))

    Pi = np.zeros((M, 2)) # Frisbee pos
    Fi = np.zeros((M, 2)) # Fresbee velo 

    for _ in range(N):
        Dx, Dy, V = map(int, input().split())
        Di[_] = [Dx, Dy]
        Vi[_] = V
    for _ in range(M):
        px, py, fx, fy = map(int, input().split())
        Pi[_] = [px, py]
        Fi[_] = [fx, fy]

    def intercept_times(P, F, D, V):
        """
        P: (2,)   Frisbee position
        F: (2,)   Frisbee velocity
        D: (N, 2) Dog positions
        V: (N,)   Dog speeds
        """
        r = P[None, :] - D

        a = np.dot(F, F) - V**2
        b = 2 * np.sum(r * F[None, :], axis=1)
        c = np.sum(r**2, axis=1)

        t = np.full(len(V), np.inf)

        # cはフリスビーからの距離なので、フリスビー位置にいる犬は0
        at_target = (c == 0)
        if np.any(at_target):
            t[at_target] = 0
            return t

        # a == 0なら、bt + c = 0を解く。
        linear = (a == 0) & (b != 0) & ~at_target
        t_linear = -c[linear] / b[linear]
        t[linear] = np.where(t_linear >= 0, t_linear, np.inf)

        # 二次式を解く
        disc = b**2 - 4*a*c
        valid = (a != 0) & (disc >= 0) & ~at_target

        if np.any(valid):
            av = a[valid]
            bv = b[valid]
            cv = c[valid]

            sqrt_disc = np.sqrt(disc[valid])
            q = -0.5 * (bv + np.copysign(sqrt_disc, bv))

            t1 = np.full(len(q), np.inf)
            t2 = np.full(len(q), np.inf)

            nonzero = (q != 0)
            t1[nonzero] = q[nonzero] / av[nonzero]
            t2[nonzero] = cv[nonzero] / q[nonzero]

            zero = ~nonzero
            t1[zero] = -bv[zero] / (2 * av[zero])

            t1 = np.where(t1 >= 0, t1, np.inf)
            t2 = np.where(t2 >= 0, t2, np.inf)

            t[valid] = np.minimum(t1, t2)

        return t

    counts = np.zeros(N, dtype=np.int64)

    for j in range(M):
        P = Pi[j]
        F = Fi[j]

        # Each dog's earliest interception time
        ti = intercept_times(P, F, Di, Vi)

        winner = np.argmin(ti)
        T = ti[winner]

        if not np.isfinite(T):
            continue

        counts[winner] += 1

        # Each dog aims at its own earliest interception point
        valid = np.isfinite(ti) & (ti > 0)

        target = P[None, :] + ti[valid, None] * F[None, :]

        ratio = T / ti[valid]

        Di[valid] += ratio[:, None] * (target - Di[valid])

    print(*counts)
    return True

while eval():
    pass

